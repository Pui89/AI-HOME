# AI HOME Local Dashboard Specification

**Status:** Software-only demonstrator  
**Implementation target:** Static HTML, CSS and JavaScript; no framework or external runtime.

## 1. Information architecture

1. Header with explicit **SIMULATED DATA — NOT CONNECTED TO SENSORS** label.
2. Two primary metric cards: temperature and relative humidity.
3. Overall state summary: normal, warning or unavailable.
4. Scenario selector for deterministic demonstration.
5. Threshold controls with validation and reset-to-demo defaults.
6. Sensor health panel showing each channel state.
7. Timestamped evidence/event log.

## 2. Interaction requirements

- Selecting a scenario updates synthetic readings and records the transition.
- Scenarios: normal, high temperature, high humidity, stale, disconnected and invalid.
- Threshold edits immediately re-evaluate the current valid synthetic sample.
- Invalid threshold inputs are rejected with a clear message.
- The user can clear the session log.
- No background polling, browser sensor access, network requests or hidden persistence.

## 3. Status semantics

- **Normal:** valid simulated readings are within configured thresholds.
- **Warning:** at least one valid simulated reading crosses a configured threshold.
- **Unavailable:** one or more required channels are stale, disconnected or invalid. Missing evidence takes precedence over a reassuring overall status.
- Status text must explain the cause. Colour is supplementary and never the only indicator.

## 4. Accessibility and usability

Use semantic headings, explicit labels, keyboard-operable native controls, visible focus, sufficient contrast, and programmatically exposed status messages. Avoid flashing or rapidly moving content. The implementation should be reviewed against applicable WCAG 2.2 guidance; this specification does not claim conformance.

Reference: [W3C Understanding Success Criterion 4.1.3 — Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html).

## 5. Privacy and security

The demo is fully local and uses synthetic inputs. No external scripts, fonts, analytics, network calls, personal data, camera or microphone. Do not add browser storage without a separate privacy review. Treat future imported sensor data as untrusted input.

## 6. Acceptance checks

- Page opens from a local file without installation.
- Simulated-data label remains visible in every scenario.
- Every scenario produces the expected state and a log entry.
- Threshold validation prevents inverted or non-numeric ranges.
- Stale/disconnected/invalid data never appears as normal.
- No network request or persistent browser storage is used.
