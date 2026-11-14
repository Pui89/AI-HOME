import unittest
from pui89_perception.indoor import Detection, IndoorFrame, ProposalKind, build_indoor_world_state

class IndoorPerceptionTests(unittest.TestCase):
    def frame(self, **overrides):
        values = dict(timestamp="2026-11-14T10:00:00+07:00", frame_id="frame-001",
                      camera_available=True, frame_age_seconds=0.2,
                      localization_confidence=0.95, detections=())
        values.update(overrides)
        return IndoorFrame(**values)

    def test_fresh_empty_scene_only_continues_monitoring(self):
        result = build_indoor_world_state(self.frame())
        self.assertEqual(result.proposal.kind, ProposalKind.CONTINUE_MONITORING)
        self.assertEqual(result.world_state.status, "OBSERVED_NOT_VERIFIED_SAFE")
        self.assertFalse(result.proposal.execution_authority)

    def test_near_obstacle_requires_safe_hold(self):
        item = Detection("chair", 0.92, (0.1, 0.2, 0.5, 0.8), 0.6, "test_adapter")
        result = build_indoor_world_state(self.frame(detections=(item,)))
        self.assertEqual(result.proposal.kind, ProposalKind.SAFE_HOLD)
        self.assertEqual(result.world_state.obstacle_count, 1)

    def test_obstacle_without_calibrated_distance_holds(self):
        item = Detection("box", 0.88, (0.1, 0.2, 0.5, 0.8), None, "test_adapter")
        result = build_indoor_world_state(self.frame(detections=(item,)))
        self.assertEqual(result.proposal.kind, ProposalKind.SAFE_HOLD)
        self.assertIn("obstacle_distance_not_calibrated", result.world_state.uncertainty)

    def test_stale_frame_holds(self):
        result = build_indoor_world_state(self.frame(frame_age_seconds=3.0))
        self.assertEqual(result.proposal.kind, ProposalKind.SAFE_HOLD)
        self.assertIn("STALE_FRAME", {f.code for f in result.failures})

    def test_camera_loss_holds(self):
        result = build_indoor_world_state(self.frame(camera_available=False))
        self.assertEqual(result.proposal.kind, ProposalKind.SAFE_HOLD)
        self.assertIn("CAMERA_UNAVAILABLE", {f.code for f in result.failures})

    def test_uncertain_localization_holds(self):
        result = build_indoor_world_state(self.frame(localization_confidence=0.2))
        self.assertEqual(result.proposal.kind, ProposalKind.SAFE_HOLD)

    def test_person_is_reported_without_identity(self):
        item = Detection("person", 0.91, (0.2, 0.1, 0.6, 0.9), 2.5, "test_adapter")
        result = build_indoor_world_state(self.frame(detections=(item,)))
        self.assertEqual(result.world_state.people_count, 1)
        self.assertNotIn("identity", str(result.to_dict()).lower())

    def test_invalid_bbox_is_rejected_and_holds(self):
        item = Detection("chair", 0.9, (0.8, 0.2, 0.1, 0.9), 1.5, "test_adapter")
        result = build_indoor_world_state(self.frame(detections=(item,)))
        self.assertEqual(result.proposal.kind, ProposalKind.SAFE_HOLD)
        self.assertIn("INVALID_DETECTION", {f.code for f in result.failures})

    def test_low_confidence_detection_is_not_promoted_to_fact(self):
        item = Detection("person", 0.3, (0.2, 0.1, 0.6, 0.9), None, "test_adapter")
        result = build_indoor_world_state(self.frame(detections=(item,)))
        self.assertEqual(result.world_state.people_count, 0)
        self.assertIn("low_confidence:person", result.world_state.uncertainty)
        self.assertEqual(result.proposal.kind, ProposalKind.CONTINUE_MONITORING)

    def test_thresholds_reject_invalid_values(self):
        with self.assertRaises(ValueError):
            build_indoor_world_state(self.frame(), confidence_threshold=1.5)

if __name__ == "__main__":
    unittest.main()