"""Dependency-free tests for the opt-in PUI89 AI HOME model adapter.

These tests validate adapter guardrails and import behaviour only. They do not
load model weights, install dependencies, run inference or measure accuracy.
"""
import os
import unittest
from pathlib import Path
from unittest.mock import patch

from pui89_models import hf_vision


class HFVisionAdapterTests(unittest.TestCase):
    def test_checkpoint_ids_are_explicit(self):
        self.assertEqual(
            hf_vision.OWLV2_MODEL_ID,
            "google/owlv2-base-patch16-ensemble",
        )
        self.assertEqual(
            hf_vision.DEPTH_MODEL_ID,
            "Intel/dpt-hybrid-midas",
        )

    def test_import_does_not_require_model_runtime(self):
        # Importing the module exposes adapters without importing torch or
        # transformers or triggering a model download.
        self.assertTrue(callable(hf_vision.load_owlv2))
        self.assertTrue(callable(hf_vision.load_dpt_hybrid))

    def test_local_cache_only_is_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertTrue(hf_vision._local_only(False))

    def test_download_requires_explicit_environment_opt_in(self):
        with patch.dict(os.environ, {"PUI89_ALLOW_MODEL_DOWNLOAD": "0"}):
            self.assertTrue(hf_vision._local_only(False))
        with patch.dict(os.environ, {"PUI89_ALLOW_MODEL_DOWNLOAD": "1"}):
            self.assertFalse(hf_vision._local_only(False))

    def test_download_can_be_explicitly_enabled_per_call(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(hf_vision._local_only(True))

    def test_invalid_threshold_is_rejected_before_torch_import(self):
        with patch.dict("sys.modules", {"torch": None}):
            with self.assertRaises(ValueError):
                hf_vision.detect_objects(None, ["person"], threshold=-0.01)
            with self.assertRaises(ValueError):
                hf_vision.detect_objects(None, ["person"], threshold=1.01)

    def test_empty_labels_are_rejected_before_torch_import(self):
        with patch.dict("sys.modules", {"torch": None}):
            with self.assertRaises(ValueError):
                hf_vision.detect_objects(None, ["", "  "])

    def test_adapter_keeps_outputs_as_reviewable_proposals(self):
        source = Path(hf_vision.__file__).read_text(encoding="utf-8")
        self.assertIn("MODEL_PROPOSAL_REQUIRES_REVIEW", source)
        self.assertIn("local_files_only=local_only", source)
        self.assertIn("PUI89_ALLOW_MODEL_DOWNLOAD", source)


if __name__ == "__main__":
    unittest.main()
