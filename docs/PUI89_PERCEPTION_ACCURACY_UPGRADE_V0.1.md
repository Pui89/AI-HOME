# AI HOME / Homeguard — Perception Accuracy Upgrade v0.1

**Status:** Requirements specified; visual detection is not a diagnosis or proof of home safety.

Shared contract: [PUI89 Perception and Accuracy Standard](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_AND_ACCURACY_STANDARD_V0.1.md).

## Priority perception tasks

1. Detect/segment visible smoke and flame; distinguish steam, dust, sunlight and common false positives.
2. Detect water leaks, puddles and waterline changes; corroborate with moisture/leak sensors where available.
3. Detect visible wall/ceiling cracks and compare the same location over time using registered viewpoints.
4. Detect dampness or mold-like visual patterns without diagnosing species, toxicity or hidden mold.
5. Identify visibly damaged electrical fittings, but never infer that a circuit is de-energized or electrically safe from an image.
6. Detect people, pets and other animals with privacy-preserving processing.
7. Recognize doors, windows, stairs, furniture and navigation obstacles.
8. Fuse temperature, humidity, vibration, smoke, water and electrical-monitor readings only with known units, calibration and timestamps.
9. Detect camera obstruction, sensor drift, missing observations and stale room maps.

## Temporal change protocol

Store room/area identifiers, camera pose, capture time, image registration quality and evidence references. Distinguish new, persistent, growing, repaired, uncertain and unobserved conditions. Do not report deterioration if viewpoint/lighting differences could explain the change.

## Evaluation

Measure per-class precision/recall, crack localization error, leak segmentation IoU, false alarms from steam/dust/reflections, temporal-change precision, sensor-fusion disagreement and missed-hazard rate. Include day/night, shadows, reflective surfaces, low light, clutter and camera movement.

**Safety boundary:** no visual-only structural, electrical, fire-system or health diagnosis. Escalate uncertainty to a qualified person; perception does not authorize physical intervention.
