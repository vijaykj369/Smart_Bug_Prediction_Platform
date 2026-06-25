import os
import joblib
import pandas as pd

# Absolute path to project root
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "bug_model.pkl"
)

FEATURES_PATH = os.path.join(
    BASE_DIR,
    "models",
    "features.pkl"
)

# Load model and feature list
model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)


def predict_bug(loc, vg, evg, branch_count, total_op):

    data = pd.DataFrame([{
        'loc': loc,
        'v(g)': vg,
        'ev(g)': evg,
        'branchCount': branch_count,
        'total_Op': total_op
    }])

    data = data[features]

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]
    confidence = round(max(probability) * 100, 2)

    if confidence >= 80:
        risk = "High"
    elif confidence >= 60:
        risk = "Medium"
    else:
        risk = "Low"

    return prediction, confidence, risk