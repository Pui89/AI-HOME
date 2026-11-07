# PUI89 AI HOME — AI Home Assistant Robot

## Project website QR codes

<table><tr><td align="center"><strong>English website</strong><br><a href="https://pui89.github.io/home.html"><img src="https://pui89.github.io/qr/home-en.png" width="160" alt="PUI89 AI HOME English website QR code"></a><br><a href="https://pui89.github.io/home.html">Open English website</a></td><td align="center"><strong>เว็บไซต์ภาษาไทย</strong><br><a href="https://pui89.github.io/home-th.html"><img src="https://pui89.github.io/qr/home-th.png" width="160" alt="QR Code เว็บไซต์ภาษาไทย PUI89 AI HOME"></a><br><a href="https://pui89.github.io/home-th.html">เปิดเว็บไซต์ภาษาไทย</a></td></tr></table>
### An Indoor Mobile Assistant for Home Safety, Monitoring and Everyday Support

**A calmer, more understandable view of home conditions.**

PUI89 AI HOME is a dedicated indoor mobile assistant concept focused on home safety, environmental monitoring and everyday support. It uses a compact four-wheel design and remains a separate product from PUI89 AI NOMAD, which is intended for indoor and outdoor mobility, travel and carrying assistance.

- **Project:** PUI89 AI HOME
- **Product type:** AI Home Assistant Robot
- **Repository:** https://github.com/Pui89/AI-HOME
- **Website:** [English](https://pui89.github.io/home.html) · [ภาษาไทย](https://pui89.github.io/home-th.html)
- **Related but independent product:** [PUI89 AI NOMAD](https://github.com/Pui89/AI-NOMAD)

![PUI89 AI HOME indoor four-wheel robot concept](https://pui89.github.io/images/homeguard-ai-home-concept.svg)

## Product purpose

HOME is intended to help residents understand changes and possible hazards inside a home or small building. It is a software-first, evidence-led concept; it is not a certified alarm, building inspector or replacement for qualified professionals.

Research areas include:
- Water leaks, moisture and humidity changes
- Smoke, abnormal heat and fire-related warning evidence
- Electrical anomaly indicators, without operating breakers or wiring
- Visible cracks and vibration/change observations, without claiming structural diagnosis
- Mold-risk conditions based on environmental evidence
- Sound, light, temperature and other environmental changes
- Clear reports showing what is known, unknown, changed, uncertain and worth checking

## Indoor robot concept — proposed requirements

| Parameter | Proposed target |
|---|---|
| Form | Compact four-wheel indoor mobile robot |
| Complete weight target | 8 kg |
| Absolute maximum complete weight | 10 kg |
| Environment | Indoor homes and buildings |
| Mobility | Four protected wheels; low-speed supervised movement |
| Safety | Soft perimeter bumper, obstacle/drop-off awareness, safe stop on uncertainty |
| Privacy | Minimal collection; avoid unnecessary video, face recognition and conversation recording |

The 8 kg target and 10 kg maximum include the battery, sensors, computer, enclosure and accessories. They are engineering requirements, not measured prototype specifications.

## Shared intelligence, independent products

HOME may reuse versioned PUI89 AI Core contracts and services:
- WorldState, Observation, ActionProposal and FailureReport
- Evidence provenance, freshness and sensor-health checks
- Uncertainty propagation and conflict/missing-data handling
- Human-reviewed recommendations and safety gates
- Reproducible tests and machine-readable reports

HOME and NOMAD must keep separate mechanical designs, navigation, sensor configurations, operating environments, risk assessments and validation evidence.

## Safety and privacy boundaries

- Certified smoke, fire, carbon-monoxide and electrical protection devices remain primary.
- Never delay evacuation or emergency procedures for AI analysis.
- HOME must not operate locks, breakers, valves, cooking appliances or certified alarms.
- Stop when localization, obstacle evidence or battery state is uncertain.
- Do not claim fire detection, structural diagnosis, electrical fault diagnosis or hazard prevention without appropriate evidence and independent validation.
- Minimize personal data and provide clear owner control.

## Development status

**FOUNDATION / CONCEPT / NOT VALIDATED.** This repository establishes the HOME product identity and requirements. No completed robot, real sensor integration, trained model, certified alarm function or real-world safety performance is claimed.

The development sequence is: requirements and hazard analysis → software contracts and deterministic synthetic scenarios → tests and evidence reports → simulation → reviewed sensor integration only when resources, licences, security and costs are approved.

## Zero-cost and supply-chain policy

No paid API, subscription, cloud GPU or automatic model download is required for this project foundation. No package or external service should be added without checking provenance, licence, security, resource requirements and total cost first. PUI89 excludes Chinese-origin AI models, providers and model-hosting services from its approved stack.

**PUI89 — Intelligent Systems. Verifiable Decisions. Safer Outcomes.**


## Hugging Face vision models — opt-in local integration

This repository now includes real Hugging Face checkpoint adapters in [`pui89_models/hf_vision.py`](pui89_models/hf_vision.py), with project-specific usage boundaries in [`docs/HUGGING_FACE_MODEL_INTEGRATION.md`](docs/HUGGING_FACE_MODEL_INTEGRATION.md).

- **OWLv2:** `google/owlv2-base-patch16-ensemble` for text-conditioned object proposals.
- **Intel DPT-Hybrid:** `Intel/dpt-hybrid-midas` for relative scene depth where appropriate; not calibrated distance or physical depth.
- **Zero-cost default:** no packages or model weights are installed/downloaded automatically; CPU-only inference, local cache only by default, no hosted inference API or cloud GPU.
- **Evidence status:** adapter code is added; model inference and project-specific accuracy are NOT YET TESTED. Outputs remain uncertain observations for human review, never actuator commands.

## Licence — Apache-2.0 for selected source code only

The Apache License, Version 2.0 applies **only** to the two source-code files listed in [`LICENSE-SCOPE.md`](LICENSE-SCOPE.md) and marked `SPDX-License-Identifier: Apache-2.0`:

- `pui89_models/hf_vision.py`
- `tests/test_hf_vision_adapter.py`

**Not licensed under Apache-2.0:** the PUI89 name, logos, trademarks, brand identity, AI HOME product identity, robot appearance and industrial/product designs, CAD or mechanical drawings, concept images/artwork, website, this README, other documentation, repository configuration, and all unlisted files. Those materials remain reserved to their respective rights holders, to the extent those rights exist and are owned or controlled by them. Third-party assets and models remain under their own terms.

See [`LICENSE`](LICENSE), [`LICENSE-SCOPE.md`](LICENSE-SCOPE.md) and [`NOTICE`](NOTICE). Apache-2.0 does not grant permission to use PUI89 trademarks or imply PUI89 endorsement.
