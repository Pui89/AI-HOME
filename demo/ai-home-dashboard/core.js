(() => {
  "use strict";
  const DEFAULT_THRESHOLDS = Object.freeze({
    tempLow: 18, tempHigh: 30, humidityLow: 30, humidityHigh: 70
  });
  const SCENARIOS = Object.freeze({
    normal: Object.freeze({ temperature: 26, humidity: 55, tempStatus: "connected", humidityStatus: "connected", label: "Normal simulated readings" }),
    hot: Object.freeze({ temperature: 34, humidity: 55, tempStatus: "connected", humidityStatus: "connected", label: "High temperature scenario" }),
    humid: Object.freeze({ temperature: 26, humidity: 82, tempStatus: "connected", humidityStatus: "connected", label: "High humidity scenario" }),
    stale: Object.freeze({ temperature: 24, humidity: 55, tempStatus: "stale", humidityStatus: "connected", label: "Stale temperature sample" }),
    disconnected: Object.freeze({ temperature: null, humidity: 55, tempStatus: "disconnected", humidityStatus: "connected", label: "Temperature channel disconnected" }),
    invalid: Object.freeze({ temperature: 26, humidity: "not-a-number", tempStatus: "connected", humidityStatus: "invalid", label: "Invalid humidity sample" })
  });

  function validateThresholds(input) {
    const keys = ["tempLow", "tempHigh", "humidityLow", "humidityHigh"];
    if (!input || keys.some((key) => input[key] === null || input[key] === undefined ||
        (typeof input[key] === "string" && input[key].trim() === ""))) {
      return { valid: false, values: null, reason: "All four threshold values are required." };
    }
    const values = Object.fromEntries(keys.map((key) => [key, Number(input[key])]));
    if (keys.some((key) => !Number.isFinite(values[key]))) {
      return { valid: false, values: null, reason: "Thresholds must be finite numbers." };
    }
    if (values.tempLow < -40 || values.tempHigh > 100 ||
        values.tempHigh < -40 || values.tempLow > 100) {
      return { valid: false, values: null, reason: "Temperature thresholds must be between -40 and 100 °C." };
    }
    if (values.humidityLow < 0 || values.humidityHigh > 100 ||
        values.humidityHigh < 0 || values.humidityLow > 100) {
      return { valid: false, values: null, reason: "Humidity thresholds must be between 0 and 100 %RH." };
    }
    if (values.tempLow >= values.tempHigh || values.humidityLow >= values.humidityHigh) {
      return { valid: false, values: null, reason: "Each low threshold must be lower than its high threshold." };
    }
    return { valid: true, values, reason: "Thresholds are valid demonstration settings." };
  }

  function createScenarioSample(key, observedAt) {
    const scenario = SCENARIOS[key];
    if (!scenario) return null;
    return { ...scenario, observedAt: observedAt || new Date().toISOString() };
  }

  function evaluate(sample, thresholds) {
    if (!sample) {
      return { state: "unavailable", reason: "No sample is available. No normal-state conclusion is made." };
    }
    const checked = validateThresholds(thresholds || DEFAULT_THRESHOLDS);
    if (!checked.valid) {
      return { state: "unavailable", reason: "Threshold configuration is invalid: " + checked.reason };
    }
    const statuses = [
      ["temperature", sample.tempStatus],
      ["humidity", sample.humidityStatus]
    ];
    const unhealthy = statuses.filter((entry) => entry[1] !== "connected");
    if (unhealthy.length) {
      const reasons = unhealthy.map((entry) => entry[0] + " is " + (entry[1] || "unknown"));
      return { state: "unavailable", reason: "Required evidence unavailable: " + reasons.join("; ") + ". No normal-state conclusion is made." };
    }
    if (typeof sample.temperature !== "number" || !Number.isFinite(sample.temperature) ||
        typeof sample.humidity !== "number" || !Number.isFinite(sample.humidity)) {
      return { state: "unavailable", reason: "A connected channel supplied an invalid value. No normal-state conclusion is made." };
    }
    const t = checked.values;
    const reasons = [];
    if (sample.temperature < t.tempLow || sample.temperature > t.tempHigh) reasons.push("temperature outside configured range");
    if (sample.humidity < t.humidityLow || sample.humidity > t.humidityHigh) reasons.push("humidity outside configured range");
    if (reasons.length) {
      return { state: "warning", reason: "Threshold warning: " + reasons.join("; ") + ". This is not a diagnosis." };
    }
    return { state: "normal", reason: "Both synthetic channels are connected and within the configured demonstration thresholds." };
  }

  globalThis.Pui89HomeCore = Object.freeze({
    DEFAULT_THRESHOLDS, SCENARIOS, validateThresholds, createScenarioSample, evaluate
  });
})();
