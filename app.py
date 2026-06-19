# Gathering Requirements

import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/house_model.pkl")

st.title("Real Estate Price Predictor")

size = st.number_input("Size in Sqft")
bhk = st.number_input("BHK")

if st.button("Predict"):
    data = pd.DataFrame({
        "Size_in_SqFt" : [size],
        "BHK" : [bhk]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Price : $ {prediction[0]:.2f} Lakhs")

