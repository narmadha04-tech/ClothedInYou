import cv2
import numpy as np

def get_undertone(image):

    img = cv2.resize(image, (300, 300))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bgr = img

    h = np.mean(hsv[:, :, 0])
    b = np.mean(bgr[:, :, 0])
    r = np.mean(bgr[:, :, 2])

    print("Hue:", h, "R:", r, "B:", b)

    # 🔥 FINAL LOGIC (STABLE)
    if r > b + 8:
        return "warm"
    elif b > r + 8:
        return "cool"
    else:
        return "neutral"