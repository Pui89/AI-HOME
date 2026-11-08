# Contributing to PUI89 AI HOME — AI Home Assistant Robot

Thank you for helping improve PUI89 AI HOME, the PUI89 AI Home Assistant Robot project. This repository is currently a concept and software foundation, not a validated robot or certified safety product.

## Before proposing a change
- Explain the problem, affected files and expected behaviour.
- Separate implemented facts from proposals, assumptions and unverified claims.
- Keep changes small and reviewable.
- Do not add paid APIs, subscriptions, metered services, cloud GPUs or payment-card trials.
- Do not add Chinese-origin models, providers, tools or datasets.
- Do not download model weights or install packages as part of routine tests.
- Check exact code, model, dataset and documentation licences independently.
- Check dependency and action provenance, maintenance status, vulnerabilities and resource requirements.
- Do not commit credentials, tokens, personal data, private sensor recordings or model weights.

## Tests and workflows
- Prefer Python standard-library tests for the repository foundation.
- Keep CI least-privilege and read-only by default.
- Do not expose secrets to pull-request code.
- Do not add GitHub Actions or external dependencies without documented security and licence review.
- State exactly which tests ran; do not claim model inference or real-world validation when only adapter or contract tests ran.

## AI and robotics boundaries
Model results are uncertain observations for human review. They must not directly command motors, locks, breakers, valves, appliances or emergency systems. Preserve provenance, timestamps, sensor health, missing data, uncertainty and review outcomes.

## Pull requests
Include a concise summary, rationale, tests, security/privacy impact, licence/provenance impact and known limitations. Never bypass branch protection or required reviews.
