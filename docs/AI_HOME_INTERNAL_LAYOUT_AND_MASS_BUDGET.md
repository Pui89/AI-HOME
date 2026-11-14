# PUI89 AI HOME — Compact Layout and 4–6 kg Target Mass Plan

**Status:** Preliminary design study only. No components are selected, purchased, assembled, weighed or validated.  
**Revised design envelope:** 25–28 cm wide × 30–33 cm deep × 30–35 cm high, including wheels and fixed external features.  
**Complete robot mass target:** 4–6 kg, including battery and all installed parts.  
**Maximum design ceiling:** 10 kg; this is not the desired build mass.  
**Initial payload target:** 1–2 kg, additional to robot mass and subject to validation.  
**Use:** Indoor residential concept; supervised movement only if a mobility prototype is later developed.

## 1. Design rules

1. Design toward a complete robot mass of 4–6 kg; do not treat the 10 kg maximum design ceiling as the target.
2. The complete robot mass includes chassis, enclosure, wheels, motors, battery/BMS, computer, sensors, wiring, connectors, fasteners, guards and all installed accessories.
3. Payload is separate from robot mass and must be included in stability, wheel-load, torque, braking and runtime calculations.
4. No component mass, supplier, price, certification, runtime, speed, payload capability or protection rating is approved by this document.
5. Do not invent subsystem mass allocations before candidate components and mechanical architecture are selected. Record each candidate's datasheet mass and later measure the physical part.
6. Keep heavy components low and near the centreline. Avoid top-heavy sensor towers and unnecessary displays, duplicate controllers, oversized motors or decorative structure.
7. Certified household smoke/fire/CO/electrical protection remains primary. AI HOME must not control locks, breakers, valves, appliances or certified alarms.

## 2. Preliminary packaging envelope

| Parameter | Proposed range | CAD envelope for initial fit check |
|---|---:|---:|
| Width | 250–280 mm | 280 mm maximum |
| Length / depth | 300–330 mm | 330 mm maximum |
| Height | 300–350 mm | 350 mm maximum |

The envelope includes wheels, fixed sensor housing, guards and permanent external features. Internal zones are not frozen until a CAD layout and exact component dimensions are available.

**Packaging priorities**
- Base: protected wheel/drive arrangement, low centre of gravity and safe floor clearance.
- Lower central zone: battery enclosure, BMS and power protection.
- Middle zone: compute/control electronics and serviceable wiring.
- Upper zone: only the sensors and indicators required for the first product task.
- Reserve ventilation, cable bend radius, connector access, wheel sweep and maintenance clearance.

A candidate two-powered-wheel plus two-support-wheel layout may be evaluated, but no drive arrangement is selected. Motor count and wheel geometry remain TBD pending torque, stability, floor-transition and stopping calculations.

## 3. Component-level mass ledger — required before design freeze

No unsupported per-subsystem allocations are assigned at this stage. Populate this table from official manufacturer datasheets, supplier documentation and physical weighing.

| Subsystem / item | Manufacturer and exact model | Quantity | Datasheet mass (g) | Measured mass (g) | Mounts / wiring allowance (g) | Evidence / status |
|---|---|---:|---:|---:|---:|---|
| Chassis and frame | TBD | TBD | TBD | TBD | TBD | Pending |
| Enclosure and access panels | TBD | TBD | TBD | TBD | TBD | Pending |
| Wheels, motors and drive | TBD | TBD | TBD | TBD | TBD | Pending |
| Battery, BMS and containment | TBD | TBD | TBD | TBD | TBD | Pending |
| Compute and control electronics | TBD | TBD | TBD | TBD | TBD | Pending |
| Sensors and mounts | TBD | TBD | TBD | TBD | TBD | Pending |
| Power conversion, fuses and protection | TBD | TBD | TBD | TBD | TBD | Pending |
| Wiring, connectors and strain relief | TBD | TBD | TBD | TBD | TBD | Pending |
| Guards, fasteners and service parts | TBD | TBD | TBD | TBD | TBD | Pending |
| **Complete robot mass** |  |  | **TBD** | **TBD** | **TBD** | Must target 4–6 kg; must not exceed 10 kg ceiling |

Do not declare the target achieved from estimates alone. Report the measured assembled mass, scale resolution, configuration, battery state and included accessories.

## 4. Preliminary BOM categories

| BOM group | Required evidence before selection |
|---|---|
| Chassis/frame and enclosure | CAD, material datasheets, strength/stability review, mass and manufacturing method |
| Wheels and drive units | Official datasheets, torque/speed/braking calculations, guarded moving parts and mass |
| Battery pack and BMS | Cell provenance, official datasheets, protection design, charging and thermal review, complete mass |
| Compute/control unit | Exact model, supported software, measured power/RAM/storage, licence and mass |
| Environmental sensors | Measurement range, accuracy, drift, calibration and placement data |
| Power conversion and protection | Voltage/current budget, fuse/protection calculations and component ratings |
| Wiring/connectors | Current rating, insulation, strain relief, temperature and service ratings |
| Fasteners, seals and guards | Material/grade, retention, serviceability, inspection and mass |

No purchases, supplier contact, account creation, trials, package installations or paid services are authorised. Research must use official, freely accessible manufacturer documentation where available; country of origin, licence, ongoing cost and safety approvals require separate review.

## 5. Engineering gates before design freeze

- [ ] CAD proves the complete external envelope is within 280 × 330 × 350 mm.
- [ ] Component-level mass ledger targets 4–6 kg and the complete robot remains at or below 10 kg.
- [ ] Physical weighing confirms the assembled mass; estimates are not reported as measurements.
- [ ] Centre-of-gravity and tip-resistance analysis covers turns, slopes and emergency stops.
- [ ] Drive torque, speed, wheel loading, stopping distance and floor-transition limits are calculated.
- [ ] The 1–2 kg initial payload target is validated separately from robot mass.
- [ ] Battery energy, peak/continuous current, BMS, charging and thermal limits are documented.
- [ ] Electrical protection, fuse sizing, connector ratings and wiring diagram are reviewed.
- [ ] Sensor placement, coverage, blind spots, calibration and environmental limits are documented.
- [ ] Thermal dissipation, ventilation, ingress paths and maintenance access are assessed.
- [ ] Privacy/data-flow review is complete before camera/audio capture.
- [ ] Bench and supervised validation plans define pass/fail criteria and safe abort conditions.

## 6. Explicit limitations

This document does not establish that the proposed compact envelope, 4–6 kg target or 1–2 kg payload is mechanically feasible. It does not establish a prototype, selected components, real sensor integration, runtime, navigation performance, waterproofing, fire resistance, IP rating, certified alarm function or safety certification. Stair climbing and outdoor terrain operation are out of scope. Unknown values remain TBD.

## 7. Review record

Record revisions, reviewers, exact changed values, supporting datasheets/calculations, physical weighing records and unresolved risks. Never convert a planning target or supplier-listed mass into a measured result without weighing the actual installed part.
