from fastapi import FastAPI
from pydantic import BaseModel
from catboost import CatBoostClassifier
import pandas as pd

# Initialize FastAPI
app = FastAPI(
    title="Fertility Diagnosis Prediction API",
    description="Educational healthcare ML model using CatBoost",
    version="1.0"
)

# Load model
model = CatBoostClassifier()
model.load_model("model/catboost_fertility_model.cbm")

# Input schema
class FertilityInput(BaseModel):
    Season: str
    Age: int
    Childish_diseases: str
    Accident_or_serious_trauma: str
    Surgical_intervention: str
    High_fevers_in_the_last_year: str
    Frequency_of_alcohol_consumption: str
    Smoking_habit: str
    Number_of_hours_spent_sitting_per_day: int


@app.get("/")
def home():
    return {
        "message": "Fertility Diagnosis Prediction API",
        "note": "This is for educational purposes only"
    }


@app.post("/predict")
def predict_fertility(data: FertilityInput):

    df = pd.DataFrame([{
        "Season": data.Season,
        "Age": data.Age,
        "Childish diseases": data.Childish_diseases,
        "Accident or serious trauma": data.Accident_or_serious_trauma,
        "Surgical intervention": data.Surgical_intervention,
        "High fevers in the last year": data.High_fevers_in_the_last_year,
        "Frequency of alcohol consumption": data.Frequency_of_alcohol_consumption,
        "Smoking habit": data.Smoking_habit,
        "Number of hours spent sitting per day": data.Number_of_hours_spent_sitting_per_day
    }])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df).max()

    return {
        "prediction": prediction,
        "confidence": round(float(probability), 3),
        "disclaimer": "Not a medical diagnostic tool"
    }
