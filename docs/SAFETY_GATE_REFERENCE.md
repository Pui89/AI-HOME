# AI HOME safety-gate reference prototype

**Status:** Experimental software reference; not integrated with the robot or sensors.

## Purpose

This small, standard-library-only example demonstrates a fail-closed decision
boundary for future human-reviewed recommendations.

- Missing source, timestamp or provenance results in `HOLD`.
- Unhealthy, stale, conflicting or unresolved evidence results in `HOLD`.
- Restricted action categories and any execution request result in `BLOCKED`.
- Complete evidence can produce only `REVIEW_REQUIRED`.
- No result authorises a physical action.

## Run tests

From the repository root, using Python 3.10 or later:

```bash
python -m unittest discover -s tests -v
```

No third-party packages, models, network access, cloud services or hardware are
required.

## Important limitations

This is not a complete safety case, risk assessment, certified control system,
sensor-validation result or proof of safe robot operation. It does not calculate
sensor freshness from wall-clock time, calibrate sensors, establish ground truth,
or connect to any actuator. Thresholds and system-specific policy must be
derived from hazard analysis and verified evidence before any physical use.

The implementation is intentionally separate from model inference. Model output
must not be treated as trusted evidence without independent validation.
