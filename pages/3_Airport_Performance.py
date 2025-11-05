import streamlit as st
from utils.preprocessing import load_and_clean_data
from utils.visuals import plot_airport_performance

st.title("🛫 Airport Performance Insights")

file_path = "data/flight_data.csv"
df = load_and_clean_data(file_path)

st.plotly_chart(plot_airport_performance(df), use_container_width=True)
