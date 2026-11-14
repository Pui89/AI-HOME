"""Deterministic, model-agnostic indoor perception decision layer.

This module does not run a vision model or control hardware. It validates
candidate detections supplied by a future local vision adapter, builds a
small evidence-backed WorldState, and emits a human-reviewable proposal.
"""

from __future__ import annotations
from dataclasses import asdict, dataclass
from enum import Enum
from math import isfinite
from typing import Any

class ProposalKind(str, Enum):
    CONTINUE_MONITORING = "CONTINUE_MONITORING"
    REQUEST_HUMAN_REVIEW = "REQUEST_HUMAN_REVIEW"
    SAFE_HOLD = "SAFE_HOLD"

@dataclass(frozen=True)
class Detection:
    """Candidate detection from an external, separately validated model."""
    label: str
    confidence: float
    bbox_xyxy: tuple[float, float, float, float]
    distance_m: float | None = None
    source: str = "unverified_vision_adapter"

@dataclass(frozen=True)
class IndoorFrame:
    """One frame metadata record; no image is stored by this module."""
    timestamp: str
    frame_id: str
    camera_available: bool
    frame_age_seconds: float
    localization_confidence: float
    detections: tuple[Detection, ...] = ()

@dataclass(frozen=True)
class ActionProposal:
    kind: ProposalKind
    reason: str
    requires_human_review: bool = True
    execution_authority: bool = False

@dataclass(frozen=True)
class FailureReport:
    code: str
    message: str
    source: str = "indoor_perception"

@dataclass(frozen=True)
class WorldState:
    timestamp: str
    frame_id: str
    status: str
    people_count: int
    object_labels: tuple[str, ...]
    obstacle_count: int
    nearest_obstacle_distance_m: float | None
    evidence_sources: tuple[str, ...]
    uncertainty: tuple[str, ...]

@dataclass(frozen=True)
class PerceptionResult:
    world_state: WorldState
    proposal: ActionProposal
    failures: tuple[FailureReport, ...]

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-friendly representation without custom dependencies."""
        result = asdict(self)
        result["proposal"]["kind"] = self.proposal.kind.value
        return result

_OBSTACLE_LABELS = frozenset({
    "obstacle", "chair", "table", "box", "bag", "cable", "spill",
    "furniture", "pet", "person",
})
_PERSON_LABELS = frozenset({"person", "human"})

def _valid_detection(detection: Detection) -> bool:
    if not detection.label or not detection.source or len(detection.bbox_xyxy) != 4:
        return False
    values = (*detection.bbox_xyxy, detection.confidence)
    if not all(isfinite(v) for v in values):
        return False
    x1, y1, x2, y2 = detection.bbox_xyxy
    if not (0 <= x1 < x2 <= 1 and 0 <= y1 < y2 <= 1):
        return False
    if not 0 <= detection.confidence <= 1:
        return False
    if detection.distance_m is not None and (
        not isfinite(detection.distance_m) or detection.distance_m < 0
    ):
        return False
    return True

def build_indoor_world_state(
    frame: IndoorFrame, *, confidence_threshold: float = 0.50,
    stale_after_seconds: float = 2.0, near_obstacle_distance_m: float = 1.0,
    minimum_localization_confidence: float = 0.50,
) -> PerceptionResult:
    """Build a conservative WorldState from candidate detections.

    Distance is used only when supplied by a calibrated upstream source.
    Bounding-box size is never converted into physical distance. Invalid,
    stale or unavailable critical input results in SAFE_HOLD, not a safe claim.
    """
    failures: list[FailureReport] = []
    uncertainty: list[str] = []
    thresholds = (confidence_threshold, stale_after_seconds,
                  near_obstacle_distance_m, minimum_localization_confidence)
    if not all(isfinite(v) for v in thresholds):
        raise ValueError("thresholds must be finite numbers")
    if not 0 <= confidence_threshold <= 1:
        raise ValueError("confidence_threshold must be between 0 and 1")
    if stale_after_seconds < 0 or near_obstacle_distance_m < 0:
        raise ValueError("age and distance thresholds must be non-negative")
    if not 0 <= minimum_localization_confidence <= 1:
        raise ValueError("minimum_localization_confidence must be between 0 and 1")

    critical_failure = False
    if not frame.camera_available:
        failures.append(FailureReport("CAMERA_UNAVAILABLE", "Camera input is unavailable."))
        uncertainty.append("camera_unavailable")
        critical_failure = True
    if not isfinite(frame.frame_age_seconds) or frame.frame_age_seconds < 0:
        failures.append(FailureReport("INVALID_FRAME_AGE", "Frame age is invalid."))
        uncertainty.append("frame_freshness_unknown")
        critical_failure = True
    elif frame.frame_age_seconds > stale_after_seconds:
        failures.append(FailureReport("STALE_FRAME", "Frame is older than the allowed freshness limit."))
        uncertainty.append("stale_visual_evidence")
        critical_failure = True
    if (not isfinite(frame.localization_confidence)
            or not 0 <= frame.localization_confidence <= 1
            or frame.localization_confidence < minimum_localization_confidence):
        failures.append(FailureReport("LOCALIZATION_UNCERTAIN", "Localization confidence is invalid or below the minimum."))
        uncertainty.append("localization_uncertain")
        critical_failure = True

    valid: list[Detection] = []
    for detection in frame.detections:
        if not _valid_detection(detection):
            failures.append(FailureReport("INVALID_DETECTION", "A candidate detection failed schema validation."))
            uncertainty.append("invalid_detection_present")
            critical_failure = True
            continue
        if detection.confidence < confidence_threshold:
            uncertainty.append(f"low_confidence:{detection.label}")
            continue
        valid.append(detection)

    people = sum(d.label.lower() in _PERSON_LABELS for d in valid)
    obstacles = [d for d in valid if d.label.lower() in _OBSTACLE_LABELS]
    distances = [d.distance_m for d in obstacles if d.distance_m is not None]
    nearest = min(distances) if distances else None
    if obstacles and len(distances) != len(obstacles):
        uncertainty.append("obstacle_distance_not_calibrated")
        failures.append(FailureReport("OBSTACLE_DISTANCE_UNKNOWN", "At least one obstacle has no calibrated distance."))
        critical_failure = True
    if nearest is not None and nearest <= near_obstacle_distance_m:
        uncertainty.append("obstacle_within_stop_threshold")
        critical_failure = True

    if critical_failure:
        proposal = ActionProposal(ProposalKind.SAFE_HOLD, "Critical input is unavailable, stale, invalid or uncertain.")
    elif obstacles:
        proposal = ActionProposal(ProposalKind.REQUEST_HUMAN_REVIEW, "Scene observations are available; review before any physical action.")
    else:
        proposal = ActionProposal(ProposalKind.CONTINUE_MONITORING, "No supported obstacle proposal was received; continue observation only.")

    state = WorldState(
        timestamp=frame.timestamp, frame_id=frame.frame_id,
        status="UNCERTAIN" if critical_failure or uncertainty else "OBSERVED_NOT_VERIFIED_SAFE",
        people_count=people, object_labels=tuple(sorted({d.label for d in valid})),
        obstacle_count=len(obstacles), nearest_obstacle_distance_m=nearest,
        evidence_sources=tuple(sorted({d.source for d in valid})),
        uncertainty=tuple(sorted(set(uncertainty))),
    )
    return PerceptionResult(state, proposal, tuple(failures))