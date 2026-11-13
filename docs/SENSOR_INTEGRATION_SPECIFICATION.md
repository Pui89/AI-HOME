# AI HOME Sensor Integration Specification

**Status:** Interface requirements only — no sensor selected and no hardware purchase approved.  
**Initial channel:** Temperature and relative humidity.

## 1. Purpose

Define a vendor-neutral boundary for a future environmental sensor so that the software can distinguish valid observations from missing, stale, malformed or implausible data.

## 2. Sensor channel contract

Each future observation should carry:
- `sensor_id`: stable, non-secret identifier;
- `channel`: `temperature_c` or `relative_humidity_pct`;
- `value`: numeric measurement;
- `unit`: `°C` or `%RH`;
- `observed_at`: source timestamp with timezone;
- `received_at`: system receipt timestamp with timezone;
- `status`: connected, disconnected, stale or invalid;
- `source_type`: simulated or physical;
- `quality_flags`: optional calibration, range, transport or self-test notes;
- `provenance`: sensor model/firmware and calibration record when known.

Do not silently replace absent readings with zero or a previous value.

## 3. Input validation

- Reject non-numeric, NaN and infinite values.
- Apply engineering plausibility bounds only as data-quality checks, not as hazard thresholds.
- Detect timestamps in the future beyond the allowed clock-skew tolerance.
- Mark readings stale after a documented freshness timeout.
- Preserve the original source timestamp and record receipt time separately.
- On communication loss, expose disconnected state; do not display the last value as current.
- Calibration status and measurement uncertainty must be recorded when physical sensors are introduced.

## 4. Transport and electrical integration

Transport is TBD until the selected board and sensor are reviewed. I²C, SPI, UART or another interface must not be assumed before a component-level design review. Any physical connection requires checks for voltage compatibility, pull-ups, connector polarity, grounding, cable length, electrical protection, enclosure, thermal placement and serviceability.

## 5. Candidate evaluation criteria

Evaluate any candidate against:
- manufacturer documentation and traceable origin;
- measurement range, accuracy conditions, repeatability and drift;
- calibration requirements and availability of reference equipment;
- interface and voltage compatibility;
- power budget and thermal self-heating;
- package, mounting, ventilation and enclosure effects;
- long-term availability, licence terms for libraries and firmware;
- local operation without cloud dependency.

No component is selected by this specification. A previously discussed sensor candidate remains research-only until formally reviewed and approved.

## 6. Data quality and failure behaviour

| Condition | Required software state | Required behaviour |
|---|---|---|
| Valid and fresh | connected | Evaluate configured threshold |
| No communication | disconnected | Show unavailable; log event |
| Older than freshness limit | stale | Show stale; do not treat as current |
| Malformed or out-of-range | invalid | Reject value; log reason |
| Calibration unknown | quality warning | Show limitation; do not imply traceable accuracy |

## 7. Shared AI Core mapping

A future sensor sample may map to an `Observation` with provenance, timestamps, units, quality and uncertainty. Derived environmental status may contribute to `WorldState`. No sensor reading should directly create an actuator command. If evidence is missing or conflicting, emit a failure/uncertainty record and hold the system in a non-actuating state.

## 8. Approval gate

Before hardware work: approve the exact part and source, inspect official datasheet, check licence and software provenance, review electrical/mechanical compatibility, define calibration/reference method, estimate total mass and power, and approve any purchase or installation separately.
