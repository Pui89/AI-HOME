# PUI89 AI HOME — Security and Safety Threat Model

**Status:** initial design baseline; not a certification or completed security assessment.

## Assets to protect
- Resident privacy, occupancy patterns, images, audio and household routines.
- Sensor observations, timestamps, calibration records and evidence provenance.
- Robot navigation state, action proposals, configuration and update integrity.
- Repository credentials, GitHub tokens, workflow permissions and software supply chain.
- Availability of the home's independent certified safety devices.

## Trust boundaries
1. Physical sensors and their firmware.
2. Local AI/model runtime and cached model files.
3. Home network, router and connected devices.
4. GitHub repository, pull requests, workflows and external dependencies.
5. Human operator reviewing observations and proposals.
6. Robot motion and any future actuator interface.

Treat data crossing every boundary as untrusted until validated. Do not assume sensor readings, model labels, prompts or network messages are authentic.

## Threats and required mitigations

| Threat | Required baseline |
|---|---|
| Private camera/audio or occupancy data exposed | Data minimization; no resident samples in Git; local-first processing; explicit consent and retention rules before capture features |
| Spoofed, stale, disconnected or miscalibrated sensors | Record source, timestamp, freshness, calibration and health; represent missing/conflicting evidence explicitly |
| False positive or missed hazard | Never replace certified alarms; human review; uncertainty reporting; corroboration where appropriate |
| Prompt injection or malicious image/text content | Treat model and user content as data, never executable instructions; constrain tools and outputs |
| Model hallucination or distribution shift | Model outputs remain proposals; test on representative labelled data; no safety claims without independent validation |
| Unauthorized robot movement | No physical actuation from model output; supervised movement only after separate hazard analysis; emergency stop and safe-stop design required before tests |
| Malicious dependency, model or GitHub Action | Verify publisher, exact revision, licence, provenance and integrity; minimize dependencies; review updates |
| Leaked token or secret | Never commit secrets; least-privilege tokens; rotate exposed credentials; do not pass secrets to untrusted pull requests |
| Workflow supply-chain compromise | Read-only GITHUB_TOKEN; review and pin third-party actions before production use; no write permissions in test jobs |
| Denial of service or resource exhaustion | Bound image sizes, input counts, runtime and memory; timeouts; fail safely without disabling certified devices |

## Non-negotiable safety boundaries
- AI HOME must not control locks, breakers, valves, cooking appliances, certified alarms or emergency systems.
- Never delay evacuation, emergency calls or established safety procedures for AI analysis.
- No structural, electrical, fire, smoke or mold diagnosis is claimed by this repository.
- A model score is not a probability of safety unless calibrated and validated for the exact task.
- Uncertain, contradictory, stale or missing evidence must not become a confident safe status.
- Physical robot tests require separate hazard analysis, a supervised test plan and an independent emergency stop.

## Release gates
Before any real sensor or robot deployment, document: threat review, data-flow diagram, privacy impact, dependency and model inventory, exact licences, vulnerability review, test evidence, failure handling, human override, recovery plan and independent safety review.

This file is a starting threat model. It does not establish that any control has been implemented or validated.

## Home-environment hazard validation gates

**Status:** requirements for future design and evaluation. Unless an implementation path and test evidence are linked, each control is **NOT VERIFIED**. These gates do not establish a working sensor, certified alarm, building diagnosis or protective function.

### 1. Independent life-safety protection

- Certified smoke, carbon-monoxide and other locally required alarms, fire protection, residual-current/circuit protection and emergency procedures remain independent primary safeguards.
- AI HOME must not silence, reset, delay, replace, reinterpret or control certified alarms or protective electrical devices.
- If a certified alarm activates, residents must follow its instructions and established evacuation/emergency procedures immediately; never wait for AI analysis or a phone notification.
- Clearly distinguish an independent alarm event, a third-party sensor reading, an AI-generated anomaly prompt and an unverified user report.

### 2. Sensor identity, health and evidence quality

For each installed sensor, document its exact model, measured physical quantity, units, range, accuracy/limitations, location, installation date, calibration/self-test method, maintenance interval, firmware and data source.

- Check freshness, timestamp/timezone, plausible range, stuck values, missing samples, drift, communication loss, battery/power state and tamper indications.
- Use suitable reference checks and qualified installation/calibration procedures; do not invent calibration values or infer a sensor's health from a plausible-looking reading.
- Mark failed, stale, out-of-range, uncalibrated or disconnected readings INVALID/UNKNOWN. Do not turn sensor silence into an all-clear.
- Keep raw readings and AI interpretation separate; record transformations, configuration/software version and evidence references.
- A sensor alert is an indication requiring appropriate verification, not proof of a hazard or its cause.

### 3. Water, leakage and moisture

- Define what each sensor detects (for example, contact water, relative humidity or a measured moisture property); do not conflate humidity with a leak or flood.
- Test placement, detection delay, false alarms, missed wetting, condensation, cleaning fluids, sensor fouling, cable/connectivity failure and battery failure under controlled conditions.
- Document water exposure limits for the exact sensor, enclosure, connectors and power system. No IP rating, waterproof, water-resistant or safe-in-flood claim without applicable system-level test evidence.
- Keep electrical equipment isolated from wet areas according to qualified design; AI HOME must never operate valves, pumps or breakers as an automatic response.
- Report the affected zone and uncertainty without claiming the source, extent or structural consequence of water.

### 4. Fire, smoke, heat and electrical anomalies

- Treat temperature, optical smoke-like signals, sound and power telemetry as distinct measurements with known limits and interference conditions.
- Do not claim fire or smoke detection from an unvalidated camera/model or temperature anomaly; no AI output may delay a certified alarm or emergency action.
- Do not connect to, switch, reset, open or diagnose mains wiring, outlets, breakers, batteries or appliances. No autonomous electrical intervention.
- Any future powered hardware requires qualified electrical design, isolation, overcurrent protection, thermal design, enclosure selection and documented fault testing.
- Define safe shutdown and isolation procedures for overheating, smoke, damaged wiring, liquid ingress, abnormal battery temperature, swelling, odour or power instability. Residents should not handle damaged or wet electrical/battery equipment; use qualified responders.
- Fire resistance, flame retardancy, thermal-runaway protection and safe charging are NOT VERIFIED until the exact assembly has appropriate independent tests.

### 5. Cracks, vibration and structural change

- Distinguish a visual change observation from a structural diagnosis. A camera image, phone accelerometer or low-cost vibration sensor cannot certify building safety.
- Record sensor mounting, orientation, sampling rate, units, baseline period, environmental influences, uncertainty and any image alignment/lighting limitations.
- Test repeatability, mounting movement, temperature effects, normal building vibration and false change alerts using controlled, non-destructive methods.
- Escalate potentially significant changes to a qualified building professional; do not recommend occupancy, evacuation or structural repair decisions solely from AI output.
- Never drill, attach to structural elements or conduct load/impact tests without owner permission and qualified assessment.

### 6. Humidity, condensation and mold-risk indicators

- Keep measured relative humidity, temperature, visible staining and model-generated mold-risk estimates as separate evidence.
- Record sensor placement, calibration, condensation exposure, ventilation effects, room use and missing periods.
- Do not identify mold species, toxicity, hidden growth or health risk from ordinary RGB imagery or humidity alone.
- Recommend inspection by an appropriately qualified professional when persistent moisture or suspected growth is reported; do not prescribe chemical treatment or remediation from an AI score.

### 7. Privacy, audio and indoor observation

- Default to minimum necessary sensing; avoid continuous recording, face recognition, biometric inference, conversation transcription and occupancy profiling.
- Provide clear resident control, consent/authority, visible sensor status, purpose limitation, access roles, retention/deletion and export controls before any camera or microphone feature is enabled.
- Keep resident images, audio, floor plans, occupancy patterns, network details and access credentials out of public repositories, issues, test fixtures and routine logs.
- Synthetic fixtures must not contain real resident or household data.

### 8. Safe software behavior and escalation

- Use explicit states such as NORMAL_WITHIN_SENSOR_LIMITS, ALERT_REQUIRES_CHECK, UNKNOWN, SENSOR_FAULT and SYSTEM_UNAVAILABLE. Never display a global SAFE status when required sensors are missing, stale or unverified.
- Show the measurement, source, timestamp, sensor health, uncertainty and reason for the alert; avoid unsupported causal claims.
- AI recommendations remain advisory. No autonomous operation of locks, doors, windows, breakers, valves, appliances, heaters, cookers, alarms or emergency systems.
- On model failure, corrupted data, clock mismatch, communications loss, power failure or conflicting readings, preserve available evidence, show the limitation and defer to independent safety devices and human procedures.
- Test notification delivery, duplicate alerts, delayed alerts, quiet modes, offline operation, restart and recovery. Do not promise emergency notification unless end-to-end delivery is independently tested.

### 9. Minimum evidence record before any pilot

For each sensor and hazard scenario, retain the exact hardware/software revision, intended location/use, test method, reference instrument and calibration, environmental conditions, sample count, detection and missed-event results, false alarms, latency where measured, failure/recovery behavior, limitations, reviewer and date. Include NOT RUN and NOT TESTED cases.

**Stop condition:** if a life-safety device, sensor identity/health, required evidence, privacy authority or communication path is uncertain, AI HOME must not issue a reassuring all-clear or take physical action. Residents must rely on certified protection and established emergency procedures.

