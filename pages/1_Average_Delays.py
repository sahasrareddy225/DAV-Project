import streamlit as st
from utils.preprocessing import load_and_clean_data
from utils.visuals import plot_avg_delay_airline, plot_monthly_trend

st.title("📊 Average Delays Analysis")

file_path = "data/flight_data.csv"
df = load_and_clean_data(file_path)

airlines = df["carrier_name"].dropna().unique().tolist()
selected_airlines = st.sidebar.multiselect("Select Airlines", airlines, default=airlines[:5])

if selected_airlines:
    df = df[df["carrier_name"].isin(selected_airlines)]

st.plotly_chart(plot_avg_delay_airline(df), use_container_width=True)
st.plotly_chart(plot_monthly_trend(df), use_container_width=True)
