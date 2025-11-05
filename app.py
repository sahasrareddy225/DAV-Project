import streamlit as st
from utils.preprocessing import load_and_clean_data

st.set_page_config(
    page_title="✈️ Airline On-Time Performance",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("✈️ Airline On-Time Performance Dashboard")

st.markdown("""
Welcome to the **Data Analytics and Visualization Project** on Airline On-Time Performance.  
Use the sidebar to explore detailed insights and analytics.
""")

st.sidebar.header("Dataset Information")

file_path = "data/flight_data.csv"
df = load_and_clean_data(file_path)

st.success("✅ Data Loaded Successfully!")
st.write("### Dataset Snapshot")
st.dataframe(df.head(10))

st.write("**Shape:**", df.shape)
st.write("**Columns:**", list(df.columns))

st.markdown("---")
st.write("Use the navigation menu on the left to explore analytics:")
st.markdown("""
- 📊 **Average Delays** – Analyze delay patterns per airline  
- ❌ **Cancellations** – Explore cancellation causes  
- 🛫 **Airport Performance** – Compare airports’ delay rates  
""")

st.info("💡 Tip: Use the sidebar filters to refine your analysis.")

import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Flight Delay Predictor", layout="centered")

st.title("✈️ Flight Delay Predictor")

MODEL_PATH = "models/model.pkl"

# Load model
if not os.path.exists(MODEL_PATH):
    st.error("⚠️ Model not found! Please train it first by running: `python -m utils.model_training`")
    st.stop()

model = joblib.load(MODEL_PATH)

# Collect user input
st.header("Enter Flight Delay Factors")

carrier_delay = st.number_input("Carrier Delay (minutes)", min_value=0.0, max_value=1000.0, value=10.0)
weather_delay = st.number_input("Weather Delay (minutes)", min_value=0.0, max_value=1000.0, value=5.0)
nas_delay = st.number_input("NAS Delay (minutes)", min_value=0.0, max_value=1000.0, value=3.0)
security_delay = st.number_input("Security Delay (minutes)", min_value=0.0, max_value=1000.0, value=0.0)
late_aircraft_delay = st.number_input("Late Aircraft Delay (minutes)", min_value=0.0, max_value=1000.0, value=7.0)

if st.button("🔍 Predict Delay"):
    # Prepare data for prediction
    input_data = pd.DataFrame({
        "carrier_delay": [carrier_delay],
        "weather_delay": [weather_delay],
        "nas_delay": [nas_delay],
        "security_delay": [security_delay],
        "late_aircraft_delay": [late_aircraft_delay]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🛑 Prediction: The flight is likely to be **Delayed** ✈️")
    else:
        st.success("✅ Prediction: The flight is **On Time** 🕒")
