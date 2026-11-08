"""Standard-library tests for the AI HOME safety-gate reference."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pui89_home.safety_gate import (
    ActionRequest,
    Decision,
    EvidenceStatus,
    evaluate_proposal,
)


GOOD_EVIDENCE = EvidenceStatus(
    source_present=True,
    timestamp_present=True,
    provenance_present=True,
    sensor_healthy=True,
    evidence_fresh=True,
    evidence_consistent=True,
    uncertainty_resolved=True,
)


class SafetyGateTests(unittest.TestCase):
    def test_complete_evidence_only_requests_human_review(self):
        decision, reasons = evaluate_proposal(
            GOOD_EVIDENCE, ActionRequest(category="report")
        )
        self.assertEqual(decision, Decision.REVIEW_REQUIRED)
        self.assertEqual(reasons, ("human_decision_required",))

    def test_each_missing_or_unsafe_evidence_condition_holds(self):
        fields = (
            "source_present",
            "timestamp_present",
            "provenance_present",
            "sensor_healthy",
            "evidence_fresh",
            "evidence_consistent",
            "uncertainty_resolved",
        )
        for field in fields:
            with self.subTest(field=field):
                values = GOOD_EVIDENCE.__dict__.copy()
                values[field] = False
                decision, reasons = evaluate_proposal(
                    EvidenceStatus(**values), ActionRequest(category="report")
                )
                self.assertEqual(decision, Decision.HOLD)
                self.assertTrue(reasons)

    def test_restricted_categories_are_blocked(self):
        categories = (
            "lock",
            "breaker",
            "valve",
            "appliance",
            "certified_alarm",
            "emergency_system",
            "motor",
            "actuator",
        )
        for category in categories:
            with self.subTest(category=category):
                decision, _ = evaluate_proposal(
                    GOOD_EVIDENCE, ActionRequest(category=category)
                )
                self.assertEqual(decision, Decision.BLOCKED)

    def test_execution_request_is_always_blocked(self):
        decision, reasons = evaluate_proposal(
            GOOD_EVIDENCE,
            ActionRequest(category="report", execution_requested=True),
        )
        self.assertEqual(decision, Decision.BLOCKED)
        self.assertIn("execution_not_authorised", reasons)

    def test_human_review_cannot_be_disabled(self):
        decision, reasons = evaluate_proposal(
            GOOD_EVIDENCE,
            ActionRequest(category="report", human_review_required=False),
        )
        self.assertEqual(decision, Decision.HOLD)
        self.assertIn("human_review_required", reasons)

    def test_no_decision_authorises_execution(self):
        decision, _ = evaluate_proposal(
            GOOD_EVIDENCE, ActionRequest(category="report")
        )
        self.assertIn(decision, (Decision.HOLD, Decision.BLOCKED, Decision.REVIEW_REQUIRED))


if __name__ == "__main__":
    unittest.main()
