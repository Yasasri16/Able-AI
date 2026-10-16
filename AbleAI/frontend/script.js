// ================================
// script.js — FINAL STABLE VERSION
// ================================

console.log("script.js loaded");

// -------------------------------
// DOM READY
// -------------------------------
document.addEventListener("DOMContentLoaded", () => {
  loadDarkMode();
  updateAuthUI();
});

// -------------------------------
// DARK MODE
// -------------------------------
function loadDarkMode() {
  const isDark = localStorage.getItem("darkMode") === "true";
  document.body.classList.toggle("dark", isDark);

  const toggle = document.getElementById("dark-toggle");
  if (toggle) {
    toggle.checked = isDark;
    toggle.addEventListener("change", toggleDarkMode);
  }
}

window.toggleDarkMode = function () {
  const isDark = !document.body.classList.contains("dark");
  document.body.classList.toggle("dark", isDark);
  localStorage.setItem("darkMode", isDark ? "true" : "false");
};

// -------------------------------
// AUTH UI
// -------------------------------
window.updateAuthUI = function () {
  const authArea = document.getElementById("auth-area");
  if (!authArea) return;

  const isLoggedIn = localStorage.getItem("isLoggedIn");
  const username = localStorage.getItem("username");

  if (isLoggedIn === "true" && username) {
    authArea.innerHTML = `
      <div style="display:flex;gap:10px;align-items:center;">
        <span>👤 ${username}</span>
        <button onclick="logout()">Logout</button>
      </div>
    `;
  } else {
    authArea.innerHTML = `
      <a href="login.html">Login</a>
      <a href="register.html">Sign Up</a>
    `;
  }
};

window.logout = function () {
  localStorage.clear();
  location.href = "index.html";
};

// -------------------------------
// BACKEND COMMUNICATION
// -------------------------------
const API_BASE = "http://localhost:8000";

async function postSentence(sentence) {
  if (!sentence || !sentence.trim()) return null;

  const res = await fetch(`${API_BASE}/process-gesture`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sentence })
  });

  return res.json();
}

window.sendToBackend = async function (text) {
  try {
    const data = await postSentence(text);
    if (data) updateUI(data);
  } catch (err) {
    console.error("Backend error:", err);
  }
};

window.sendGestureToBackend = async function (sentence) {
  try {
    const data = await postSentence(sentence);
    if (data) updateUI(data);
  } catch (err) {
    console.error("Gesture backend error:", err);
  }
};

// -------------------------------
// UI UPDATE
// -------------------------------
function updateUI(data) {
  const corrected = document.getElementById("correctedText");
  const final = document.getElementById("finalResponse");

  if (corrected) {
    corrected.innerText = "I understood: " + data.corrected_input;
  }

  if (final) {
    final.innerText = data.response;
  }

  speakText(data.response);
}

// -------------------------------
// TEXT TO SPEECH (AUTO)
// -------------------------------
let voices = [];

function loadVoices() {
  voices = speechSynthesis.getVoices();
}

loadVoices();
speechSynthesis.onvoiceschanged = loadVoices;

window.speakText = function (text) {
  if (!text) return;

  speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  const voice =
    voices.find(v => v.lang === "en-US") ||
    voices.find(v => v.lang.startsWith("en")) ||
    voices[0];

  utterance.voice = voice;
  utterance.lang = voice ? voice.lang : "en-US";
  utterance.rate = 1;
  utterance.pitch = 1;

  speechSynthesis.speak(utterance);
};

// -------------------------------
// FILE HANDLING (OPTIONAL)
// -------------------------------
window.handleFileUpload = function (input) {
  const preview = document.getElementById("file-preview-zone");
  if (!preview || !input.files.length) return;

  preview.innerHTML = `
    <div>
      📄 ${input.files[0].name}
      <button onclick="removeFile()">✕</button>
    </div>
  `;
};

window.removeFile = function () {
  const preview = document.getElementById("file-preview-zone");
  const fileInput = document.getElementById("file-upload");
  if (preview) preview.innerHTML = "";
  if (fileInput) fileInput.value = "";
};
