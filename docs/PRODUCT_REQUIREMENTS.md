# PUI89 AI Home Assistant Robot — Product Requirements

**Document status:** Proposed requirements baseline  
**Project stage:** Software foundation and concept; requirements are not proof of implementation.  
**Owner:** PUI89  
**Review rule:** Every requirement remains **PROPOSED / NOT VERIFIED** until linked to implementation and repeatable evidence.

## 1. Product purpose

An indoor, four-wheel assistant concept that helps residents notice relevant changes in the home, understand the available evidence and decide when human attention is needed. It is not a certified alarm, emergency service, medical device, building inspector or autonomous home-protection system.

## 2. Users and operating context

- Primary user: a resident or authorised household operator.
- Environment: indoor residential floors and corridors; exact floor types, thresholds, lighting, clutter and connectivity limits must be established through testing.
- Operation: supervised and low speed if mobility is developed.
- Privacy: local-first where feasible, collect the minimum data needed, and provide clear control over capture, access, retention and deletion.

## 3. Scope

**In scope for research:** water/moisture indicators, temperature and humidity, environmental change, permitted non-invasive electrical indicators, visual obstacle/context proposals, evidence reporting and human-reviewed recommendations.

**Out of scope:** replacing certified smoke/fire/CO/electrical protection; diagnosing mould, structural damage, electrical faults or fire cause; operating locks, breakers, valves, appliances or emergency systems; unsupervised navigation; autonomous intervention.

Only modalities supported by an identified, lawful, tested sensor or dataset may be presented as available.

## 4. Product requirements

| ID | Requirement | Acceptance evidence | Status |
|---|---|---|---|
| HOME-REQ-001 | Every observation records source/sensor ID, timestamp, units, zone, quality and provenance. | Schema tests reject missing or malformed required fields. | PROPOSED |
| HOME-REQ-002 | Stale, missing, noisy, conflicting or unhealthy inputs remain explicitly uncertain. | Synthetic fault tests prove the system does not label them safe. | PROPOSED |
| HOME-REQ-003 | Reports distinguish measured observation, inference, prediction and recommendation. | Report tests verify each claim links to its evidence and uncertainty. | PROPOSED |
| HOME-REQ-004 | Recommendations require human review; no model output directly controls an actuator. | Interface and API tests show no direct model-to-actuator path. | PROPOSED |
| HOME-REQ-005 | Loss of localisation, obstacle confidence, communications or safe battery state results in a defined safe stop/hold. | Simulation and supervised bench tests with recorded outcomes. | PROPOSED |
| HOME-REQ-006 | Certified life-safety devices operate independently of AI HOME. | Architecture review and physical integration inspection; no alarm disable/control path. | PROPOSED |
| HOME-REQ-007 | Personal data is minimised and access, retention and deletion are documented before capture. | Data-flow review and privacy test record. | PROPOSED |
| HOME-REQ-008 | Software, models and dependencies are traceable to exact versions and licences. | Reproducible inventory with provenance and licence review. | PROPOSED |
| HOME-REQ-009 | Each supported sensing function has a documented validation method and known limitations. | Test plan, ground truth, calibration record and results. | PROPOSED |
| HOME-REQ-010 | The product can report failures and recover without silently discarding evidence. | Failure injection and recovery tests. | PROPOSED |

## 5. Physical design targets

- Mobility concept: four wheels, indoor use, supervised movement.
- Complete robot mass: **4–6 kg target**, including battery and all installed parts; **10 kg is the maximum design ceiling**, not the target build mass.
- External dimensions: **25–28 cm W × 30–33 cm D × 30–35 cm H** as a provisional complete assembled envelope including wheels and fixed sensor housing; not measured.
- Initial payload target: **1–2 kg**, separate from robot mass and subject to stability, drive and stopping validation.
- Centre of gravity, turning radius, speed, stopping distance, threshold-crossing ability, floor loading, runtime and charging time: **TBD**. Do not publish invented values.
- Use the [preliminary internal layout and mass-budget plan](AI_HOME_INTERNAL_LAYOUT_AND_MASS_BUDGET.md) for planning only; allocations are not measured component masses or selected hardware.
- Protection against water ingress, heat and fire: define from a documented hazard analysis and verified component/material ratings. Do not describe the robot as waterproof or fireproof without applicable test evidence.


## 6. Human factors

- Show what was observed, when, where, by which sensor and with what quality.
- Explain why a recommendation was generated and what remains unknown.
- Provide a clear way to dismiss, acknowledge or escalate a recommendation.
- Avoid alarming language where evidence is weak; never delay emergency action.

## 7. Requirement change control

Record each change with ID, reason, author, date, affected tests and evidence. A requirement is not complete because it appears in a document. Update its status only after review of the implementation and test record.

## 8. Related documents

- [System architecture](SYSTEM_ARCHITECTURE.md)
- [Safety and cybersecurity requirements](SAFETY_AND_CYBERSECURITY_REQUIREMENTS.md)
- [Verification and validation plan](VERIFICATION_AND_VALIDATION_PLAN.md)
- [Hardware specification and selection criteria](HARDWARE_SPECIFICATION.md)
- [Security threat model](SECURITY_THREAT_MODEL.md)
