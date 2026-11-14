# AI HOME Stage 2 — Indoor Perception MVP

**Status:** Initial software implementation; tests must pass before this work is treated as verified.
**Scope:** CPU-first, model-agnostic decision layer. No hardware purchase, sensor integration, robot motion or cloud service is included.

## Implemented
- Typed frame and candidate-detection inputs.
- Validation of normalized bounding boxes, confidence values and optional calibrated distance.
- Minimal WorldState with people count, object labels, obstacle count, evidence sources and explicit uncertainty.
- SAFE_HOLD proposals for camera loss, stale frames, invalid detections, uncertain localization, missing obstacle distance or a nearby obstacle.
- ActionProposal is a record only: it has no execution authority and cannot command motors or actuators.
- FailureReport records rejected or uncertain evidence.
- Standard-library unittest tests; no third-party package is required.

## Not implemented

This module does not run object detection, person detection, tracking, segmentation, mapping, depth estimation or SLAM. It does not read a camera, estimate distance from image size, identify people or establish a safe path. Candidate detections must come from a separately reviewed adapter and calibrated source. Unit tests validate deterministic software rules only, not real-world perception accuracy.

## Run tests locally

From the repository root, run:

    python -m unittest discover -s tests -p 'test_indoor_perception.py' -v

## Acceptance gates
1. All deterministic unit tests pass on the target CPU environment.
2. A reviewed local vision adapter supplies documented class labels, confidence, normalized boxes and provenance.
3. Distance is accepted only from a calibrated depth/ranging source with its calibration record.
4. A labelled indoor evaluation set measures per-class precision/recall, obstacle miss rate, false alarms and uncertainty behaviour.
5. Supervised stationary tests demonstrate stale-frame, camera-loss and localization-loss handling.
6. No movement or actuator interface is connected in this stage.

## Evidence boundary

This is a first deterministic decision layer, not a completed AI perception system or robot. Do not report detection accuracy, real sensor performance, navigation capability or product readiness until the corresponding tests and evidence exist.