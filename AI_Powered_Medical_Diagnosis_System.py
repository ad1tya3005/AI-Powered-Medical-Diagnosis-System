import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Disease Rules
disease_rules = {
    "Diabetes": {"Fasting_Blood_Sugar": 126, "Glucose_Level": 200},
    "Hypertension": {"Systolic_BP": 140, "Diastolic_BP": 90},
    "Heart Disease": {"Cholesterol": 240, "Blood_Pressure": 130},
    "Anemia": {"Hemoglobin": 12},
    "Kidney Disease": {"Creatinine": 1.5},
}

st.title("AI-Powered Medical Diagnosis System")
st.write("### Enter Your Symptoms & Test Results")

user_data = {}
for condition, thresholds in disease_rules.items():
    for parameter, _ in thresholds.items():
        if parameter not in user_data:
            user_data[parameter] = st.number_input(f"{parameter.replace('_', ' ')}", min_value=0.0, max_value=300.0, value=50.0)

if st.button("Predict Disease"):
    predictions = []
    for disease, thresholds in disease_rules.items():
        match = all(user_data[param] >= value for param, value in thresholds.items())
        if match:
            predictions.append(disease)
    
    if predictions:
        st.write("### Possible Diagnoses:")
        for disease in predictions:
            st.write(f"- *{disease.replace('_', ' ')}*")
    else:
        st.write("No strong matches found. Consult a doctor for further analysis.")

    fig, ax = plt.subplots()
    sns.barplot(x=list(user_data.keys()), y=list(user_data.values()), ax=ax)
    ax.set_ylabel("Measured Values")
    ax.set_title("User Input Data")
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.write("This is a basic diagnostic tool. Always consult a medical professional for accurate results.")