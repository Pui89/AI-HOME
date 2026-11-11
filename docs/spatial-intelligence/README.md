# AI HOME: Spatial and Network Intelligence integration profile

## Intended use
Advisory indoor room layout, obstacle and spatial-change context. A future optional network-inventory view may help users understand the local devices and compute infrastructure supporting AI HOME.

## Planned spatial tasks
- Indoor room and obstacle geometry
- Spatial change records with provenance and timestamps
- Evidence references for human inspection

## Network Intelligence reference
PUI89 Network Intelligence v0.1 is implemented in the [Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core/tree/main/pui89_core/network_topology.py) and merged through [PR #37](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/37). The associated [GitHub Actions run](https://github.com/Pui89/PUI89-Shared-AI-Core/actions/runs/42984419052) completed successfully.

Its current scope is a static, user-declared inventory and deterministic SVG diagram. It does not discover devices, scan ports, test reachability, verify network security, read credentials, change configurations, or perform live monitoring. AI HOME has not yet adopted this module at runtime.

Treat real network inventories and diagrams as sensitive infrastructure data. Use fictional or synthetic examples in public tests and documentation.

## Safety boundaries
- Geometry does not identify fire, gas, electrical, structural or health hazards.
- Network topology does not prove device availability, security or correct configuration.
- No emergency response or home-safety guarantee.
- Privacy-preserving local processing and sensor permissions require separate review.
- No physical actuation is enabled.

Require lawful data provenance, calibration, synchronized timestamps, sensor-health checks, uncertainty handling, synthetic fault tests and human review before runtime use.

**Status:** Shared Core Network Intelligence is implemented and its CI check passed; AI HOME runtime adapter, real sensor integration, accuracy and field validation remain pending. No paid services or hardware purchase required.
