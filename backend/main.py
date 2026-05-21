from fastapi import FastAPI, File, UploadFile, Form
from predictor import get_recommendations
import cv2
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from sklearn.cluster import KMeans

app = FastAPI()

# CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# SKIN TONE DETECTION
# ---------------------------
def detect_skin_tone(image):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        return "unknown"
    
    img = cv2.resize(img, (300, 300))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l = lab[:, :, 0]
    a = lab[:, :, 1]

    brightness = np.mean(l)
    redness = np.mean(a)

    score = brightness + (0.3 * redness)

    if score > 175:
        return "fair"
    elif 145 <= score < 175:
        return "medium"
    elif 132 < score <= 145:
        return "dusky"
    else:
        return "dark"


# ---------------------------
# UNDERTONE DETECTION
# ---------------------------
def detect_undertone(image):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    
    if img is None:
        return "unknown"
    img = cv2.resize(img, (300, 300))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = np.mean(hsv[:, :, 0])

    if 11 <= h < 15:
        return "warm"
    elif 15 <= h <= 25:
        return "neutral"
    else:
        return "cool"

# ---------------------------
# K-MEANS COLOR EXTRACTION (ML PART)
# ---------------------------
def get_dominant_colors(image_bytes, k=3):
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (100, 100))

    img = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(img)

    colors = kmeans.cluster_centers_.astype(int)

    hex_colors = []
    for c in colors:
        hex_colors.append('#%02x%02x%02x' % (c[2], c[1], c[0]))

    return hex_colors

# ---------------------------
# HOME
# ---------------------------
@app.get("/")
def home():
    return {"message": "Backend running 🚀"}


# ---------------------------
# MANUAL MODE
# ---------------------------
@app.post("/recommend")
def recommend(
    gender: str = Form(...),
    skin_tone: str = Form(...),
    undertone: str = Form(...),
    occasion: str = Form(...)
):

    result = get_recommendations(
        gender,
        skin_tone,
        undertone,
        occasion
    )

    return {
        "mode": "manual",
        "output": result
    }


# ---------------------------
# IMAGE MODE
# ---------------------------
@app.post("/image_recommend")
async def image_recommend(
    face: UploadFile = File(...),
    hand: UploadFile = File(...),
    gender: str = Form(...),
    occasion: str = Form(...)
):

    face_bytes = await face.read()
    hand_bytes = await hand.read()

    skin_tone = detect_skin_tone(face_bytes)
    undertone = detect_undertone(hand_bytes)

    result = get_recommendations(
        gender,
        skin_tone,
        undertone,
        occasion
    )

    return {
        "mode": "image",
        "detected": {
            "skin_tone": skin_tone,
            "undertone": undertone
        },
        "output": result
    }