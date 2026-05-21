from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "fashion_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "color_model.pkl")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Features
X = df[["gender", "skin_tone", "undertone", "occasion"]]
y_color = df["color"]

# Preprocessing (SAME AS OUTFIT MODEL)
preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"),
         ["gender", "skin_tone", "undertone", "occasion"])
    ]
)

# Model pipeline
color_model = Pipeline(steps=[
    ("preprocess", preprocess),
    ("model", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train
color_model.fit(X, y_color)

# Save model
joblib.dump(color_model, MODEL_PATH)

print("✅ Color model trained successfully")