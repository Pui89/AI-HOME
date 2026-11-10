# AI HOME: Spatial Intelligence integration profile

## Intended use
Advisory indoor room layout, obstacle and spatial-change context.

## Planned tasks
- Indoor room and obstacle geometry
- Spatial change records with provenance and timestamps
- Evidence references for human inspection

## Safety boundaries
- Geometry does not identify fire, gas, electrical, structural or health hazards.
- No emergency response or home-safety guarantee.
- Privacy-preserving local processing and sensor permissions require separate review.

The common interfaces are under development in [Shared AI Core PR #26](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/26), which remains draft and unmerged. This profile documents the intended integration contract only; no runtime import, sensor driver or physical integration is claimed.

Require lawful data provenance, calibration, synchronized timestamps, sensor-health checks, uncertainty handling, synthetic fault tests and human review before runtime use. No physical actuation is enabled.

**Status:** profile documentation added; runtime adapter, real sensor integration, accuracy and field validation pending. No paid services or hardware purchase required.
