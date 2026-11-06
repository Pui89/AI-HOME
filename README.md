# PUI89 AI HOME — Intelligent Home Assistant Robot
### An Indoor Mobile Assistant for Home Safety, Monitoring and Everyday Support

**A calmer, more understandable view of home conditions.**

PUI89 AI HOME is a dedicated indoor mobile assistant concept focused on home safety, environmental monitoring and everyday support. It uses a compact four-wheel design and remains a separate product from PUI89 AI NOMAD, which is intended for indoor and outdoor mobility, travel and carrying assistance.

- **Project:** PUI89 AI HOME
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

## Hugging Face model candidates — Non-Chinese origin only

**PUI89 mandatory rule:** use only models with verified non-Chinese developer and checkpoint provenance. Unknown or unclear origin means exclude. This section is a candidate list only; no weights have been downloaded, installed, or evaluated.

| Candidate checkpoint | Research role | Status |
|---|---|---|
| [microsoft/Florence-2-base](https://huggingface.co/microsoft/Florence-2-base) | Indoor scene descriptions, OCR and candidate object localization | CANDIDATE — review required |
| [facebook/dinov2-base](https://huggingface.co/facebook/dinov2-base) | Visual change and image-feature comparisons | CANDIDATE — review required |
| [google/siglip2-base-patch16-224](https://huggingface.co/google/siglip2-base-patch16-224) | Text-image similarity for household object and scene categories | CANDIDATE — review required |
| [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) | Optional multilingual voice-command transcription, subject to privacy controls | CANDIDATE — review required |

These models do not certify fire, electrical, structural, water, gas, mould or other hazard detection. Use appropriate physical sensors, deterministic thresholds, human review and independently tested alarms.

**Adoption gates:** verify the exact checkpoint's developer, origin, immutable revision, model-card and file licence, training-data disclosures, code/dependency security, file format, hardware fit and total cost before any download or execution. No paid APIs, hosted inference, cloud GPUs, automatic downloads or direct physical control. Florence-2 requires extra source review because its documented loader uses trust_remote_code=True. All models remain research-only until independently evaluated and approved.

**Shared policy:** [PUI89 Hugging Face Model Policy](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_HUGGINGFACE_MODEL_POLICY.md).

