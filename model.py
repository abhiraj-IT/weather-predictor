import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import modelbit

# Load model and label encoder
model = joblib.load("weather_model.pkl")
le = joblib.load("label_encoder.pkl")

# Prediction function for Modelbit
def predict_weather(temperature: float, humidity: float, wind: float) -> str:
    input_data = [[temperature, humidity, wind]]
    prediction = model.predict(input_data)
    return le.inverse_transform(prediction)[0]

# Deploy to Modelbit
mb = modelbit.login()

@mb.deploy(name="weather_api")
def weather_api(temperature: float, humidity: float, wind: float) -> str:
    return predict_weather(temperature, humidity, wind)

print("✅ Model deployed to Modelbit!")
