# Security Policy

## Scope
This policy covers the PUI89 AI HOME repository, source code, documentation, tests, workflows and proposed indoor robot concept.

**Project status:** foundation / concept / not validated. AI HOME is not a certified alarm, medical device, building inspector or emergency-response system.

## Reporting a vulnerability
Do not publish exploitable vulnerability details in a public issue or pull request.

1. Check whether GitHub **Private vulnerability reporting** is enabled. If so, use the repository's **Security → Advisories → Report a vulnerability** flow.
2. If private reporting is unavailable, contact the repository owner privately through the contact route on the PUI89 GitHub profile. Share only the minimum information needed to reproduce the issue.
3. Do not include resident data, credentials, access tokens, private camera footage or other personal information.

A report should include the affected commit/version, impact, safe reproduction steps and suggested mitigation. Allow time for investigation and coordinated remediation before public disclosure. Do not access, alter, retain or disclose data that is not yours.

## Supported versions
Only the current default branch is actively maintained. Older branches and unmerged pull requests are not security-supported releases.

## Security controls and project boundaries
- Keep GitHub Actions permissions least-privilege; workflows should be read-only unless a separately reviewed task requires more.
- Never commit secrets, personal data, sensor recordings, model weights or credentials.
- Do not execute untrusted pull-request code with repository secrets or write tokens.
- Review dependency, action, model, dataset and licence provenance before adoption.
- Model outputs are untrusted observations requiring validation and human review; they are not actuator commands.
- Do not use this concept as a replacement for certified smoke, fire, carbon-monoxide, electrical or other safety devices.
- No automatic operation of locks, breakers, valves, appliances or emergency systems.
- Preserve uncertainty, missing evidence and sensor faults; fail safely when evidence is unreliable.

## Response
The maintainer will assess reported impact, reproduce the issue where safe, prepare a fix and document any user action needed. No response-time guarantee is made for this concept repository.
