import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model 
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("📱 House Price Predictor")
st.write("Fill in the details below to estimate the house price:")

# Input
area = st.number_input("Area (in sq.ft)", value=1000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=1)
stories = st.number_input("Number of Stories", min_value=1, max_value=4, value=1)
basement = st.selectbox("Basement", ["No", "Yes"])
parking = st.selectbox("Parking", ["No", "Yes"])

# Encode categorical inputs
basement = 1 if basement == "Yes" else 0
parking = 1 if parking == "Yes" else 0

# Predict
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms, stories, basement, parking ]])
    
    prediction = model.predict(input_data)[0]
    formatted_price = f"₹ {prediction:,.2f}"
    st.success(f"Estimated House Price: {formatted_price}")