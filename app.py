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
