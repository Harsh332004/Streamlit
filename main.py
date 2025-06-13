import streamlit as st
import pandas as pd

# Streamlit UI
st.title("Student Performance Predictor")
st.write("Estimate student performance based on study habits and participation.")

# Input fields
subject = st.selectbox("Subject", ["Math", "Science", "English", "History", "Computer Science"])
study_hours = st.slider("Daily Study Hours", min_value=0, max_value=10, value=2)
attendance = st.slider("Attendance (%)", min_value=0, max_value=100, value=75)
participation = st.selectbox("Class Participation Level", ["Low", "Medium", "High"])

# Rule-based prediction
def predict_performance(hours, attendance, participation_level):
    score = hours * 2 + (attendance / 10)
    
    if participation_level == "Medium":
        score += 5
    elif participation_level == "High":
        score += 10

    if score >= 25:
        return "Excellent"
    elif score >= 15:
        return "Average"
    else:
        return "Poor"

if st.button("Predict Performance"):
    result = predict_performance(study_hours, attendance, participation)
    st.success(f"Predicted Performance: {result}")

# Chart: Score estimate across subjects
st.write("## Subject-wise Score Estimate Chart")
subjects = ["Math", "Science", "English", "History", "Computer Science"]
scores = [
    predict_performance(study_hours, attendance, participation) for _ in subjects
]

# Convert performance to numerical scores for plotting
performance_map = {"Poor": 1, "Average": 2, "Excellent": 3}
scores_numeric = [performance_map.get(p, 0) for p in scores]
df_chart = pd.DataFrame({'Performance Score': scores_numeric}, index=subjects)

st.bar_chart(df_chart)
