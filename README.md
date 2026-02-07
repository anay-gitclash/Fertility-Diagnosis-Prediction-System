🧬 Fertility Diagnosis Prediction System

Healthcare ML Proof of Concept | CatBoost · FastAPI · Streamlit

📌 Overview

This project is a healthcare machine learning proof of concept that predicts fertility diagnosis outcomes (Normal / Altered) based on patient lifestyle and medical history data.

The focus of this project is not clinical deployment, but to demonstrate:

Correct healthcare ML problem framing

Handling categorical medical features

Managing class imbalance

Using appropriate evaluation metrics

End-to-end ML deployment (Model → API → UI)

Ethical awareness in medical AI

🎯 Problem Statement

Predict whether a fertility diagnosis is Normal or Altered using features such as:

Age and sedentary behavior

Lifestyle habits (alcohol consumption, smoking)

Medical history (childhood diseases, trauma, surgeries, fevers)

This is framed as a binary classification problem.

📊 Dataset

Source: Public fertility dataset

Size: 100 records

Target Variable: Diagnosis (Normal / Altered)

Key Challenge: Severe class imbalance

⚠️ Dataset Limitations

Very small sample size

Limited positive (Altered) cases

No direct IVF clinic data due to privacy constraints

➡️ Therefore, the project is treated as a proof of concept, not a production-ready medical model.

🧠 Feature Types
Numerical Features

Age

Number of hours spent sitting per day

Categorical Features

Season

Childish diseases (Yes / No)

Accident or serious trauma

Surgical intervention

High fevers in the last year

Frequency of alcohol consumption

Smoking habit

All categorical features are kept as string/object types.

🏗️ Model Choice
CatBoostClassifier
Why CatBoost?

Native handling of categorical features

No manual encoding required

Reduced risk of data leakage

Performs well on small datasets

Suitable for healthcare ML prototypes

📐 Evaluation Strategy
❌ Why Accuracy Alone Is Misleading

Due to class imbalance, a model can achieve high accuracy by predicting only the majority class while failing clinically.

✅ Metrics Used

Confusion Matrix

Precision, Recall, F1-Score

ROC-AUC

Clinical Priority

Recall for the Altered class (missing high-risk cases is more critical than false alarms)

📈 Final Results (Test Set)
Metric	Value
Recall (Altered)	0.33
Precision (Altered)	1.00
ROC-AUC	~0.71
Accuracy	~94%
Interpretation

The model successfully learns minority-class signal

Performance is limited by dataset size

Results are honest and realistic, not over-optimized

⚖️ Class Imbalance Handling

Applied class-weighted loss

Adjusted prediction threshold

Prioritized recall over raw accuracy

This reflects real healthcare ML decision-making.

🚀 Deployment Architecture
Backend

FastAPI

Pydantic for input validation

JSON-based prediction endpoint

Confidence score returned

Frontend

Streamlit

Simple UI for demonstration

Calls FastAPI backend

Displays prediction, confidence, and disclaimer

🛑 Ethical Disclaimer

⚠️ This project is for educational and demonstration purposes only.
It is NOT a medical diagnostic tool and must not be used for clinical decision-making.

Ethical transparency is intentionally emphasized.

🔮 Future Improvements

Access to larger clinical or IVF-specific datasets

Synthetic data generation aligned with medical statistics

IVF success prediction (AMH, embryo quality, transfer day)

SHAP-based explainability for clinicians

Dockerized deployment

Cloud hosting

🧑‍💻 Tech Stack

Python

Pandas

CatBoost

Scikit-learn

FastAPI

Streamlit

Uvicorn
