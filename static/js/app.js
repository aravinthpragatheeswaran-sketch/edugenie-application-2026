const mode = document.querySelector("#mode");
const input = document.querySelector("#input");
const result = document.querySelector("#result");
const status = document.querySelector("#status");
const run = document.querySelector("#run");

function updateFields() {
  const selected = mode.value;
  document.querySelector("#levelField").hidden = selected === "qa" || selected === "summarize" || selected === "quiz";
  document.querySelector("#countField").hidden = selected !== "quiz";
  document.querySelector("#weeksField").hidden = selected !== "learn/recommendations";
  input.placeholder = selected === "summarize" || selected === "quiz" ? "Paste your study material..." : "Enter a topic or question...";
}

function render(data, selected) {
  if (data.result) {
    result.textContent = data.result;
    return;
  }
  if (data.questions) {
    result.innerHTML = data.questions.map((item, index) => `<article class="quiz-question"><strong>${index + 1}. ${item.question}</strong><div class="options">${item.options.map(option => `<div class="option">${option}</div>`).join("")}</div><p class="feedback">Answer: ${item.answer}</p></article>`).join("");
    return;
  }
  if (data.steps) {
    result.innerHTML = data.steps.map(step => `<article class="path-step"><strong>Week ${step.week}: ${step.title}</strong><p>${step.focus}</p></article>`).join("");
  }
}

async function submit() {
  const selected = mode.value;
  const payload = selected === "qa" ? { question: input.value } : selected === "quiz" ? { text: input.value, count: Number(document.querySelector("#count").value) } : selected === "summarize" ? { text: input.value, length: "short" } : selected === "learn/recommendations" ? { topic: input.value, level: document.querySelector("#level").value, weeks: Number(document.querySelector("#weeks").value) } : { topic: input.value, level: document.querySelector("#level").value };
  if (!input.value.trim()) { status.textContent = "Add some material first."; return; }
  run.disabled = true;
  status.textContent = "Working...";
  try {
    const response = await fetch(`/${selected}`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) });
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || "Request failed");
    result.classList.remove("empty");
    render(data, selected);
    status.textContent = "Done.";
  } catch (error) { status.textContent = error.message; }
  finally { run.disabled = false; }
}

mode.addEventListener("change", updateFields);
run.addEventListener("click", submit);
document.querySelector("#clear").addEventListener("click", () => { result.textContent = "Your learning result will appear here."; result.className = "result empty"; status.textContent = ""; });
updateFields();