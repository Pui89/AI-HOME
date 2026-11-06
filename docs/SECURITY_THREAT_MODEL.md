# PUI89 AI HOME — Security and Safety Threat Model

**Status:** initial design baseline; not a certification or completed security assessment.

## Assets to protect
- Resident privacy, occupancy patterns, images, audio and household routines.
- Sensor observations, timestamps, calibration records and evidence provenance.
- Robot navigation state, action proposals, configuration and update integrity.
- Repository credentials, GitHub tokens, workflow permissions and software supply chain.
- Availability of the home's independent certified safety devices.

## Trust boundaries
1. Physical sensors and their firmware.
2. Local AI/model runtime and cached model files.
3. Home network, router and connected devices.
4. GitHub repository, pull requests, workflows and external dependencies.
5. Human operator reviewing observations and proposals.
6. Robot motion and any future actuator interface.

Treat data crossing every boundary as untrusted until validated. Do not assume sensor readings, model labels, prompts or network messages are authentic.

## Threats and required mitigations

| Threat | Required baseline |
|---|---|
| Private camera/audio or occupancy data exposed | Data minimization; no resident samples in Git; local-first processing; explicit consent and retention rules before capture features |
| Spoofed, stale, disconnected or miscalibrated sensors | Record source, timestamp, freshness, calibration and health; represent missing/conflicting evidence explicitly |
| False positive or missed hazard | Never replace certified alarms; human review; uncertainty reporting; corroboration where appropriate |
| Prompt injection or malicious image/text content | Treat model and user content as data, never executable instructions; constrain tools and outputs |
| Model hallucination or distribution shift | Model outputs remain proposals; test on representative labelled data; no safety claims without independent validation |
| Unauthorized robot movement | No physical actuation from model output; supervised movement only after separate hazard analysis; emergency stop and safe-stop design required before tests |
| Malicious dependency, model or GitHub Action | Verify publisher, exact revision, licence, provenance and integrity; minimize dependencies; review updates |
| Leaked token or secret | Never commit secrets; least-privilege tokens; rotate exposed credentials; do not pass secrets to untrusted pull requests |
| Workflow supply-chain compromise | Read-only GITHUB_TOKEN; review and pin third-party actions before production use; no write permissions in test jobs |
| Denial of service or resource exhaustion | Bound image sizes, input counts, runtime and memory; timeouts; fail safely without disabling certified devices |

## Non-negotiable safety boundaries
- AI HOME must not control locks, breakers, valves, cooking appliances, certified alarms or emergency systems.
- Never delay evacuation, emergency calls or established safety procedures for AI analysis.
- No structural, electrical, fire, smoke or mold diagnosis is claimed by this repository.
- A model score is not a probability of safety unless calibrated and validated for the exact task.
- Uncertain, contradictory, stale or missing evidence must not become a confident safe status.
- Physical robot tests require separate hazard analysis, a supervised test plan and an independent emergency stop.

## Release gates
Before any real sensor or robot deployment, document: threat review, data-flow diagram, privacy impact, dependency and model inventory, exact licences, vulnerability review, test evidence, failure handling, human override, recovery plan and independent safety review.

This file is a starting threat model. It does not establish that any control has been implemented or validated.
