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

## Real Hugging Face model integration — offline OWL-ViT

This repository now contains an executable inference adapter for the real Hugging Face checkpoint **[google/owlvit-base-patch32](https://huggingface.co/google/owlvit-base-patch32)**. It runs zero-shot, text-conditioned object detection against a local image and writes a JSON evidence report with image SHA-256, model ID/revision, candidate labels, scores and bounding boxes.

**Run after manually preparing a compatible local environment and caching the checkpoint:**

```bash
python tools/huggingface_local_vision_demo.py path/to/local-image.jpg --json-out reports/hf-owlvit-report.json
```

- Default device is CPU; CUDA is opt-in with `--device cuda`.
- Both model and processor use `local_files_only=True`; safetensors are required. The model revision is pinned to `cbc355fb364588351c5d51c7f74465e8e7ec6f72`. The safetensors weights are approximately 613 MB; check disk/RAM before any manual download. The script does not download weights, install packages, call hosted inference, or upload images.
- Candidate labels are configured for this project's domain and can be overridden with repeated `--label` arguments.
- The model card declares Apache-2.0 and describes OWL-ViT as zero-shot text-conditioned object detection. Review the exact checkpoint files, upstream licence and data disclosures before commercial release.
- **Status:** executable integration code added; model inference has not been run because weights and optional dependencies were not downloaded or installed. No accuracy, safety or field-performance claim is made.
- Output is an uncertain observation for human review only. It cannot authorize robot/vehicle actuation or consequential decisions.

The report builder is covered by standard-library tests in `tests/test_huggingface_local_vision_demo.py`; these tests validate report/safety metadata, not model accuracy.
