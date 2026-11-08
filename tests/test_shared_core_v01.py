import json
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pui89_models"))
from pui89_shared_core_v01 import build_home_v01_records

class HomeSharedCoreV01Tests(unittest.TestCase):
    def make_bundle(self):
        return build_home_v01_records(
            observation_id="home-fixture-001",
            source_ref="synthetic://home/vision/001",
            observed_at="2026-11-01T00:00:00Z",
            recorded_at="2026-11-01T00:00:01Z",
            model_id="test-fixture-not-a-model",
            detections=[{
                "label": "possible water stain",
                "score": 0.62,
                "box_xyxy": [1.0, 2.0, 3.0, 4.0],
                "status": "MODEL_PROPOSAL_REQUIRES_REVIEW",
            }],
        )

    def test_vision_proposals_remain_unverified_and_advisory(self):
        bundle = self.make_bundle()
        self.assertEqual(bundle["observation"]["schema_version"], "0.1.0")
        self.assertEqual(bundle["observation"]["source"]["source_type"], "software")
        self.assertEqual(bundle["observation"]["quality"]["status"], "unknown")
        self.assertEqual(bundle["observation"]["payload"]["proposals"][0]["status"], "MODEL_PROPOSAL_REQUIRES_REVIEW")
        authority = bundle["action_proposal"]["authority"]
        self.assertEqual(authority["mode"], "advisory_only")
        self.assertIs(authority["human_approval_required"], True)
        self.assertIs(authority["execution_authorized"], False)

    def test_invalid_time_and_modality_are_rejected(self):
        args = dict(observation_id="x", source_ref="synthetic://x",
                    observed_at="2026-11-01T00:00:00Z", detections=[{"label":"x"}])
        with self.assertRaises(ValueError):
            build_home_v01_records(**{**args, "observed_at":"2026-11-01T00:00:00"})
        with self.assertRaises(ValueError):
            build_home_v01_records(**{**args, "modality":"ultrasound"})

    def test_shared_core_schema_required_fields_match(self):
        core_dir = os.environ.get("PUI89_SHARED_CORE_DIR")
        if not core_dir:
            self.skipTest("Shared AI Core checkout is supplied by GitHub Actions")
        schema_dir = Path(core_dir) / "schemas" / "v0.1"
        bundle = self.make_bundle()
        for key, filename in (("observation","observation.schema.json"),("action_proposal","action-proposal.schema.json")):
            schema = json.loads((schema_dir / filename).read_text(encoding="utf-8"))
            self.assertEqual(schema["properties"]["schema_version"]["const"], "0.1.0")
            self.assertTrue(set(schema["required"]).issubset(bundle[key].keys()))

if __name__ == "__main__":
    unittest.main()
