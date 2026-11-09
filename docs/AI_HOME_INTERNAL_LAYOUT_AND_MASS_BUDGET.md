# PUI89 AI HOME — Preliminary Internal Layout and 8 kg Mass Budget

**Status:** Preliminary design study only. No components are selected, purchased, assembled, weighed or validated.  
**Design envelope:** 25 cm wide × 25 cm deep × 40 cm high, including fixed external features and wheels.  
**Complete mass ceiling:** 8.00 kg maximum, including battery and all installed parts.  
**Use:** Indoor residential concept; supervised movement only if a mobility prototype is later developed.

## 1. Design rules

1. The complete assembled unit must remain within 250 × 250 × 400 mm and 8.00 kg.
2. The mass ceiling includes chassis, enclosure, wheels, motors, battery/BMS, computer, sensors, displays, wiring, connectors, fasteners and protective parts.
3. The values below are planning allocations, not measured component weights or a bill of selected parts.
4. No part number, supplier, price, certification, runtime, speed, payload or protection rating is approved by this document.
5. If a real component exceeds its allocation, redesign or remove non-essential features; do not silently increase the 8 kg ceiling.
6. Keep heavy parts low and near the centreline; do not place the battery high in the sensor section.
7. Certified household smoke/fire/CO/electrical protection remains primary. AI HOME must not control locks, breakers, valves, appliances or certified alarms.

## 2. Preliminary vertical layout

The 40 cm height is the complete external envelope. The zones are packaging concepts and may overlap after detailed CAD and component selection.

| Vertical zone (from floor) | Proposed contents | Layout intent |
|---|---|---|
| 0–8 cm | Wheel/drive envelope, guarded moving parts, low base structure | Keep moving parts protected; preserve floor clearance and safe stopping |
| 8–17 cm | Battery with suitable enclosure/BMS, power protection | Place the heaviest subsystem low and close to the centre |
| 17–27 cm | Compute/control board, power conversion, cable routing | Accessible service area; separate heat sources from sensors and battery |
| 27–35 cm | Environmental sensor boards, air paths, status indicators | Avoid blocked vents; sensor placement must match each datasheet |
| 35–40 cm | Fixed upper sensor/camera/audio interface, if selected | Minimise top mass; privacy-by-design and no unnecessary recording |

**Horizontal packaging:** reserve a central protected electronics volume inside the 250 × 250 mm footprint. Wheel sweep, caster swivel, cable bend radius, ventilation, connector access and enclosure wall thickness must be included in CAD; nominal footprint alone does not prove fit.

**Mobility architecture:** four-wheel indoor concept only. A candidate arrangement is two powered drive wheels plus two passive support wheels, but wheel type, drive arrangement, motor count and geometry remain TBD pending torque, stability, floor-transition and stopping calculations. Do not treat this candidate as selected hardware.

## 3. Preliminary mass budget

| Subsystem allocation | Planning allowance |
|---|---:|
| Chassis and structural frame | 0.90 kg |
| Outer enclosure and access panels | 0.55 kg |
| Wheels, motors and mechanical drive | 1.25 kg |
| Battery and battery management/protection | 1.10 kg |
| Compute and control electronics | 0.55 kg |
| Environmental sensors and sensor mounts | 0.70 kg |
| Power conversion, fusing and electrical protection | 0.40 kg |
| Wiring, connectors and strain relief | 0.25 kg |
| User interface, indicators and audio (if retained) | 0.35 kg |
| Thermal management and ventilation parts | 0.25 kg |
| Fasteners, guards and service hardware | 0.45 kg |
| **Subtotal planning allocation** | **6.75 kg** |
| **Unallocated design margin** | **1.25 kg** |
| **Maximum complete mass** | **8.00 kg** |

The 1.25 kg margin is not permission to add optional hardware automatically. It is reserved for component variance, wiring, mounts, tolerances and design changes. The budget must be replaced by a component-by-component measured mass ledger before design freeze. Each row must eventually list exact manufacturer/model, quantity, datasheet/source, individual mass, measured mass, mounting mass and status.

## 4. Preliminary bill of materials (BOM) — categories only

| BOM group | Planning quantity | Required evidence before selection |
|---|---:|---|
| Chassis/frame and enclosure | 1 assembly | CAD, material datasheets, strength/stability review, mass |
| Wheels and drive units | TBD | Official motor/wheel datasheets, torque/speed/braking calculations, guarding |
| Battery pack and BMS | 1 system | Cell provenance, official datasheets, protection design, charging and thermal review |
| Compute/control unit | 1 system | Exact model, supported software, measured power/RAM/storage, licence |
| Temperature/humidity sensing | TBD | Range, accuracy, drift, calibration and placement data |
| Water/moisture sensing | TBD | Detection principle, coverage, false-alarm and repeatability test |
| Smoke/fire status interface | Optional; independent certified alarm remains primary | Manufacturer-approved interface and isolation review; no alarm control |
| Air/environment sensing | TBD | Exact target measurands, datasheet, calibration and cross-sensitivity review |
| Visual/context sensor | Optional | Privacy assessment, field of view, local processing and data-retention controls |
| Power conversion and protection | TBD | Voltage/current budget, fuse/protection calculations, component ratings |
| Wiring/connectors | TBD | Current rating, insulation, strain relief, temperature and service ratings |
| Indicators/audio/display | Optional | Accessibility, power budget and user-control review |
| Thermal/ventilation parts | TBD | Thermal model, airflow path, dust/ingress trade-off and bench evidence |
| Fasteners, seals and guards | TBD | Material/grade, retention, serviceability and inspection |

No purchases, supplier contact, account creation, trials, package installations or paid services are authorised. Research must use official, freely accessible manufacturer documentation where available; country of origin, licence, ongoing cost and safety approvals require separate review.

## 5. Engineering gates before design freeze

- [ ] CAD proves the complete external envelope is at most 250 × 250 × 400 mm.
- [ ] Component-level mass ledger, including fasteners and cables, totals at most 8.00 kg.
- [ ] Centre-of-gravity and tip-resistance analysis covers turns, slopes and emergency stops.
- [ ] Drive torque, speed, wheel loading, stopping distance and floor-transition limits are calculated.
- [ ] Battery energy, peak/continuous current, BMS, charging and thermal limits are documented.
- [ ] Electrical protection, fuse sizing, connector ratings and wiring diagram are reviewed.
- [ ] Sensor placement, coverage, blind spots, calibration and environmental limits are documented.
- [ ] Thermal dissipation, ventilation, ingress paths and maintenance access are assessed.
- [ ] Privacy/data-flow review is complete before camera/audio capture.
- [ ] Bench and supervised validation plans define pass/fail criteria and safe abort conditions.

## 6. Explicit limitations

This document does not establish that a 25 × 25 × 40 cm, 8 kg product is mechanically feasible. It does not establish a prototype, selected components, real sensor integration, runtime, navigation performance, waterproofing, fire resistance, IP rating, certified alarm function or safety certification. Stair climbing and rough-terrain operation are out of scope. Unknown values remain TBD.

## 7. Review record

Update this document only with traceable sources and evidence. Record revision, reviewer, exact changed values, supporting datasheets/calculations and unresolved risks. Never convert a planning allocation into a measured result without weighing the actual part.
