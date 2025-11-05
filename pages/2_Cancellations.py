import streamlit as st
from utils.preprocessing import load_and_clean_data
from utils.visuals import plot_cancellation_by_airline

st.title("❌ Flight Cancellations Analysis")

file_path = "data/flight_data.csv"
df = load_and_clean_data(file_path)

st.plotly_chart(plot_cancellation_by_airline(df), use_container_width=True)

st.write("### Cancellation Overview")
cancel_rate = (df["arr_cancelled"].sum() / df["arr_flights"].sum()) * 100
st.metric("Overall Cancellation Rate", f"{cancel_rate:.2f}%")
