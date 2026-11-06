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

## Robotics foundation model candidates — Non-Chinese origin only

### Shortlisted candidate: SmolVLA

- Checkpoint: [`lerobot/smolvla_base`](https://huggingface.co/lerobot/smolvla_base)
- Publisher/developer: Hugging Face / LeRobot
- Model-card licence: Apache-2.0
- Size: 450 million parameters
- Type: Vision-Language-Action (VLA); consumes camera images, robot state and an optional language instruction, and predicts continuous action sequences.
- Status: **CANDIDATE ONLY — not downloaded, installed, tested or approved for physical deployment.**

The model card describes SmolVLA as a compact VLA designed for robot manipulation research. It still requires robot-specific demonstrations, fine-tuning and evaluation; the published training guidance uses a GPU. Its 450M parameter count does not guarantee it will run acceptably on this project's available hardware or without cost.

### Project fit and limits

- **Coconut Harvest AI:** possible simulation-only research for a robot arm's bounded grasp/reach/cut-preparation proposal. It is not validated for harvesting, outdoor conditions, people/animals nearby, coconut mass, cutting forces or the 0–30 m operating concept. Cutting and release must remain independently guarded and human-supervised.
- **Flood Rescue AI:** not suitable as boat navigation, water-current control, rescue approach or propulsion policy. Consider only if a separate manipulator is designed, and then only in a controlled simulator with bounded proposals.
- **Sentinel Multimodal Screening AI:** not a substance-identification, search, enforcement or autonomous screening model. Consider only for a future non-consequential manipulator research task, if one is defined; otherwise do not integrate.
- **AI HOME:** not a general indoor mobile-navigation or hazard-response policy. Do not use for driving wheels, stairs, doors, appliance control or emergency response. A future arm/gripper task would require separate robot-specific validation.
- **AI NOMAD:** **not recommended for quadruped locomotion, gait, balance, foothold selection or outdoor navigation.** SmolVLA's manipulation focus does not establish dog-like mobility capability.
- **AI Car:** **not suitable for vehicle control.** No steering, throttle, braking, gear, propulsion or road-decision authority.
- **AI Motorcycle / EasyRide:** **not suitable for motorcycle control.** No steering, throttle, braking, balance, motor or rider-safety authority.

### Additional candidates not approved

- **OpenVLA 7B** ([model card](https://huggingface.co/openvla/openvla-7b)): research reference only, **HOLD — LICENCE REVIEW REQUIRED**. Although the Hugging Face card labels the checkpoint MIT, the upstream OpenVLA repository warns that the pretrained weights may inherit the Llama 2 Community License. The 7B model also has substantial compute needs and documents remote custom code. Do not adopt, download or commercially use until the exact weight terms and code are reconciled.

### Robotics safety rule

A VLA predicts actions; it is not a safety controller. In PUI89 it may only produce a bounded, logged **ActionProposal** for a simulator or an independently reviewed offline experiment. It must never issue actuator commands. Require typed observations, robot-specific coordinate/action mapping, joint and workspace limits, collision checks, speed/force limits, emergency stop, watchdog, deterministic safety interlocks, human approval, and a verified safe fallback outside the model. No physical robot tests are authorized by this documentation.



## Real Hugging Face model integration — offline OWL-ViT

This repository now contains an executable inference adapter for the real Hugging Face checkpoint **[google/owlvit-base-patch32](https://huggingface.co/google/owlvit-base-patch32)**. It runs zero-shot, text-conditioned object detection against a local image and writes a JSON evidence report with image SHA-256, model ID/revision, candidate labels, scores and bounding boxes.

**Run after manually preparing a compatible local environment and caching the checkpoint:**

```bash
python tools/huggingface_local_vision_demo.py path/to/local-image.jpg --json-out reports/hf-owlvit-report.json
```

- Default device is CPU; CUDA is opt-in with `--device cuda`.
- Both model and processor use `local_files_only=True`; safetensors are required. The script does not download weights, install packages, call hosted inference, or upload images.
- Candidate labels are configured for this project's domain and can be overridden with repeated `--label` arguments.
- The model card declares Apache-2.0 and describes OWL-ViT as zero-shot text-conditioned object detection. Review the exact checkpoint files, upstream licence and data disclosures before commercial release.
- **Status:** executable integration code added; model inference has not been run because weights and optional dependencies were not downloaded or installed. No accuracy, safety or field-performance claim is made.
- Output is an uncertain observation for human review only. It cannot authorize robot/vehicle actuation or consequential decisions.

The report builder is covered by standard-library tests in `tests/test_huggingface_local_vision_demo.py`; these tests validate report/safety metadata, not model accuracy.
