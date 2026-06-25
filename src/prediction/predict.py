import joblib
import pandas as pd

# Load model and feature list
model = joblib.load("models/bug_model.pkl")
features = joblib.load("models/features.pkl")


def predict_bug(loc, vg, evg, branch_count, total_op):

    data = pd.DataFrame([{
        'loc': loc,
        'v(g)': vg,
        'ev(g)': evg,
        'branchCount': branch_count,
        'total_Op': total_op
    }])

    # Ensure correct feature order
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