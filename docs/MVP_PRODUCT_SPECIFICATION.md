# AI HOME MVP Product Specification

**Status:** Proposed software demonstrator baseline  
**Product:** PUI89 AI HOME — indoor home-condition awareness assistant  
**Evidence boundary:** This document defines a scoped MVP. It does not establish a completed robot, real sensor integration, detection accuracy, certification or physical safety performance.

## 1. MVP objective

Deliver a small, understandable local-first demonstrator that receives environmental readings (initially simulated), evaluates configurable thresholds, exposes sensor health and records timestamped evidence for human review.

The first milestone is software-only. Hardware selection, purchasing, installation and physical integration are separate approval gates.

## 2. Target user and primary task

A resident or evaluator should be able to:
- view the latest temperature and relative-humidity values;
- understand whether each input is normal, warning, unavailable, stale or invalid;
- adjust demonstration thresholds;
- trigger predefined simulated scenarios;
- inspect a timestamped event/evidence log.

## 3. MVP scope

### Included
- Temperature and relative-humidity display.
- Configurable high/low thresholds with input validation.
- Explicit sensor states: connected, disconnected, stale and invalid.
- Rule-based status evaluation with uncertainty-aware fail-safe handling.
- Timestamped in-memory event log.
- Simulated scenarios for normal, high temperature, high humidity, stale, disconnected and invalid input.
- Local browser execution with no backend, account, network call, hosted API or external dependency.
- Clear labels distinguishing simulated data from real measurements.

### Excluded
- Physical robot movement or autonomous navigation.
- Real sensor drivers or hardware control.
- Smoke, fire, carbon-monoxide, electrical, mould or structural diagnosis.
- Emergency dispatch or replacement of certified household protection.
- Camera, microphone, resident identification, cloud storage or remote monitoring.
- AI/ML inference in the first demonstrator. Rules are more transparent and testable for this narrow MVP.

## 4. User-visible requirements

| ID | Requirement | Acceptance evidence |
|---|---|---|
| HOME-MVP-01 | Show temperature and humidity values with units | Browser demo displays both values |
| HOME-MVP-02 | Show data provenance as simulated | Persistent visible demo label |
| HOME-MVP-03 | Allow threshold configuration | User can change values; invalid ranges are rejected |
| HOME-MVP-04 | Evaluate readings deterministically | Scenario changes produce documented states |
| HOME-MVP-05 | Distinguish disconnected, stale and invalid inputs | Each fault scenario is visible and logged |
| HOME-MVP-06 | Record timestamps for state changes | Event log contains local timestamps |
| HOME-MVP-07 | Keep data local to the browser session | No network requests or remote service |
| HOME-MVP-08 | Avoid hazardous actuation | No actuator controls or output commands exist |

## 5. Decision rules

- A valid, connected, fresh reading inside configured thresholds is **Normal**.
- A valid reading outside a configured threshold is **Warning**; it is an informational threshold event, not a diagnosis.
- Disconnected, stale or invalid input is **Unavailable / Needs attention**. Do not infer that the environment is safe.
- Missing or uncertain evidence must never be converted into a normal state.
- Thresholds are user-configurable demonstration settings, not medical, fire, electrical or building-safety limits.

## 6. Safety and human authority

Certified smoke, fire, carbon-monoxide and electrical protection devices remain primary. The demonstrator must never advise delaying evacuation or emergency procedures. It must not control locks, breakers, valves, appliances, certified alarms or other safety-critical equipment. Human users retain decision authority.

## 7. Privacy and data handling

The MVP uses synthetic values only. The browser demo must not request personal data, access sensors, use a camera or microphone, transmit readings, or persist resident data. The event log is session-only and is cleared when the page is reloaded.

## 8. Resource and supply-chain constraints

Use browser-native HTML, CSS and JavaScript only. No package manager, model download, automatic installation, external font, analytics, CDN, paid API, hosted inference or cloud GPU. Any future dependency or hardware proposal requires a separate provenance, licence, security, resource and approval review.

## 9. Release gates

1. Software-only demonstrator and deterministic tests reviewed.
2. Sensor interface and candidate component assessed; no purchase implied.
3. Bench integration plan reviewed before any hardware is connected.
4. Real sensor readings validated against a suitable reference instrument.
5. Safety, privacy, reliability and usability review before public capability claims.

Passing a software demo gate does not pass a physical or product-safety gate.
