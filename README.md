# Smart Bug Prediction Platform

## Overview

The Smart Bug Prediction Platform is a Machine Learning-based web application that predicts whether a software module is likely to contain defects (bugs) using software metrics. The system is trained on the KC1 software defect dataset and uses a Random Forest Classifier to identify bug-prone modules.

The platform provides an easy-to-use web interface where users can enter software metrics and receive predictions along with confidence scores and risk levels.

---

## Problem Statement

Software defects increase development costs, delay releases, and reduce software quality. Detecting bug-prone modules early in the software development lifecycle helps developers focus testing efforts on high-risk components.

This project aims to predict whether a software module is likely to contain defects using historical software metrics and machine learning techniques.

---

## Objectives

* Predict software defects using machine learning.
* Reduce manual effort in identifying bug-prone modules.
* Provide an interactive web interface for predictions.
* Demonstrate the practical application of machine learning in software engineering.

---

## Dataset

### Dataset Used

KC1 Software Defect Dataset

The KC1 dataset is a widely used software defect prediction dataset containing software metrics collected from real-world software modules.

### Target Variable

```text
defects
```

The target variable is converted into a binary classification problem:

```text
defects = 0  → Non-Buggy Module
defects > 0  → Buggy Module
```

---

## Selected Features

To simplify implementation and improve usability, only five important software metrics were selected:

| Feature     | Description           |
| ----------- | --------------------- |
| loc         | Lines of Code         |
| v(g)        | Cyclomatic Complexity |
| ev(g)       | Essential Complexity  |
| branchCount | Number of Branches    |
| total_Op    | Total Operators       |

---

## Machine Learning Model

### Algorithm Used

Random Forest Classifier

### Configuration

```python
RandomForestClassifier(
    n_estimators=300,
    class_weight='balanced',
    random_state=42
)
```

### Why Random Forest?

* Handles non-linear relationships.
* Works well on software metrics datasets.
* Reduces overfitting through ensemble learning.
* Provides feature importance analysis.
* Requires minimal preprocessing.

---

## Feature Importance

The trained model identified the following feature importance values:

| Feature     | Importance |
| ----------- | ---------- |
| total_Op    | 42.75%     |
| loc         | 38.96%     |
| branchCount | 8.60%      |
| v(g)        | 6.38%      |
| ev(g)       | 3.31%      |

This indicates that Total Operators and Lines of Code contribute most significantly to bug prediction.

---

## Model Performance

### Evaluation Metrics

Accuracy:

```text
79.15%
```

Confusion Matrix:

```text
[[298  59]
 [ 29  36]]
```

Classification Report:

```text
Precision (Buggy): 0.38
Recall (Buggy):    0.55
F1-Score:          0.45
```

### Interpretation

The model successfully identifies a significant portion of bug-prone modules while maintaining good overall classification performance.

---

## System Architecture

```text
KC1 Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Selection
      │
      ▼
Random Forest Training
      │
      ▼
Model Serialization
      │
      ▼
Prediction Module
      │
      ▼
Flask Web Application
      │
      ▼
User Interface
      │
      ▼
Bug Prediction Result
```

---

## Project Structure

```text
smart_bug_prediction_platform/
│
├── data/
│   └── kc1.csv
│
├── models/
│   ├── bug_model.pkl
│   └── features.pkl
│
├── src/
│   ├── app.py
│   │
│   ├── prediction/
│   │   └── predict.py
│   │
│   └── training/
│       └── train_model.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

### Programming Language

* Python 3.12

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Backend

* Flask

### Frontend

* HTML
* Bootstrap 5

### Version Control

* Git
* GitHub

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd smart_bug_prediction_platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

Run:

```bash
python src/training/train_model.py
```

Outputs:

```text
Accuracy
Confusion Matrix
Classification Report
Feature Importance
```

Generated files:

```text
models/bug_model.pkl
models/features.pkl
```

---

## Running the Application

Start the Flask server:

```bash
python src/app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Usage

1. Open the web application.
2. Enter the five software metrics:

   * LOC
   * Cyclomatic Complexity
   * Essential Complexity
   * Branch Count
   * Total Operators
3. Click the Predict button.
4. View:

   * Prediction Result
   * Confidence Score
   * Risk Level

---

## Sample Output

```text
Prediction Result:
Buggy Module

Confidence:
60.67%

Risk Level:
Medium
```

---

## Future Enhancements

* CSV Upload for Batch Predictions
* Prediction History Storage
* Interactive Dashboard
* Feature Importance Visualization
* Advanced Model Comparison
* Real-Time Software Metrics Extraction

---

## Applications

* Software Quality Assurance
* Defect Prediction
* Software Testing Prioritization
* Risk Assessment
* Software Maintenance Planning

---

## Conclusion

The Smart Bug Prediction Platform demonstrates the application of machine learning techniques for software defect prediction. By leveraging software metrics and a Random Forest classifier, the system can identify bug-prone modules and assist developers in improving software quality through early defect detection.
