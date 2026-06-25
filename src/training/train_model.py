import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load dataset
df = pd.read_csv("data/kc1.csv")

# Selected 5 features
selected_features = [
    'loc',
    'v(g)',
    'ev(g)',
    'branchCount',
    'total_Op'
]

# Input features
X = df[selected_features]

# Target variable
y = (df['defects'] > 0).astype(int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    class_weight='balanced',
    random_state=42,
    n_jobs=-1
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Feature Importance
importance_df = pd.DataFrame({
    'Feature': selected_features,
    'Importance': model.feature_importances_
})

importance_df = importance_df.sort_values(
    by='Importance',
    ascending=False
)

print("\nFeature Importance:")
print(importance_df)

# Save model and feature list
joblib.dump(model, "models/bug_model.pkl")
joblib.dump(selected_features, "models/features.pkl")

print("\nModel saved successfully.")
print("Feature list saved successfully.")