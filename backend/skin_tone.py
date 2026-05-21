import cv2
import numpy as np

def get_skin_tone(image_path):

    img = cv2.imread(image_path)

    if img is None:
        raise Exception(f"Image not found: {image_path}")

    # ---------------------------
    # FACE DETECTION (SAFE VERSION)
    # ---------------------------
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        img = img[y:y+h, x:x+w]

    # ---------------------------
    # ORIGINAL LAB METHOD (STABLE)
    # ---------------------------
    img = cv2.resize(img, (300, 300))
    img = cv2.GaussianBlur(img, (5, 5), 0)

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    L = lab[:, :, 0]

    brightness = np.mean(L)

    # ---------------------------
    # ORIGINAL WORKING THRESHOLDS
    # ---------------------------
    if brightness > 150:
        return "fair"
    elif brightness > 125:
        return "medium"
    elif brightness > 90:
        return "dusky"
    else:
        return "dark"