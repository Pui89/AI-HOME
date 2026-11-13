(() => {
  "use strict";
  const Core = window.Pui89HomeCore;
  const output = document.getElementById("test-results");
  const summary = document.getElementById("test-summary");
  const cases = [];
  function test(name, fn) {
    try {
      fn();
      cases.push({ name, passed: true });
    } catch (error) {
      cases.push({ name, passed: false, error: error.message });
    }
  }
  function equal(actual, expected, message) {
    if (actual !== expected) throw new Error(message + " (expected " + expected + ", got " + actual + ")");
  }
  const defaults = Core.DEFAULT_THRESHOLDS;

  test("Normal synthetic readings return normal", () => {
    equal(Core.evaluate(Core.createScenarioSample("normal"), defaults).state, "normal", "Normal scenario");
  });
  test("High temperature returns warning", () => {
    equal(Core.evaluate(Core.createScenarioSample("hot"), defaults).state, "warning", "Hot scenario");
  });
  test("High humidity returns warning", () => {
    equal(Core.evaluate(Core.createScenarioSample("humid"), defaults).state, "warning", "Humid scenario");
  });
  test("Stale input fails closed", () => {
    equal(Core.evaluate(Core.createScenarioSample("stale"), defaults).state, "unavailable", "Stale scenario");
  });
  test("Disconnected input fails closed", () => {
    equal(Core.evaluate(Core.createScenarioSample("disconnected"), defaults).state, "unavailable", "Disconnected scenario");
  });
  test("Invalid input fails closed", () => {
    equal(Core.evaluate(Core.createScenarioSample("invalid"), defaults).state, "unavailable", "Invalid scenario");
  });
  test("Missing sample never becomes normal", () => {
    equal(Core.evaluate(null, defaults).state, "unavailable", "Missing sample");
  });
  test("Reversed thresholds are rejected", () => {
    equal(Core.validateThresholds({ ...defaults, tempLow: 35, tempHigh: 30 }).valid, false, "Reversed temperature thresholds");
  });
  test("Blank threshold is rejected", () => {
    equal(Core.validateThresholds({ ...defaults, humidityLow: "" }).valid, false, "Blank humidity threshold");
  });
  test("Out-of-range threshold is rejected", () => {
    equal(Core.validateThresholds({ ...defaults, humidityHigh: 101 }).valid, false, "Humidity upper bound");
  });
  test("Warning includes a human-review proposal", () => {\n    const result = Core.evaluate(Core.createScenarioSample("hot"), defaults);\n    if (!result.actionProposal || !result.actionProposal.includes("Human decision")) throw new Error("Warning proposal must require human review");\n  });\n  test("Unavailable input includes a fail-safe proposal", () => {\n    const result = Core.evaluate(Core.createScenarioSample("disconnected"), defaults);\n    if (!result.actionProposal || !result.actionProposal.includes("Do not infer")) throw new Error("Unavailable proposal must reject normal-state inference");\n  });\n  test("Unknown scenario is rejected", () => {
    equal(Core.createScenarioSample("unknown"), null, "Unknown scenario");
  });
  test("Boundary values are accepted", () => {
    equal(Core.validateThresholds({ tempLow: -40, tempHigh: 100, humidityLow: 0, humidityHigh: 100 }).valid, true, "Inclusive demo bounds");
  });

  output.replaceChildren();
  cases.forEach((item) => {
    const li = document.createElement("li");
    li.className = item.passed ? "pass" : "fail";
    li.textContent = (item.passed ? "PASS — " : "FAIL — ") + item.name + (item.error ? ": " + item.error : "");
    output.append(li);
  });
  const passed = cases.filter((item) => item.passed).length;
  const failed = cases.length - passed;
  summary.textContent = passed + " / " + cases.length + " checks passed" + (failed ? " · " + failed + " failed" : " · all checks passed");
  summary.dataset.state = failed ? "fail" : "pass";
})();
