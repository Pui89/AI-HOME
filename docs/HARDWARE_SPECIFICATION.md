# PUI89 AI Home Assistant Robot — Hardware Specification and Selection Criteria

**Status:** Research specification only. No parts are selected, purchased or validated by this document.

## 1. Current design targets

| Item | Current target | Evidence status |
|---|---|---|
| Platform | Four-wheel indoor mobile assistant | Concept only |
| Complete mass | 8 kg target; 10 kg maximum including battery, sensors, computer, enclosure and accessories | Proposed; not measured |
| Dimensions | Not yet specified | TBD |
| Speed and acceleration | Not yet specified; low-speed supervised movement is the design intent | TBD |
| Turning radius and floor clearance | Not yet specified | TBD |
| Runtime and charging time | Not yet specified | TBD |
| Payload and stability | Not yet specified | TBD |
| Water-ingress and dust protection | Rating to be selected from hazard analysis and verified test requirements | TBD |
| Fire/heat performance | Must be based on verified component/material ratings and system-level hazard review | TBD |

Do not publish a waterproof, fireproof, stair-safe, child-safe or pet-safe claim without relevant test evidence and independent review.

## 2. Subsystem selection checklist

| Subsystem | Selection criteria | Evidence required before approval |
|---|---|---|
| Chassis and enclosure | Stability, cleanability, service access, impact protection, mass and manufacturability | Mechanical drawings, material datasheets, load/stability analysis and prototype inspection |
| Wheels and drive | Indoor floor compatibility, controllability, guarded moving parts and predictable stopping | Motor/gearbox datasheets, speed/torque calculations and controlled stopping tests |
| Compute | Supported OS/runtime, measured RAM/storage/power fit, secure update path and offline capability | Exact model, official datasheet, reproducible resource measurements and licence |
| Sensors | Defined measurement range, accuracy, drift, response time, placement and calibration method | Official datasheet, calibration procedure and project-specific bench test |
| Water/moisture | Corrosion resistance, placement, false-alarm handling and serviceability | Sensor datasheet, coverage test and wet/dry repeatability results |
| Temperature/humidity | Operating range, accuracy, drift and condensation tolerance | Datasheet, calibration and environmental test record |
| Smoke/fire interface | Certified independent alarm remains primary; only a permitted, isolated status interface may be considered | Local compliance review, manufacturer interface documentation and electrical isolation review |
| Electrical monitoring | Non-invasive and legally permitted measurement only | Qualified professional review, applicable approvals and measurement validation |
| Battery and charging | Cell provenance, protection/BMS, thermal limits, charging control and safe enclosure | Manufacturer datasheets, applicable certification, BMS documentation and supervised tests |
| Wiring and connectors | Current rating, strain relief, insulation, ingress protection and serviceability | Datasheets, wiring diagram and inspection |
| Network | Local-first, authenticated access, minimal exposed services and offline behaviour | Threat review, configuration and network-loss tests |
| Materials | Verified heat/flame, impact, cleaning and ageing properties appropriate to the hazard | Exact grade datasheet and relevant test/certification reports |

## 3. Required engineering calculations

Before a hardware configuration is approved, calculate and document:

- Complete mass budget with every component and margin.
- Centre of gravity and static/dynamic stability for expected slopes and stopping.
- Wheel torque, speed, acceleration, braking/stopping distance and thermal duty.
- Battery energy budget, peak/continuous current, runtime estimate and thermal limits.
- Power distribution, fuse/protection sizing, wiring and connector ratings.
- Sensor coverage, blind spots, placement, calibration interval and environmental limits.
- Enclosure heat dissipation, ventilation, ingress paths and service access.

All values must cite the exact component datasheet and calculation assumptions. Unknown values stay **TBD**.

## 4. Water, heat and fire protection

- Define foreseeable exposure scenarios before choosing an ingress-protection target.
- Select enclosure, seals, connectors and vents as a complete system; a component rating does not prove whole-robot protection.
- Use verified material grades and supplier documentation; marketing phrases such as “fire resistant” are insufficient.
- Keep batteries away from foreseeable water ingress and heat sources; design for monitoring, isolation and safe charging.
- Never test with live mains wiring, open flames or hazardous smoke as an informal experiment. Use qualified facilities and approved procedures where required.

## 5. Zero-cost procurement rule

This document authorises **research only**, not purchasing. Do not contact suppliers, order samples, create accounts, activate trials or pay for tools without explicit approval. Prefer official datasheets and freely accessible technical documentation. Check country of origin, ownership, exact licence, safety approvals, lifecycle support and total cost before considering any candidate.

## 6. Selection record

For each candidate, record subsystem, exact manufacturer/model/revision, official source, country/origin evidence, datasheet date, price and ongoing costs, licence/terms, safety approvals, power/resource needs, known limitations, comparison result and decision (**APPROVED FOR BENCH TEST / RESEARCH ONLY / REJECTED**). No candidate is approved by appearing in this template.
