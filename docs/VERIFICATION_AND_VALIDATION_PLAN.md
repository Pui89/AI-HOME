# PUI89 AI Home Assistant Robot — Verification and Validation Plan

**Status:** Planned test strategy; no test execution or product validation is claimed by this document.

## 1. Purpose

Define how each requirement will be tested, what counts as a pass, and how failures are recorded. Keep software tests, simulation, bench tests and real-world validation separate.

## 2. Test stages

| Stage | Test environment | What it can establish | What it cannot establish |
|---|---|---|---|
| T0 — Static review | Source, schemas, documentation | Contract consistency, permissions, traceability and obvious design gaps. | Runtime behaviour or physical safety. |
| T1 — Software tests | Dependency-free unit/contract tests and synthetic inputs | Deterministic software behaviour for tested cases. | Sensor accuracy or real-world performance. |
| T2 — Simulation | Controlled synthetic home layouts and sensor streams | Behaviour under defined simulated scenarios. | Physical robot safety or real sensor accuracy. |
| T3 — Bench tests | Identified sensors and hardware in a controlled setup | Sensor behaviour under recorded bench conditions. | General household performance or certification. |
| T4 — Supervised environment tests | Approved, controlled test space with independent safety controls | Performance in the exact documented environment and conditions. | Universal reliability, certification or unattended safety. |

A later stage does not replace earlier tests. Never run physical tests until the relevant safety gate is approved.

## 3. Minimum verification matrix

| Test ID | Scenario | Expected result | Evidence to retain |
|---|---|---|---|
| HOME-T-001 | Missing required observation field | Reject or quarantine input; do not create a safe state. | Input, validation result and test log. |
| HOME-T-002 | Stale timestamp | Mark stale/unknown and explain why. | Timestamp and report output. |
| HOME-T-003 | Sensor disconnected | Mark sensor unavailable; preserve last-known value as stale, not current. | Disconnect event and state transition. |
| HOME-T-004 | Noisy or implausible reading | Flag quality/range issue; do not silently smooth into certainty. | Raw input and quality result. |
| HOME-T-005 | Conflicting sensors | Show conflict and uncertainty; require review. | Both source records and report. |
| HOME-T-006 | Calibration expired or unknown | Mark calibration state; restrict claims according to policy. | Calibration metadata and decision. |
| HOME-T-007 | Malformed or oversized image/input | Reject safely within defined resource limits. | Test input metadata and rejection log. |
| HOME-T-008 | Model timeout or malformed output | Reject output; create FailureReport. | Model/version, timeout and failure record. |
| HOME-T-009 | Prompt injection in text/image metadata | Treat content as data; do not change policy or permissions. | Adversarial test case and output. |
| HOME-T-010 | Network unavailable | Preserve defined local behaviour; report unavailable services. | Network condition and event log. |
| HOME-T-011 | Unauthorised request for protected action | Deny and record; no physical command is sent. | Request, policy decision and audit event. |
| HOME-T-012 | Localisation/obstacle uncertainty (future mobility) | Hold/stop; do not continue motion based on uncertain state. | Simulation/bench trace; later physical test record. |
| HOME-T-013 | Drop-off/stair edge (future mobility) | Stop before the defined safety boundary. | Geometry, speed, stopping trace and repetitions. |
| HOME-T-014 | Low battery, over-temperature or charging fault | Enter documented safe state and report fault. | Battery/BMS telemetry and test conditions. |
| HOME-T-015 | Emergency-stop activation (future mobility) | Independent stop response; reset requires deliberate safe procedure. | Physical inspection, response trace and reviewer. |
| HOME-T-016 | Data retention/deletion request | Delete or anonymise data according to approved policy, including defined derivatives/backups. | Before/after record without exposing personal data. |

## 4. Pass/fail rules

- Define numeric thresholds before a test, based on the selected sensor, hazard analysis and applicable standards; do not invent thresholds after seeing results.
- A test passes only if the expected result is observed for all required repetitions and no unresolved critical failure remains.
- Record failures and retests; never overwrite a failed result with a later pass.
- A synthetic test must be labelled **SIMULATED**. A bench result must be labelled **BENCH**. Do not combine them into a real-world accuracy claim.
- For detection functions, report the ground-truth method, dataset provenance, sample counts, false positives, false negatives, detection delay, calibration and limitations. If unavailable, report **NOT MEASURED**.

## 5. Test record template

For each test, record:

- Test ID, requirement IDs, date/time and reviewer.
- Git commit, software version, model/checkpoint revision and dependency inventory.
- Sensor make/model/firmware, calibration and installation details, if applicable.
- Environment, setup, ground truth, input sample and number of repetitions.
- Expected result, actual result, pass/fail, logs and evidence links.
- Failure mode, severity, corrective action, retest reference and remaining limitation.

## 6. Release gates

- **Software baseline:** T0/T1 tests reviewed; no unresolved critical defects.
- **Simulation baseline:** T2 scenario set and limitations published.
- **Sensor bench baseline:** exact sensor and calibration evidence available; no claims beyond test conditions.
- **Physical prototype baseline:** approved hazard analysis, independent emergency stop, controlled environment, trained supervision and documented T3/T4 results.
- **Public/product claims:** claims must match evidence and applicable independent approvals. Software tests do not establish product safety or certification.
