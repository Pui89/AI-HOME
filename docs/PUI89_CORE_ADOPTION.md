# PUI89 Shared AI Core — AI HOME Adapter

**Status:** Integration plan; documentation only. Shared Core Network Intelligence v0.1 is available on the Shared AI Core main branch; AI HOME runtime adoption remains pending.
**Platform contract:** [PUI89 Evidence-to-Action Intelligence Platform](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_EVIDENCE_TO_ACTION_PLATFORM.md)

## Purpose

Use shared evidence, world-state, change tracking, uncertainty and safety proposal contracts for the AI HOME software platform and future HOME/NOMAD devices. This guide does not claim a completed robot or certified safety function.

## Shared Core Network Intelligence reference

The dependency-light Network Intelligence module is available at pui89_core/network_topology.py in [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core). It validates user-declared inventory and renders static SVG topology diagrams. The implementation and tests were merged through [PR #37](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/37); the corresponding [GitHub Actions run](https://github.com/Pui89/PUI89-Shared-AI-Core/actions/runs/42984419052) completed successfully.

Potential AI HOME use is limited to an optional inventory context for routers, switches, servers, access points and local compute devices. It may help a human understand which declared infrastructure supports the home platform. It must not be treated as a live sensor, health monitor, intrusion detector, or proof that a device is reachable or secure.

### Integration boundary

- Consume only a user-supplied, reviewed inventory; no automatic network discovery or port scanning.
- Keep network inventory separate from room/sensor observations unless a documented evidence relationship exists.
- Preserve source, timestamp, inventory revision, provenance and unknown/stale status.
- Represent any topology-derived state as a time-bounded estimate with explicit unknowns; do not infer device health from a drawn link.
- Any recommendation remains advisory, requires human review, and has execution_authorized=false.
- Never store passwords, API keys, private keys or Wi-Fi credentials in topology files.
- Treat topology exports as sensitive infrastructure data; keep them local/private unless the owner explicitly approves disclosure.
- No network configuration changes, remote commands, or physical actuation are in scope.

The current AI HOME repository has no verified runtime adapter for this module. Do not mark integration complete until a pinned interface, project-owned synthetic fixtures, negative tests, CI evidence and a retained conformance report exist.

## Domain observations

Represent each reading with sensor/source identity, timestamp, units, location/zone, quality, calibration/health status and provenance. Potential domains include temperature, humidity, water leakage, smoke/fire indicators, electrical monitoring, structural vibration/cracks, air quality, sound and environmental change. Only record modalities that are actually available and tested.

## World-state and change intelligence

Maintain versioned zone-level state. Compare new evidence with prior verified baselines, identify sensor drift and missing readings, and distinguish:
- new observation;
- verified change;
- suspected deterioration;
- prediction;
- unverified anomaly.

Every change claim must cite the prior and current evidence. A prediction must include its basis, horizon, uncertainty and validation status.

## Safety rules

- AI recommendations supplement, never replace, certified smoke/fire/CO alarms, electrical protection, building inspections or emergency services.
- HOLD when sensor health, calibration, evidence freshness or hazard severity is unknown.
- BLOCK any proposal that would disable or interfere with certified safety devices or building systems.
- Do not automatically operate locks, mains electricity, gas, heaters, appliances or emergency controls.
- Escalate urgent hazards to the user with clear uncertainty and appropriate emergency guidance; do not claim a sensor is a certified alarm.

## Evaluation gates

1. Validate shared schemas and units/ranges for each supported sensor.
2. Test missing, stale, drifting, noisy and disconnected sensors.
3. Test baseline/change comparisons and false deterioration alerts.
4. Test hazard escalation, unknown states and fail-closed behavior.
5. Measure false alarms, missed detections and detection delay only against a documented ground-truth dataset or controlled test protocol.
6. Verify privacy minimisation and local data handling.
7. Keep simulated sensor data separate from physical device trials.

## Required report

Record sensor model/firmware, calibration status, test conditions, ground truth, repetitions, detection delay, false alarms, missed events, failure logs, privacy handling and reviewer. If no validated sensor or ground truth is available, report performance as NOT MEASURED.

## Implementation boundary

This document is an adoption plan. No completed robot, real sensor integration, certified alarm function or real-world safety performance is established by adding this file.
