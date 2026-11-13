(() => {
  "use strict";
  const Core = window.Pui89HomeCore;
  if (!Core) throw new Error("AI HOME decision core did not load.");
  const $ = (id) => document.getElementById(id);
  let thresholds = { ...Core.DEFAULT_THRESHOLDS };
  let sample = null;
  const log = $("event-log");

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
  function setHealth(id, status) {
    const el = $(id);
    el.textContent = status.toUpperCase();
    el.dataset.state = status;
  }
  function render() {
    const result = Core.evaluate(sample, thresholds);
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
    $("action-proposal").textContent = result.actionProposal;
  }
  function applyScenario(key) {
    sample = Core.createScenarioSample(key);
    if (!sample) {
      addLog("Unknown scenario rejected.");
      return;
    }
    render();
    addLog(sample.label + " — overall state: " + Core.evaluate(sample, thresholds).state.toUpperCase() + ".");
  }
  function readThresholds() {
    const values = {
      tempLow: $("temp-low").value,
      tempHigh: $("temp-high").value,
      humidityLow: $("humidity-low").value,
      humidityHigh: $("humidity-high").value
    };
    const checked = Core.validateThresholds(values);
    if (!checked.valid) {
      $("threshold-message").textContent = "Invalid settings: " + checked.reason;
      addLog("Invalid demonstration thresholds rejected.");
      return;
    }
    thresholds = checked.values;
    $("threshold-message").textContent = "Demo thresholds applied. These are not safety limits.";
    render();
    addLog("Demonstration thresholds updated.");
  }

  $("apply-scenario").addEventListener("click", () => applyScenario($("scenario").value));
  $("save-thresholds").addEventListener("click", readThresholds);
  $("reset-thresholds").addEventListener("click", () => {
    thresholds = { ...Core.DEFAULT_THRESHOLDS };
    $("temp-low").value = thresholds.tempLow;
    $("temp-high").value = thresholds.tempHigh;
    $("humidity-low").value = thresholds.humidityLow;
    $("humidity-high").value = thresholds.humidityHigh;
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
