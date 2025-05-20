import streamlit as st
import requests
import os

# Streamlit page config
st.set_page_config(page_title="🌦️ Weather Predictor", layout="centered")
st.title("🌧️ Weather Prediction: Rain or No Rain")

# Input sliders
temperature = st.number_input("🌡️ Temperature (°C)", min_value=-30.0, max_value=60.0, step=0.1, value=25.0)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, step=0.1, value=60.0)
wind = st.number_input("🌬️ Wind Speed (km/h)", min_value=0.0, max_value=300.0, step=0.1, value=10.0)

# Predict button
if st.button("🔍 Predict Weather"):
    with st.spinner("Calling the ML model on Modelbit..."):
        api_url = "https://bamsrad.us-east-2.aws.modelbit.com/v1/weather_api/latest"

        headers = {
            "Authorization": f"Bearer {st.secrets['miK4/iqEcH:msM9TmRFMKZG0aFJHEMQKyWvzT25HSzLl6LwLVXKf2Y0o=']}",
            "Content-Type": "application/json"
        }

        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "wind": wind
        }

        try:
            response = requests.post(api_url, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            st.success(f"✅ Prediction: **{result}**")
        except Exception as e:
            st.error("❌ Failed to get prediction.")
            st.write(e)
