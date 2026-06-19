# Gathering Requirements

import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/house_model.pkl")

st.title("Real Estate Price Predictor")

bhk = st.number_input("BHK")

size = st.number_input("Size in SqFt")

floor = st.number_input("Floor Number")

schools = st.number_input("Nearby Schools")

hospitals = st.number_input("Nearby Hospitals")

age = st.number_input("Property Age")

furnished = st.selectbox(
    "Furnished Status",
    ["Unfurnished", "Semi-furnished", "Furnished"]
)

transport = st.selectbox(
    "Public Transport",
    ["Low", "Medium", "High"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Independent House", "Villa"]
)

parking = st.selectbox(
    "Parking Space",
    ["No", "Yes"]
)

security = st.selectbox(
    "Security",
    ["No", "Yes"]
)

if st.button("Predict"):

    data = pd.DataFrame({
        "BHK": [bhk],
        "Size_in_SqFt": [size],
        #"Price_per_SqFt": [price_per_sqft],  
        "Floor_No": [floor],
        "Nearby_Schools": [schools],
        "Nearby_Hospitals": [hospitals],
        "Age": [age],
        "Furnished": [furnished],
        "Public_Transport": [transport],
        "Property_Type_Independent House": [property_type],
        # "Property_Type_Villa": [property_villa],
        "Parking_Space_Yes": [parking],
        "Security_Yes": [security]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Price: ₹ {prediction[0]:.2f} Lakhs")

