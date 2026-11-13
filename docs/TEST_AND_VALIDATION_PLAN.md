# AI HOME Test and Validation Plan

**Status:** Software-only test plan with a browser-based deterministic self-test runner  
**Important:** Test completion is not implied by this plan. Results must be recorded separately with date, environment, version and evidence.

## 1. Test levels

### A. Static review
- Check semantic HTML, labels, keyboard access and status announcements.
- Confirm no external dependencies, network calls, browser sensor permissions or persistent storage.
- Review that all public claims distinguish simulated and physical evidence.

### B. Deterministic scenario tests
| ID | Input scenario | Expected result |
|---|---|---|
| T-01 | Valid readings inside thresholds | Normal |
| T-02 | Temperature above high threshold | Warning |
| T-03 | Temperature below low threshold | Warning |
| T-04 | Humidity above high threshold | Warning |
| T-05 | Humidity below low threshold | Warning |
| T-06 | Stale timestamp | Unavailable; not normal |
| T-07 | Disconnected channel | Unavailable; not normal |
| T-08 | Invalid / non-numeric channel | Unavailable; invalid value rejected |
| T-09 | Threshold minimum >= maximum | Validation error; setting rejected |
| T-10 | Reload page | Synthetic defaults restored; session log cleared |

### C. Fault injection
Simulate missing values, malformed values, delayed timestamps, channel disconnection and conflicting channel health. Verify the UI exposes the failure rather than substituting a safe-looking value.

### D. Future bench validation (not part of this software-only PR)
After a separately approved sensor is selected: compare readings against a traceable reference instrument over a documented range; test warm-up, drift, repeatability, disconnection, power cycling, timestamp integrity and environmental placement. Record uncertainty and calibration conditions.

## 2. Current executable test harness

A dependency-free browser test runner is provided at [`demo/ai-home-dashboard/tests.html`](../demo/ai-home-dashboard/tests.html). It exercises 12 deterministic checks against the same decision core used by the dashboard: normal, high temperature, high humidity, stale, disconnected, invalid, missing sample, reversed thresholds, blank thresholds, out-of-range thresholds, unknown scenario and inclusive boundary values. The test page reports results in the browser. A passing run is evidence only for these software decision-logic cases and must be recorded with the commit, browser and date before claiming the software milestone complete.

## 3. Evidence record template

For every completed test, record:
- test ID and objective;
- date/time and timezone;
- commit or build identifier;
- browser, operating system and test setup;
- input values and provenance (simulated or physical);
- expected and observed result;
- pass/fail/blocked outcome;
- evidence link or retained artifact;
- reviewer role and known limitations.

## 4. Exit criteria for software-only milestone

- All deterministic scenarios behave as specified.
- Fault states never collapse into Normal.
- Threshold validation is deterministic.
- No external network or persistence is required.
- Safety boundary and simulation label remain visible.
- Test evidence is reviewed and linked before claiming the milestone complete.

## 5. Explicit non-claims

This milestone does not validate sensor accuracy, fire/smoke/CO detection, electrical safety, leak detection, structural condition, robot mobility, battery safety, reliability in a home, or regulatory compliance.
