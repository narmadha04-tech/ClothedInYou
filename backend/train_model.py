from sklearn.preprocessing import OneHotEncoder  
from sklearn.compose import ColumnTransformer  
from sklearn.pipeline import Pipeline  
from sklearn.ensemble import RandomForestClassifier  
import pandas as pd  
import joblib  
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# FIXED PATH (go one level up from backend)
DATA_PATH = os.path.join(BASE_DIR, "..", "fashion_dataset.csv")

df = pd.read_csv(DATA_PATH)

X = df[["gender", "skin_tone", "undertone", "occasion"]]  
y_outfit = df["outfit"]  

preprocess = ColumnTransformer(  
    transformers=[  
        ("cat", OneHotEncoder(handle_unknown="ignore"),  
         ["gender", "skin_tone", "undertone", "occasion"])  
    ]  
)  

outfit_model = Pipeline(steps=[  
    ("preprocess", preprocess),  
    ("model", RandomForestClassifier())  
])  

outfit_model.fit(X, y_outfit)  

MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "outfit_model.pkl")
joblib.dump(outfit_model, MODEL_PATH)

print("✅ Model trained successfully")