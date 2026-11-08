"""Conservative, dependency-free AI HOME safety-gate reference implementation.

This module is a software-only example. It is not connected to sensors, motors,
actuators, alarms, locks, breakers, valves, appliances, or emergency systems.
A REVIEW_REQUIRED result is not permission to execute an action.
"""
from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    HOLD = "HOLD"
    BLOCKED = "BLOCKED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"


@dataclass(frozen=True)
class EvidenceStatus:
    source_present: bool
    timestamp_present: bool
    provenance_present: bool
    sensor_healthy: bool
    evidence_fresh: bool
    evidence_consistent: bool
    uncertainty_resolved: bool


@dataclass(frozen=True)
class ActionRequest:
    category: str
    human_review_required: bool = True
    execution_requested: bool = False


# These categories are outside AI HOME's permitted control scope.
RESTRICTED_ACTION_CATEGORIES = frozenset(
    {
        "lock",
        "breaker",
        "valve",
        "appliance",
        "certified_alarm",
        "emergency_system",
        "motor",
        "actuator",
    }
)


def evaluate_proposal(
    evidence: EvidenceStatus, action: ActionRequest
) -> tuple[Decision, tuple[str, ...]]:
    """Return a fail-closed decision and machine-readable reasons.

    The only positive outcome is REVIEW_REQUIRED. This function never
    authorises execution, including when all evidence checks pass.
    """
    category = action.category.strip().lower()
    if category in RESTRICTED_ACTION_CATEGORIES:
        return Decision.BLOCKED, ("restricted_action_category",)

    if action.execution_requested:
        return Decision.BLOCKED, ("execution_not_authorised",)

    if not action.human_review_required:
        return Decision.HOLD, ("human_review_required",)

    checks = (
        ("source_missing", evidence.source_present),
        ("timestamp_missing", evidence.timestamp_present),
        ("provenance_missing", evidence.provenance_present),
        ("sensor_unhealthy", evidence.sensor_healthy),
        ("evidence_stale", evidence.evidence_fresh),
        ("evidence_conflicting", evidence.evidence_consistent),
        ("uncertainty_unresolved", evidence.uncertainty_resolved),
    )
    failures = tuple(reason for reason, passed in checks if not passed)
    if failures:
        return Decision.HOLD, failures

    return Decision.REVIEW_REQUIRED, ("human_decision_required",)
