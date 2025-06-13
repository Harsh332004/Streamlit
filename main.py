import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
st.title("Food Delivery Time Estimator")
st.write("Enter order details to predict the expected delivery time for your meal.")

# Input Fields
food_category = st.selectbox("Food Category", ["Pizza", "Burger", "Sushi", "Pasta", "Salad"])  # New categories
customer_city = st.text_input("Customer City (e.g., New York, Mumbai)")
delivery_mode = st.selectbox("Delivery Mode", ["Regular", "Fast", "Ultra-Fast"])  # Changed names

# Rule-based model to predict delivery time
def predict_delivery_time(food_category, delivery_mode):
    base_time = {
        "Pizza": 30,
        "Burger": 20,
        "Sushi": 40,
        "Pasta": 25,
        "Salad": 15
    }
    delivery_modifier = {"Regular": 0, "Fast": -5, "Ultra-Fast": -10}
    
    return max(5, base_time.get(food_category, 25) + delivery_modifier.get(delivery_mode, 0))

if st.button("Predict Delivery Time"):
    prediction = predict_delivery_time(food_category, delivery_mode)
    st.success(f"Estimated Delivery Time: {prediction} minutes")

# Delivery Time Chart
st.write("## Delivery Time Comparison Chart")
delivery_times = {
    category: [predict_delivery_time(category, mode) for mode in ["Regular", "Fast", "Ultra-Fast"]]
    for category in ["Pizza", "Burger", "Sushi", "Pasta", "Salad"]
}
df_chart = pd.DataFrame(delivery_times, index=["Regular", "Fast", "Ultra-Fast"])

st.line_chart(df_chart)
