import streamlit as st
import requests

st.set_page_config(
    page_title="Fertility Diagnosis Predictor",
    layout="centered"
)

st.title("🧬 Fertility Diagnosis Prediction")
st.write("Educational ML application (not a medical tool)")

st.markdown("---")

# ---------------- INPUTS ---------------- #

season = st.selectbox(
    "Season",
    ["winter", "spring", "summer", "fall"]
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=60,
    value=30
)

childish_diseases = st.selectbox(
    "Childhood Diseases",
    ["yes", "no"]
)

accident_trauma = st.selectbox(
    "Accident or Serious Trauma",
    ["yes", "no"]
)

surgical_intervention = st.selectbox(
    "Surgical Intervention",
    ["yes", "no"]
)

high_fever = st.selectbox(
    "High Fevers in the Last Year",
    ["yes", "no"]
)

alcohol_freq = st.selectbox(
    "Frequency of Alcohol Consumption",
    ["never", "hardly ever", "once a week", "daily", "twice a day"]
)

smoking = st.selectbox(
    "Smoking Habit",
    ["yes", "no"]
)

sitting_hours = st.number_input(
    "Hours Spent Sitting Per Day",
    min_value=0,
    max_value=16,
    value=6
)

st.markdown("---")

# ---------------- PREDICTION ---------------- #

if st.button("Predict Fertility Diagnosis"):
    payload = {
        "Season": season,
        "Age": age,
        "Childish_diseases": childish_diseases,
        "Accident_or_serious_trauma": accident_trauma,
        "Surgical_intervention": surgical_intervention,
        "High_fevers_in_the_last_year": high_fever,
        "Frequency_of_alcohol_consumption": alcohol_freq,
        "Smoking_habit": smoking,
        "Number_of_hours_spent_sitting_per_day": sitting_hours
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success(f"Prediction: **{result['prediction']}**")
            st.info(f"Confidence: {result['confidence']}")
            st.warning(result["disclaimer"])

        else:
            st.error("API error. Please try again.")

    except Exception as e:
        st.error("FastAPI server is not running.")

