# AI HOME Test and Validation Plan

**Status:** Initial software-only plan  
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

## 2. Evidence record template

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

## 3. Exit criteria for software-only milestone

- All deterministic scenarios behave as specified.
- Fault states never collapse into Normal.
- Threshold validation is deterministic.
- No external network or persistence is required.
- Safety boundary and simulation label remain visible.
- Test evidence is reviewed and linked before claiming the milestone complete.

## 4. Explicit non-claims

This milestone does not validate sensor accuracy, fire/smoke/CO detection, electrical safety, leak detection, structural condition, robot mobility, battery safety, reliability in a home, or regulatory compliance.
