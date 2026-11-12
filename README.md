# PUI89 AI Home Assistant Robot


## Public privacy boundary

This public README is limited to the project overview, approved concept material and evidence that can be shared openly. Do not publish API keys, passwords, private tokens, Wi-Fi or internal network settings, private camera footage, personal or precise location data, detailed security configurations, unreleased engineering specifications, or confidential commercial plans. Keep sensitive material in an appropriately access-controlled private location. If a credential may have been exposed, revoke it; removing it from the latest commit does not remove it from Git history.

## Open-source-first engineering

PUI89 prioritises open-source software, transparent licensing, reproducible workflows and evidence-led collaboration. Model weights, datasets, hosted services and hardware are assessed separately for provenance, licence terms, security, data handling, resource requirements and intended use. Public availability alone does not establish permission for reuse or commercial deployment.


> **PUI89 engineering standard:** [Simple, Safe and Professional](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_SIMPLE_SAFE_PROFESSIONAL_STANDARD.md) — shared guidance for usability, safety, evidence, privacy and maintainable engineering.

> **PUI89 | Intelligent Systems. Verifiable Decisions. Safer Outcomes.**
> 
> **Project:** PUI89 AI Home Assistant Robot  
> **Focus:** Indoor home-assistant robot concept and home-safety software platform  
> **Development stage:** Early software foundation and product requirements; no completed robot or real sensor integration is established.
> 
> **Project website:** [English](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html) · [PUI89 portfolio](https://pui89.github.io/)
> 
> **Validation boundary:** AI recommendations do not replace certified smoke, fire, carbon-monoxide or electrical protection; no physical safety function is claimed.

## Project overview

**PUI89 AI Home Assistant Robot** is an indoor, four-wheel assistant concept for home-condition awareness and everyday support. The project is software-first and evidence-led.

- **Stage:** early software foundation and product requirements; no completed robot or real sensor integration is established.
- **Purpose:** help residents notice changes, understand evidence and decide when human attention is needed.
- **Websites:** [English](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html) · [PUI89 portfolio](https://pui89.github.io/)
- **Repository:** [Pui89/AI-Home-Safety-Robot](https://github.com/Pui89/AI-Home-Safety-Robot)
- **Related product:** [PUI89 AI NOMAD](https://github.com/Pui89/AI-Mobile-Assistant-Robot) is a separate indoor/outdoor and travel platform.

![PUI89 AI Home Assistant Robot concept](https://pui89.github.io/images/homeguard-ai-home-concept.svg)

## Compact physical design target — AI HOME

The current proposed compact form factor is:

| Parameter | Design target |
|---|---:|
| Width (W) | **25 cm** |
| Length / depth (D) | **25 cm** |
| Height (H) | **40 cm** |
| Maximum total mass | **8 kg**, including the battery |

These are **provisional design targets**, not measured prototype specifications. The dimensions describe the intended external envelope of the assembled unit, including its wheels and fixed sensor housing. The 8 kg limit includes the battery, chassis, wheels, motors, electronics, sensors, wiring and enclosure.

**Design intent:** a compact, stable, four-wheel indoor assistant that can fit into a small home while carrying its sensing and computing equipment. Keep heavier components low in the chassis, protect wheels and moving parts, provide adequate ventilation and service access, and avoid sharp external edges. HOME remains an indoor home-condition awareness product; AI NOMAD is the separate portable travel/outdoor assistant.

**Engineering checks required before freezing the design:** verify the complete mass budget against selected components; centre of gravity and tip resistance; wheel clearance and floor transitions; obstacle and collision behaviour; cable snagging; thermal management and ventilation; battery containment and charging safety; acoustic performance; cleaning and maintenance access; and safe supervised stopping. The 25 × 25 × 40 cm envelope and 8 kg limit must be checked against the actual sensor layout and enclosure.

**Capability boundary:** this target does not imply stair climbing, operation on rough terrain, water resistance, fire resistance, an IP rating, certified alarm capability, or validated safety performance. Certified household protection devices remain primary. No prototype dimensions, measured mass or physical validation are currently established by this design target.

## What it is designed to monitor

Research areas include water leaks and moisture; temperature, humidity and heat; smoke/fire-related signals from appropriate certified devices; non-invasive electrical indicators; visible surface or vibration changes; and environmental changes such as sound and light.

These are monitoring and evidence-research areas—not validated detection, diagnosis or prevention capabilities.

## Shared AI Core

The project is designed to use versioned `WorldState`, `Observation`, `ActionProposal` and `FailureReport` contracts, with evidence provenance, timestamps, sensor-health checks, uncertainty handling, safety gates and human-reviewed recommendations.

## Safety and privacy

- Certified smoke, fire, carbon-monoxide and electrical protection devices remain primary.
- Never delay evacuation or emergency procedures for AI analysis.
- Do not control locks, breakers, valves, appliances or certified alarms.
- Do not claim structural, fire, electrical or mould diagnosis without suitable independent validation.
- Stop when localization, obstacle evidence or battery state is uncertain; minimise personal data.

## Development approach

Requirements and hazard analysis → software contracts and synthetic tests → evidence reports → simulation → reviewed sensor integration. No physical safety performance, real-world sensor accuracy or certified function is currently claimed.

## Engineering foundation — Phase 2

The following documents define the proposed engineering baseline. They are requirements and test plans, **not evidence that a robot or safety function has been built or validated**.

- [Product requirements](docs/PRODUCT_REQUIREMENTS.md) — scope, users, measurable requirements and design targets.
- [System architecture](docs/SYSTEM_ARCHITECTURE.md) — evidence flow, shared AI Core contracts and human-review boundary.
- [Safety and cybersecurity requirements](docs/SAFETY_AND_CYBERSECURITY_REQUIREMENTS.md) — safety gates, privacy and security controls.
- [Verification and validation plan](docs/VERIFICATION_AND_VALIDATION_PLAN.md) — software, simulation, bench and supervised test stages.
- [Hardware specification](docs/HARDWARE_SPECIFICATION.md) — component selection criteria and TBD engineering values; research only, no purchasing.
- [Preliminary internal layout and 8 kg mass budget](docs/AI_HOME_INTERNAL_LAYOUT_AND_MASS_BUDGET.md) — packaging zones, category-level BOM and engineering gates; planning allocations only, not measured weights or selected parts.

## Development stage

**Current stage:** Early software foundation & requirements  
**ขั้นการพัฒนา:** พื้นฐานซอฟต์แวร์และข้อกำหนดระยะแรก

**Evidence:** Product requirements, architecture, software contracts and early adapter/test foundations are documented.

**Limitations:** No built robot, real sensor integration, certified alarm, or validated home-safety performance is established.

**Next milestone:** Complete a software-only home-safety demonstrator using mock sensor inputs and explicit failure states.


## Website QR codes

| English | ภาษาไทย |
|---|---|
| [![English QR](https://pui89.github.io/qr/home-en.png)](https://pui89.github.io/home.html) | [![Thai QR](https://pui89.github.io/qr/home-th.png)](https://pui89.github.io/home-th.html) |
| [Open English page](https://pui89.github.io/home.html) | [เปิดเว็บไซต์ภาษาไทย](https://pui89.github.io/home-th.html) |

## Hugging Face vision models — opt-in local integration

This repository now includes real Hugging Face checkpoint adapters in [`pui89_models/hf_vision.py`](pui89_models/hf_vision.py), with project-specific usage boundaries in [`docs/HUGGING_FACE_MODEL_INTEGRATION.md`](docs/HUGGING_FACE_MODEL_INTEGRATION.md).

- **OWLv2:** `google/owlv2-base-patch16-ensemble` for text-conditioned object proposals.
- **Intel DPT-Hybrid:** `Intel/dpt-hybrid-midas` for relative scene depth where appropriate; not calibrated distance or physical depth.
- **local-first default:** no packages or model weights are installed/downloaded automatically; CPU-only inference, local cache only by default, no hosted inference API or cloud GPU.
- **Evidence status:** adapter code is added; model inference and project-specific accuracy are NOT YET TESTED. Outputs remain uncertain observations for human review, never actuator commands.

## Licence — Apache-2.0 for selected source code only

The Apache License, Version 2.0 applies **only** to the two source-code files listed in [`LICENSE-SCOPE.md`](LICENSE-SCOPE.md) and marked `SPDX-License-Identifier: Apache-2.0`:

- `pui89_models/hf_vision.py`
- `tests/test_hf_vision_adapter.py`

**Not licensed under Apache-2.0:** the PUI89 name, logos, trademarks, brand identity, AI Home Assistant Robot product identity, robot appearance and industrial/product designs, CAD or mechanical drawings, concept images/artwork, website, this README, other documentation, repository configuration, and all unlisted files. Those materials remain reserved to their respective rights holders, to the extent those rights exist and are owned or controlled by them. Third-party assets and models remain under their own terms.

See [`LICENSE`](LICENSE), [`LICENSE-SCOPE.md`](LICENSE-SCOPE.md) and [`NOTICE`](NOTICE). Apache-2.0 does not grant permission to use PUI89 trademarks or imply PUI89 endorsement.




---

## Security, malware and supply-chain protection

Security policy: [SECURITY.md](SECURITY.md). Report suspected vulnerabilities privately; do not post resident data, camera footage, access details or exploit steps publicly.

Project-specific controls and review requirements:
- Treat sensor readings, camera/audio inputs, network messages, configuration files and imported logs as untrusted.
- Validate source, timestamps, ranges, file sizes and stale/conflicting readings; fail safely when evidence is unreliable.
- Never commit credentials, resident information, floor plans, private recordings or network secrets.
- Review dependencies, model files and GitHub Actions for provenance, licences and vulnerabilities before adoption.
- AI recommendations must not automatically operate locks, breakers, valves, appliances or emergency systems; retain human authority.
- Use least-privilege CI and never expose secrets to untrusted pull-request code.

A scan or passing test is evidence only for the checks actually run; it does not establish whether the repository contains malware or vulnerabilities.

## Shared PUI89 standards

Project-wide guidance is maintained centrally to avoid repeating the same framework in every repository:

- [Simple, Safe and Professional Engineering Standard](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_SIMPLE_SAFE_PROFESSIONAL_STANDARD.md)
- [Project strength scorecard method](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PROJECT_STRENGTH_SCORECARD.md)
- [Security policy](SECURITY.md)



## Spatial Intelligence integration

See [the project-specific spatial integration profile](docs/spatial-intelligence/README.md). Runtime sensor integration and physical validation remain pending.

<!-- PUI89_EVIDENCE_BACKED_REVIEW:START -->
## Evidence-backed project review status

**Project:** PUI89 AI HOME  
**Completed evidence-backed reviews: 0** — no qualifying completed review is currently recorded in the shared PUI89 review register.

This is a review-record count, not a statement that development or testing has not occurred. Engineering work, CI runs, test results and simulation evidence may support a review, but do not automatically count as a completed review.

A review is counted only when its record includes all required fields: **completed status, review date, defined scope, reviewer role, outcome, and at least one supporting evidence reference**. Drafts, ratings, stars, page views and comments are excluded.

The portfolio-wide count is published on the [PUI89 website](https://pui89.github.io/#evidence-backed-project-reviews). Counts change only when a qualifying record is added to the shared register.

**สถานะการทบทวนโครงการที่มีหลักฐาน**  
**จำนวนการทบทวนที่เสร็จสมบูรณ์: 0** — ยังไม่มีบันทึกการทบทวนที่ผ่านเกณฑ์สำหรับโครงการนี้ในทะเบียนกลาง PUI89

ตัวเลขนี้เป็นจำนวนบันทึกการทบทวน ไม่ได้หมายความว่าไม่มีการพัฒนาหรือทดสอบ งานวิศวกรรม ผล CI การทดสอบ และหลักฐานจากการจำลองอาจใช้ประกอบการทบทวน แต่ไม่นับเป็นการทบทวนที่เสร็จสมบูรณ์โดยอัตโนมัติ

จะนับเมื่อมีสถานะเสร็จสมบูรณ์ วันที่ ขอบเขต บทบาทผู้ทบทวน ผลการทบทวน และหลักฐานอ้างอิงอย่างน้อยหนึ่งรายการครบถ้วนเท่านั้น รายการร่าง คะแนน ดาว ยอดเข้าชม และความคิดเห็นจะไม่นับ
<!-- PUI89_EVIDENCE_BACKED_REVIEW:END -->

