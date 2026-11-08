# PUI89 Shared AI Core — AI HOME Adapter

**Status:** Integration plan; documentation only.  
**Platform contract:** [PUI89 Evidence-to-Action Intelligence Platform](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_EVIDENCE_TO_ACTION_PLATFORM.md)

## Purpose

Use shared evidence, world-state, change tracking, uncertainty and safety proposal contracts for the AI HOME software platform and future HOME/NOMAD devices. This guide does not claim a completed robot or certified safety function.

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
