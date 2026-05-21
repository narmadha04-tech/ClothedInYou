import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
df = pd.read_csv("fashion_dataset.csv")

# Features
X = df[["gender", "skin_tone", "undertone", "occasion"]]
X = pd.get_dummies(X)

# Labels
y_outfit = df["outfit"]
y_color = df["color"]

# Ensure output folder exists
os.makedirs("../models", exist_ok=True)

print("X shape:", X.shape)
print("Training outfit model...")

# ================= OUTIFT MODEL =================
outfit_model = RandomForestClassifier(n_estimators=200, random_state=42)
outfit_model.fit(X, y_outfit)

joblib.dump(outfit_model, "../models/outfit_model.pkl")
print("✔ Outfit model saved")

# ================= COLOR MODEL =================
print("Training color model...")

color_model = RandomForestClassifier(n_estimators=200, random_state=42)
color_model.fit(X, y_color)

joblib.dump(color_model, "../models/color_model.pkl")
print("✔ Color model saved")

print("🎉 BOTH MODELS TRAINED SUCCESSFULLY")









































print("\n=============================")
print("MODEL EVALUATION RESULTS")
print("=============================")
print("Outfit Model Accuracy:", outfit_model.score(X, y_outfit))
print("Color Model Accuracy:", color_model.score(X, y_color))