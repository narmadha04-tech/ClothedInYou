const API = "http://127.0.0.1:8000";

let gender = "";
let skin = "";
let undertone = "";
let occasion = "";

// FILE NAME DISPLAY
document.getElementById("face").addEventListener("change", function () {
    document.getElementById("faceName").innerText =
        this.files[0]?.name || "No file chosen";
});

document.getElementById("hand").addEventListener("change", function () {
    document.getElementById("handName").innerText =
        this.files[0]?.name || "No file chosen";
});

// NAVIGATION
function goToGender() {
    document.getElementById("landing").classList.add("hidden");
    document.getElementById("genderSection").classList.remove("hidden");
}

function selectGender(g) {
    gender = g;
    document.getElementById("genderSection").classList.add("hidden");
    document.getElementById("modeSection").classList.remove("hidden");
}

function showManual() {
    document.getElementById("modeSection").classList.add("hidden");
    document.getElementById("manualSection").classList.remove("hidden");
}

function showImage() {
    document.getElementById("modeSection").classList.add("hidden");
    document.getElementById("imageSection").classList.remove("hidden");
}

// VALUE SETTER (FIXED ERROR HERE ✅)
function setValue(type, value, el) {

    if (!el) return; // prevents crash

    if (type === "skin") skin = value;
    if (type === "undertone") undertone = value;
    if (type === "occasion") occasion = value;

    // remove active from siblings
    el.parentElement.querySelectorAll(".pill")
        .forEach(p => p.classList.remove("active"));

    el.classList.add("active");
}

// MANUAL API
async function getManual() {

    if (!gender || !skin || !undertone || !occasion) {
        alert("Please select all options");
        return;
    }

    const formData = new FormData();
    formData.append("gender", gender);
    formData.append("skin_tone", skin);
    formData.append("undertone", undertone);
    formData.append("occasion", occasion);

    const res = await fetch(API + "/recommend", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    displayResult("manualResult", data.output);
}

// IMAGE ANALYZE (FIXED KEYS ✅)
async function analyzeImages() {

    const face = document.getElementById("face").files[0];
    const hand = document.getElementById("hand").files[0];
    console.log("Face file:", face);
    console.log("Hand file:", hand);

    if (!face || !hand) {
        alert("Upload both images");
        return;
    }

    const formData = new FormData();
    formData.append("face", face);
    formData.append("hand", hand);
    formData.append("gender", gender);
    formData.append("occasion", occasion);

    const res = await fetch(API + "/image_recommend", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    skin = data.detected.skin_tone;
    undertone = data.detected.undertone;

    document.getElementById("detectResult").innerHTML =
        `<b>Detected:</b> ${skin} | ${undertone}`;
}

// IMAGE RESULT
async function getImageOutfit() {

    if (!gender || !skin || !undertone || !occasion) {
        alert("Complete all steps first!");
        return;
    }

    const formData = new FormData();
    formData.append("gender", gender);
    formData.append("skin_tone", skin);
    formData.append("undertone", undertone);
    formData.append("occasion", occasion);

    const res = await fetch(API + "/recommend", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    displayResult("imageResult", data.output);
}

// DISPLAY RESULT (CLEAN UI)
function displayResult(id, output) {

    let html = `<h2>Palette</h2><div class="palette-grid">`;

    output.palette.forEach(c => {
        html += `
        <div class="color-card">
            <div class="color-top" style="background:${c}"></div>
        </div>`;
    });

    html += `</div><h2>Outfits</h2><div class="outfit-grid">`;

    output.outfits.forEach(o => {
        html += `
        <div class="mode-card">
            <b>${o.name}</b>
            <div class="tip">💡 ${o.tip}</div>
        </div>`;
    });

    html += `</div>`;

    document.getElementById(id).innerHTML = html;
}