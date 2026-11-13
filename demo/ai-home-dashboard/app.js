(() => {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const defaults = { tempLow: 18, tempHigh: 30, humidityLow: 30, humidityHigh: 70 };
  let thresholds = { ...defaults };
  let sample = null;
  const log = $("event-log");

  const scenarios = {
    normal: { temperature: 26, humidity: 55, tempStatus: "connected", humidityStatus: "connected", label: "Normal simulated readings" },
    hot: { temperature: 34, humidity: 55, tempStatus: "connected", humidityStatus: "connected", label: "High temperature scenario" },
    humid: { temperature: 26, humidity: 82, tempStatus: "connected", humidityStatus: "connected", label: "High humidity scenario" },
    stale: { temperature: 24, humidity: 55, tempStatus: "stale", humidityStatus: "connected", label: "Stale temperature sample" },
    disconnected: { temperature: null, humidity: 55, tempStatus: "disconnected", humidityStatus: "connected", label: "Temperature channel disconnected" },
    invalid: { temperature: 26, humidity: "not-a-number", tempStatus: "connected", humidityStatus: "invalid", label: "Invalid humidity sample" }
  };

  function timestamp() {
    return new Date().toLocaleString(undefined, { dateStyle: "medium", timeStyle: "medium" });
  }
  function addLog(message) {
    const item = document.createElement("li");
    const time = document.createElement("time");
    time.dateTime = new Date().toISOString();
    time.textContent = timestamp();
    item.append(time, document.createTextNode(message));
    log.prepend(item);
  }
  function validNumber(value) {
    return typeof value === "number" && Number.isFinite(value);
  }
  function within(value, low, high) {
    return validNumber(value) && value >= low && value <= high;
  }
  function evaluate() {
    if (!sample) return { state: "unavailable", reason: "No scenario has been applied yet." };
    const unhealthy = sample.tempStatus !== "connected" || sample.humidityStatus !== "connected";
    if (unhealthy) {
      const reasons = [];
      if (sample.tempStatus !== "connected") reasons.push("temperature is " + sample.tempStatus);
      if (sample.humidityStatus !== "connected") reasons.push("humidity is " + sample.humidityStatus);
      return { state: "unavailable", reason: "Required evidence unavailable: " + reasons.join("; ") + ". No normal-state conclusion is made." };
    }
    const tempOk = within(sample.temperature, thresholds.tempLow, thresholds.tempHigh);
    const humidityOk = within(sample.humidity, thresholds.humidityLow, thresholds.humidityHigh);
    if (!tempOk || !humidityOk) {
      const reasons = [];
      if (!tempOk) reasons.push("temperature outside configured range");
      if (!humidityOk) reasons.push("humidity outside configured range");
      return { state: "warning", reason: "Threshold warning: " + reasons.join("; ") + ". This is not a diagnosis." };
    }
    return { state: "normal", reason: "Both synthetic channels are fresh and within the configured demonstration thresholds." };
  }
  function setHealth(id, status) {
    const el = $(id);
    el.textContent = status.toUpperCase();
    el.dataset.state = status;
  }
  function render() {
    const result = evaluate();
    $("temperature").textContent = validNumber(sample?.temperature) ? sample.temperature.toFixed(1) : "—";
    $("humidity").textContent = validNumber(sample?.humidity) ? String(sample.humidity) : "—";
    $("temperature-state").textContent = sample ? sample.tempStatus + " · simulated" : "No sample";
    $("humidity-state").textContent = sample ? sample.humidityStatus + " · simulated" : "No sample";
    setHealth("temp-health", sample?.tempStatus || "disconnected");
    setHealth("humidity-health", sample?.humidityStatus || "disconnected");
    const pill = $("overall-state");
    pill.dataset.state = result.state;
    pill.textContent = result.state.toUpperCase() + " · SIMULATED";
    $("explanation").textContent = result.reason;
  }
  function applyScenario(key) {
    const source = scenarios[key];
    sample = { ...source, observedAt: new Date().toISOString() };
    render();
    addLog(source.label + " — overall state: " + evaluate().state.toUpperCase() + ".");
  }
  function readThresholds() {
    const values = {
      tempLow: Number($("temp-low").value),
      tempHigh: Number($("temp-high").value),
      humidityLow: Number($("humidity-low").value),
      humidityHigh: Number($("humidity-high").value)
    };
    if (Object.values(values).some((v) => !Number.isFinite(v)) ||
        values.tempLow >= values.tempHigh ||
        values.humidityLow >= values.humidityHigh ||
        values.tempLow < -40 || values.tempHigh > 100 ||
        values.humidityLow < 0 || values.humidityHigh > 100) {
      $("threshold-message").textContent = "Invalid settings. Check numeric values, order and demo input bounds.";
      return;
    }
    thresholds = values;
    $("threshold-message").textContent = "Demo thresholds applied. These are not safety limits.";
    render();
    addLog("Demonstration thresholds updated.");
  }

  $("apply-scenario").addEventListener("click", () => applyScenario($("scenario").value));
  $("save-thresholds").addEventListener("click", readThresholds);
  $("reset-thresholds").addEventListener("click", () => {
    thresholds = { ...defaults };
    $("temp-low").value = defaults.tempLow;
    $("temp-high").value = defaults.tempHigh;
    $("humidity-low").value = defaults.humidityLow;
    $("humidity-high").value = defaults.humidityHigh;
    $("threshold-message").textContent = "Default demonstration thresholds restored.";
    render();
    addLog("Default demonstration thresholds restored.");
  });
  $("clear-log").addEventListener("click", () => {
    log.replaceChildren();
    addLog("Session log cleared by user.");
  });
  applyScenario("normal");
})();
