# 🌦️ Weather Predictor App (Modelbit + Streamlit)

This app predicts whether it will rain or not based on temperature, humidity, and wind speed. It uses a machine learning model deployed on Modelbit and interacts through a user-friendly Streamlit interface.

## 🚀 Features

- 🧠 Machine Learning model with scikit-learn
- ☁️ Deployment via Modelbit API
- 🎛️ User input form using Streamlit
- 🔐 Secure API key handling via Streamlit secrets

## 🧾 Requirements

```bash
pip install -r requirements.txt
```

## 🛠️ Setup Instructions

1. Clone the repo
```bash
git clone https://github.com/your-username/weather-predictor.git
cd weather-predictor
```

2. Modelbit Setup
- Upload weather_model.pkl and label_encoder.pkl
- Deploy model.py with:
```python
import modelbit
mb = modelbit.login()
mb.deploy(weather_api)
```

3. Streamlit Setup
- Add your API_KEY to .streamlit/secrets.toml

4. Run Streamlit app
```bash
streamlit run app.py
```

## 📂 Project Structure

```
weather-predictor/
├── app.py
├── model.py
├── weather_model.pkl
├── label_encoder.pkl
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
└── README.md
```
