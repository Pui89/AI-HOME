# AI HOME — Preliminary Hardware Sourcing and Thailand Cost Review

**Research snapshot:** 14 November 2026  
**Status:** Research only. No supplier has been contacted, no quotation requested, and no purchase authorised. Prices and stock are public listing snapshots and may change.

## 1. Revised product targets

- External envelope: 250–280 mm W × 300–330 mm D × 300–350 mm H.
- Preferred complete robot mass: 5 kg; design range 4–6 kg, including battery and all installed parts.
- Hard complete-robot design ceiling: 6 kg; do not use this as a reason to add unnecessary mass.
- Initial payload target: 1 kg, additional to robot mass; 2 kg is a stretch target requiring separate validation.
- First engineering objective: low-speed, human-supervised indoor mobile platform.
- Candidate drive architecture for evaluation: two powered wheels with encoders plus two passive support wheels. This is a cost/weight-saving concept only; it is not yet selected.

## 2. Public price snapshots and origin status

| Subsystem | Candidate / exact model | Public price snapshot (THB) | Public source / seller | Origin status | Current decision |
|---|---|---:|---|---|---|
| Main computer | Raspberry Pi 5, 4 GB | ฿4,400 incl. VAT | Cytron Thailand listing; stock showed 12 at research time | Raspberry Pi states Pi 5 production at Sony UK Technology Centre in Wales and a Japan production line. Exact unit/batch must be checked from its marking and traceability. Board-level origin does not prove every semiconductor/component origin. | PENDING — verify actual unit marking and bill-of-material provenance |
| Main computer alternative | Raspberry Pi 5 board, variant unspecified | From ฿1,719 incl. VAT; variant not established by the listing snippet | Cytron Thailand catalogue | Same batch-specific origin issue | Do not use this price as a 4 GB price |
| Camera | Raspberry Pi Camera Module 3 | ฿1,050 displayed | Cytron Thailand catalogue | Exact camera module manufacturing country and image-sensor supply chain not established | PENDING |
| Short-range distance sensor | STMicroelectronics SATEL-VL53L4CD evaluation board | ฿894 incl. VAT at RS Thailand; 14 listed as available from international warehouse at snapshot | RS Thailand | ST is a European-headquartered manufacturer; country of manufacture for the exact board/sensor is not established by the listing | PENDING |
| Short-range distance sensor alternative | SATEL-VL53L4CD breakout board | ฿707.69 shown by DigiKey Thailand | DigiKey Thailand | Exact board and sensor manufacturing origin not established | PENDING |
| Drive motor | Sha Yang Ye IG32E-100K, 12 V, 60 RPM, 32 mm planetary gearmotor with encoder | ฿1,700 each incl. VAT; listing showed 3 in stock; listing advertised ฿1,615 each at 10+ | Cytron Thailand | Seller describes the maker as Taiwanese; exact country of manufacture and upstream component origin not evidenced | PENDING — obtain manufacturer declaration / product label |
| Drive motor, rejected example | DFRobot FIT0186, 12 V, 251 RPM, encoder | Search result from DigiKey Thailand: ฿550.28 | DigiKey Thailand | Distributor compliance data states China | REJECT — confirmed Chinese origin |
| Navigation upgrade | Hokuyo UST-10LX 2D LiDAR | Public overseas listing: US$1,200; another listing €1,365; no verified Thailand landed price | Acroname / ROS Components | Japanese manufacturer; exact manufacturing origin for supplied unit still needs confirmation | PENDING — defer from first prototype due cost |

**Price interpretation:** Prices are not a supplier quotation or landed cost. The Raspberry Pi 5 4 GB and RS sensor prices above are shown with VAT; other catalogue prices may have different tax, shipping and import treatment. Confirm tax, shipping, warranty, stock and exact SKU at quotation time.

## 3. Preliminary cost subtotal — only the listed items

Illustrative configuration for planning, not an approved BOM:

| Item | Quantity | Unit price | Subtotal |
|---|---:|---:|---:|
| Raspberry Pi 5 4 GB | 1 | ฿4,400 | ฿4,400 |
| Sha Yang Ye IG32E-100K motor candidate | 2 | ฿1,700 | ฿3,400 |
| Raspberry Pi Camera Module 3 | 1 | ฿1,050 | ฿1,050 |
| ST SATEL-VL53L4CD evaluation board | 2 | ฿894 | ฿1,788 |
| **Indicative subtotal** | | | **฿10,638** |

This subtotal excludes the battery and BMS, motor controller, MCU, chassis, wheels, passive supports, enclosure, wiring, connectors, fuse and power distribution, emergency stop, bump sensors, fasteners, fabrication, shipping and any import costs. It is therefore **not a complete robot price**. Origin status remains pending for the candidate parts; none is approved for purchase.

## 4. Cost-reduction strategy

1. **Keep the first build narrowly scoped.** Validate safe low-speed movement and obstacle response before adding advanced autonomy or optional displays.
2. **Evaluate two driven wheels plus two passive supports.** This may reduce motor, driver, wiring and mass requirements compared with four powered wheels. Validate turning, traction, stability and stopping before selection.
3. **Defer the Hokuyo LiDAR.** Its public overseas price is high relative to the target product. Start with a controlled test setup using appropriate short-range sensors and physical bump/stop protection; do not claim LiDAR-grade mapping or safety.
4. **Use one main computer.** Avoid a second SBC or AI accelerator until measured CPU/RAM tests show it is necessary.
5. **Avoid screens and decorative accessories** in the first prototype. Use a local web interface or phone/browser interface only if it can be implemented without paid services.
6. **Select motors by calculation, not price alone.** Calculate wheel torque, speed, acceleration, floor transitions, duty cycle, motor current and braking for the complete mass plus payload. Compare gear material, encoder output, backlash, thermal limits, warranty and replacement availability.
7. **Design one serviceable chassis.** Minimise unique brackets and fasteners, use flat panels and standard profiles where strength allows, and keep battery and heavy components low.
8. **Request a battery design quote only after electrical requirements are known.** Do not choose a pack by voltage alone. Define chemistry, cell provenance, capacity, continuous/peak current, BMS, charger, fuse, enclosure, thermal limits and test evidence first.
9. **Compare total landed cost in Thailand.** Compare local stock against overseas supply including freight, insurance, duty, VAT, brokerage, lead time and warranty handling.
10. **Do not trade away safety or provenance.** No unverified battery cells, no undersized motor driver, no removal of fuses/BMS/guards, and no unknown-origin part presented as approved.

## 5. Thailand supplier leads — not contacted or endorsed

| Supplier lead | Potential use | What must be confirmed |
|---|---|---|
| Cytron Thailand | Raspberry Pi, camera, motor and maker electronics listings | Exact SKU, origin evidence, tax invoice, stock, warranty and country of manufacture |
| RS Thailand | Industrial/electronic components, including ST evaluation boards | Exact manufacturer part number, shipping origin, stock and country of manufacture |
| DigiKey Thailand | Component sourcing and traceability/compliance data | Exact part, origin evidence, landed cost and delivery |
| Energy Mania, Bangkok | Potential custom battery-pack engineering/manufacture | Exact cell maker/model, cell country of manufacture, BMS, pack test reports, certification, quote and warranty |
| Microtron International Business, Bangkok | Potential battery-pack design and assembly | Cell provenance, BMS, pack design, test reports, certification, quote and warranty |
| MCU2ROBOT, Bangkok | Potential maker/robotics parts source | Exact brands/models, stock and manufacturing origin for every item |

These are research leads only. A supplier's Thai location or local assembly does not prove that the battery cells or components are non-Chinese-origin. No contact has been made.

## 6. Battery sourcing gate

Before asking for a quote, define and document:
- System voltage and minimum/maximum operating voltage.
- Required runtime and average/peak electrical load.
- Cell chemistry, exact manufacturer, cell model and manufacturing country.
- Cell datasheet, batch traceability and safety documentation.
- Pack configuration, capacity, continuous/peak current and mass.
- BMS protections, fuse, charger compatibility and temperature sensing.
- Enclosure, mounting, impact protection, service isolation and charging procedure.
- Pack test reports, applicable certifications, warranty and replacement process.
- Thailand delivery terms, shipping restrictions and landed cost.

Do not accept a quote that identifies only a reseller or pack assembler but does not identify the cell maker/model and manufacturing origin.

## 7. Import-to-Thailand checklist

For each shortlisted part, obtain the exact commercial invoice description, manufacturer part number, country-of-origin declaration, datasheet, HS code proposal, Incoterm, shipping method, insurance, lead time and warranty terms. Confirm HS classification and any import restrictions with a qualified Thai customs broker or relevant authority before ordering. Calculate duty and VAT from the actual classification and customs value; do not assume a universal duty rate. For lithium batteries, verify carrier rules, packaging and transport documentation before shipment.

## 8. Approval and next engineering gates

- [ ] Confirm payload use case and target floor/threshold conditions.
- [ ] Calculate motor torque, wheel size, speed, current, driver rating and stopping distance.
- [ ] Define battery voltage, energy, current and runtime before requesting a pack quote.
- [ ] Obtain official origin evidence for the exact motor, camera, sensor board and computer batch.
- [ ] Compare at least two technically compatible non-Chinese-origin candidates per critical subsystem.
- [ ] Build a full BOM with exact models, measured mass, supplier, dated price, tax, lead time and landed cost.
- [ ] Complete CAD packaging and a component-level mass budget before design freeze.
- [ ] Perform supervised bench tests and safety review before mobile operation.

**No purchases, supplier contacts, account registrations, downloads, installations or paid services are authorised by this research document.** All items remain PENDING or REJECT until their exact origin, technical fit and safety evidence are reviewed.
