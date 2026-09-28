import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("House Price Prediction")

area = st.number_input("Area", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
age = st.number_input("Age", min_value=0, step=1)

if st.button("Predict"):
    input_data = pd.DataFrame(
        [[area, bedrooms, age]],
        columns=["Area", "Bedrooms", "Age"]
    )

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Price: {prediction:.2f}")