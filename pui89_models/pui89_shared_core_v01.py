"""Map caller-supplied AI HOME vision proposals to Shared AI Core v0.1."""
from __future__ import annotations
from datetime import datetime

SCHEMA_VERSION = "0.1.0"
ALLOWED_MODALITIES = {"rgb", "depth", "thermal", "audio", "lidar", "radar", "imu", "gps", "xray", "chemical", "text", "other"}

def _timestamp(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("timestamp must be a non-empty ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp must be valid ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    return value

def build_home_v01_records(*, observation_id, source_ref, observed_at, detections,
                           modality="rgb", model_id="unspecified", recorded_at=None):
    """Wrap existing model proposals; no model is loaded or inference executed here."""
    observed_at = _timestamp(observed_at)
    recorded_at = _timestamp(recorded_at or observed_at)
    if not isinstance(observation_id, str) or not observation_id.strip():
        raise ValueError("observation_id must be a non-empty string")
    if not isinstance(source_ref, str) or not source_ref.strip():
        raise ValueError("source_ref must be a non-empty string")
    if modality not in ALLOWED_MODALITIES:
        raise ValueError("modality is not supported by Shared AI Core v0.1")
    if not isinstance(detections, list) or not detections or not all(isinstance(item, dict) for item in detections):
        raise ValueError("detections must be a non-empty list of proposal objects")

    observation = {
        "schema_version": SCHEMA_VERSION,
        "observation_id": observation_id,
        "observed_at": observed_at,
        "source": {
            "source_id": observation_id,
            "source_type": "software",
            "device_or_system": "PUI89 AI HOME vision adapter",
        },
        "modality": modality,
        "payload": {
            "model_id": model_id,
            "proposals": detections,
            "interpretation": "model_proposals_require_human_review",
        },
        "quality": {
            "status": "unknown",
            "notes": "No independent sensor verification, model accuracy validation, or safety validation is implied.",
        },
        "uncertainty": {
            "description": "Model proposals may be incorrect, incomplete, stale, or affected by occlusion and domain shift.",
        },
        "provenance": {"recorded_at": recorded_at, "dataset_or_file": source_ref},
    }
    proposal = {
        "schema_version": SCHEMA_VERSION,
        "proposal_id": f"home-vision-review:{observation_id}",
        "created_at": recorded_at,
        "objective": "Request human review of AI HOME vision proposals.",
        "actions": [{
            "action_id": f"review:{observation_id}",
            "description": "Ask a human reviewer to inspect the source image and model proposals.",
            "risk_level": "unknown",
            "preconditions": [
                "Confirm source permission and provenance.",
                "Treat model outputs as unverified proposals, not hazard findings.",
                "Use certified independent safety devices for smoke, fire, carbon monoxide, and electrical protection.",
            ],
            "expected_effect": "A human reviewer confirms, rejects, or requests more evidence.",
            "hazards": [
                "False positives and missed detections may occur.",
                "This record does not diagnose structural, electrical, fire, or health hazards.",
            ],
            "evidence_refs": [observation_id],
        }],
        "authority": {
            "mode": "advisory_only",
            "human_approval_required": True,
            "execution_authorized": False,
        },
        "uncertainties": [
            "No validated model accuracy or real-world safety performance is established.",
            "No robot movement, alarm, lock, valve, breaker, or appliance command is authorised.",
        ],
    }
    return {"observation": observation, "action_proposal": proposal}
