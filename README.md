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
> **Development stage:** Initial Stage 2 indoor-perception decision layer added; no completed robot, live camera input or real sensor integration is established.
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

The revised compact form factor is a **proposed design target**, subject to CAD, component selection and physical validation.

| Parameter | Revised target |
|---|---:|
| Width (W) | **25–28 cm** |
| Length / depth (D) | **30–33 cm** |
| Height (H) | **30–35 cm** |
| Complete robot mass | **4–6 kg target**, including battery |
| Maximum design allowance | **10 kg ceiling**, not a desired build weight |
| Initial payload target | **1–2 kg**, subject to stability and drive testing |
| Mobility | Four wheels; indoor use |

The external dimensions include the wheels, fixed sensor housing and all permanent external features. Robot mass includes the chassis, enclosure, wheels, motors, battery/BMS, computer, sensors, wiring, connectors, fasteners and guards; payload is accounted for separately.

**Design intent:** a small, low-profile indoor assistant. Keep the battery and other heavy components low and near the centreline. Prioritise a short wheelbase, protected wheels, stable turns, safe stopping, service access and adequate ventilation. Do not add optional displays, audio or sensors unless their function justifies their mass, power and cost.

**Mass-reduction strategy:** use a lightweight but adequately stiff frame; consolidate compute/control electronics where technically appropriate; choose motors from calculated wheel torque and duty cycle rather than oversizing; minimise brackets, fasteners and duplicated housings; use appropriately rated lightweight enclosure materials; and maintain a component-level mass ledger. Do not reduce battery protection, electrical protection, wheel guarding or structural safety to meet the target.

**Engineering checks before design freeze:** verify the complete external envelope in CAD; weigh every selected component and the assembled robot; calculate centre of gravity and tip resistance; validate the 1–2 kg payload target, wheel loading, floor transitions, stopping distance, battery containment/charging, thermal behaviour, ventilation, acoustic performance and maintenance access.

**Status: PROPOSED / NOT MEASURED / NOT VALIDATED.** The 4–6 kg target and dimensions are not demonstrated by a physical prototype. The 10 kg value is a maximum design ceiling, not the expected mass. No stair climbing, outdoor terrain capability, waterproofing, fire resistance, IP rating or certified safety performance is claimed.


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
- [Preliminary internal layout and 4–6 kg target mass plan](docs/AI_HOME_INTERNAL_LAYOUT_AND_MASS_BUDGET.md) — packaging zones, category-level BOM and engineering gates; planning allocations only, not measured weights or selected parts.\n- [Indoor Perception MVP](docs/INDOOR_PERCEPTION_MVP.md) — initial deterministic CPU-first decision layer, conservative safe-hold logic and repeatable unit tests; no vision model or hardware integration is claimed.

### Software-only MVP demonstrator

The first AI HOME MVP work is being developed as a browser-only demonstrator. It uses synthetic temperature and humidity values; it is not connected to physical sensors.

- [MVP product specification](docs/MVP_PRODUCT_SPECIFICATION.md)
- [Sensor integration specification](docs/SENSOR_INTEGRATION_SPECIFICATION.md) — interface and validation requirements; no part selected or purchase approved.
- [Local dashboard specification](docs/DASHBOARD_SPECIFICATION.md)
- [Test and validation plan](docs/TEST_AND_VALIDATION_PLAN.md)
- [Open the local dashboard demo](demo/ai-home-dashboard/index.html) — open this HTML file in a modern browser; no installation is required.
- [Run the browser-based software self-tests](demo/ai-home-dashboard/tests.html) — execute deterministic decision-core checks locally without packages or network access.

The demo has configurable example thresholds and normal, warning, stale, disconnected and invalid scenarios. All readings are simulated, session-only and local to the browser. This work does not establish real sensor accuracy, a built robot, certified alarm capability or physical safety performance.

## Hardware & Materials Sourcing

PUI89 uses a traceable sourcing workflow for materials, mechanical parts, sensors, compute, power and control components. See the [bilingual Hardware & Materials Sourcing guide](https://pui89.github.io/materials.html) for the process covering exact manufacturer/model identification, Thailand and international supplier discovery, country-of-origin evidence, dated pricing and availability, lead times, shipping, compatibility checks and verification gates. Product-specific candidates are added only when supported by evidence; research candidates are not purchases or validated hardware.

## Perception & Task Intelligence (PTI)

**Role in this product:** support privacy-aware indoor awareness and owner-supervised assistance within a defined home environment. PTI is the shared PUI89 perception-and-task framework; the tasks below are intended capabilities and are not a claim of validated household autonomy.

**Priority perception tasks**
- Check camera and sensor quality, visibility, freshness and availability before interpreting a scene.
- Recognise supported rooms, common objects and people within explicitly defined scope.
- Detect obstacles and changes in the robot's immediate path; estimate distance only with suitable calibrated sensing.
- Interpret mapped indoor regions and navigable areas when a tested map/localisation stack is available.
- Fuse camera observations with approved proximity, contact, battery and environmental sensors while preserving source and uncertainty.
- Report unknown or conflicting conditions, request owner assistance and enter a safe hold when perception or localisation is unreliable.

**Task flow:** OBSERVE → PERCEIVE → ASSESS → DECIDE → RESPOND → LEARN FROM EVIDENCE. Outputs are owner-facing status, alerts and bounded assistance suggestions; they do not establish medical monitoring or unrestricted home autonomy.

**First evidence gate:** recorded indoor scenes and synthetic obstacle cases, followed by supervised tests in a controlled area. Measure obstacle misses, false alarms, localisation loss, safe-stop behaviour, privacy handling and resource use.

**Not established:** reliable household autonomy, medical/fall monitoring, safe operation around children or pets, or validated physical mobility. See the [shared PTI specification](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/perception/PUI89_PERCEPTION_TASK_INTELLIGENCE_V1.0.md) (maintainer repository access required).

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
**README snapshot (13 November 2026): 0 completed evidence-backed reviews.** This snapshot is not auto-synchronised; the live [PUI89 portfolio review register](https://pui89.github.io/#evidence-backed-project-reviews) is the source of truth.

This is a review-record count, not a statement that development or testing has not occurred. Engineering work, CI runs, test results and simulation evidence may support a review, but do not automatically count as a completed review.

A review is counted only when its record includes all required fields: **completed status, review date, defined scope, reviewer role, outcome, and at least one supporting evidence reference**. Drafts, ratings, stars, page views and comments are excluded.

The portfolio-wide count is published on the [PUI89 website](https://pui89.github.io/#evidence-backed-project-reviews). Refresh this README snapshot when the shared register changes.

**สถานะการทบทวนโครงการที่มีหลักฐาน**  
**จำนวนการทบทวนที่เสร็จสมบูรณ์: 0** — ยังไม่มีบันทึกการทบทวนที่ผ่านเกณฑ์สำหรับโครงการนี้ในทะเบียนกลาง PUI89

ตัวเลขนี้เป็นจำนวนบันทึกการทบทวน ไม่ได้หมายความว่าไม่มีการพัฒนาหรือทดสอบ งานวิศวกรรม ผล CI การทดสอบ และหลักฐานจากการจำลองอาจใช้ประกอบการทบทวน แต่ไม่นับเป็นการทบทวนที่เสร็จสมบูรณ์โดยอัตโนมัติ

จะนับเมื่อมีสถานะเสร็จสมบูรณ์ วันที่ ขอบเขต บทบาทผู้ทบทวน ผลการทบทวน และหลักฐานอ้างอิงอย่างน้อยหนึ่งรายการครบถ้วนเท่านั้น รายการร่าง คะแนน ดาว ยอดเข้าชม และความคิดเห็นจะไม่นับ
<!-- PUI89_EVIDENCE_BACKED_REVIEW:END -->

## AI Engineering Intelligence & Home-Robot Design

This project adopts PUI89 Engineering Intelligence to connect indoor perception, task planning, mechanical packaging, energy use, reliability and human-centred safety. The AI layer proposes and explains tasks; independent hardware safeguards and human authority remain essential.

**Product-specific design priorities**
- **Indoor mobility:** study footprint, turning radius, wheelbase, threshold crossing, floor transitions, carpet interaction, slope limits and low-speed stability.
- **Human-safe structure:** rounded external geometry, pinch/entrapment avoidance, compliant contact surfaces, guarded moving parts and accessible emergency stop.
- **Payload and manipulation:** target a 4–6 kg complete robot mass and retain 10 kg only as the maximum design ceiling; assess centre of mass, tip-over margin, braking distance, payload retention and safe handling separately.
- **Home-environment awareness:** detect people, pets, furniture, stairs, cables, spills and temporary obstacles with uncertainty-aware stop/slow/ask behaviour.
- **Power and thermal design:** assess battery protection, charging safety, runtime estimation, thermal monitoring, serviceability and graceful low-power shutdown.
- **Privacy by design:** local-first processing where feasible, clear camera/microphone states, data minimisation and user-controlled retention.
- **Environmental boundary:** design for indoor dust, spills and cleaning exposure; do not imply flood immersion or outdoor weather capability.

**AI engineering methods to evaluate:** visual/depth perception, semantic mapping, obstacle tracking, human/pet-aware scene understanding, task planning, voice/interface intelligence, anomaly detection, energy scheduling and indoor digital-twin simulation.

**Evidence gates:** accessible indoor dataset and task definitions → simulation and safety scenarios → stationary perception tests → supervised low-speed mobility tests → payload/stability and electrical safety review → controlled home pilot. Physical autonomy, manipulation and safety remain unvalidated until independently tested.


## Preliminary hardware sourcing

**Current research:** [Preliminary component sourcing and Thailand cost review](docs/PRELIMINARY_COMPONENT_SOURCING_AND_THAILAND_COSTS.md). Public price snapshots are estimates; origin and engineering compatibility remain subject to verification.

## Global-by-Design Product Requirement

**Strategic target:** every PUI89 product is designed for potential international use and lawful purchase, not only for the Thai market. This is a development and market-readiness target; it does **not** mean the product is currently manufactured, orderable, shipped worldwide, certified, or approved in every country.

### Requirements for global usability and purchasing
- **International usability:** design clear workflows, accessible interfaces, metric and local-unit support where relevant, time-zone/date/number formatting, and language-ready UI/documentation. English is the initial shared documentation language; additional languages are added according to user and market evidence.
- **Regional configuration:** make country, region, voltage/frequency, radio bands, network connectivity, environmental conditions, plugs/connectors, and local operating constraints explicit where applicable. Never assume one configuration fits every market.
- **Compliance before sale:** identify destination-country laws, product classification, safety, EMC/radio, electrical, battery transport, privacy, cybersecurity, accessibility, import/export, labelling and sector-specific requirements. Use qualified local review and accredited testing where required. Standards references are design inputs, not certification claims.
- **Purchasing transparency:** future buyer information must state exact model/configuration, included items, exclusions, intended use, limitations, warranty, maintenance, support, software/data terms, taxes, shipping, import duties, delivery region and return process. Publish a price only when supported by a dated quote or approved live price source.
- **Global supply and service:** qualify suppliers in multiple regions where practical; document manufacturer and country of manufacture, authorised distributors, spare parts, repair routes, lead times, end-of-life notices and regional support. Do not imply worldwide shipping or service until confirmed.
- **Open-source and commercial rights:** separate open-source software from hardware, model weights, datasets, trademarks and third-party components. Verify each licence and commercial-use right individually.
- **Privacy and security:** minimise collected data, document retention and data location, provide secure update and vulnerability-handling processes, and review applicable privacy laws before deployment.
- **Human safety and local operating limits:** preserve product-specific human oversight and safety boundaries. AI advisory software must not be described as autonomous physical control unless separately engineered, tested and legally approved.

### Release gates
1. **Global design-ready:** requirements, user groups, languages, regions and operating environments documented.
2. **Market research verified:** target-market demand, alternatives, price evidence and channel assumptions documented.
3. **Compliance mapped:** destination-market obligations identified; gaps and required tests recorded.
4. **Prototype validated:** reproducible technical, usability, reliability and safety evidence exists for the stated conditions.
5. **Commercially orderable:** exact configuration, verified price, production capacity, warranty, logistics, returns and support are confirmed.
6. **Region released:** all required local approvals, labels, documentation, import arrangements and service readiness are complete for that region.

**Current status:** global readiness is a portfolio-wide design target. Each product must report its actual gate and evidence separately. No product is to be described as globally available or purchasable until the relevant commercial and regional release gates are met.

**Shared standard:** [PUI89 Global Product Readiness Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/product/PUI89_GLOBAL_PRODUCT_READINESS_STANDARD_V1.0.md).
