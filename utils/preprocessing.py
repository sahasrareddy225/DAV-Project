import pandas as pd
import os

def load_and_clean_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found at: {file_path}")

    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()

    # Remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains('unnamed')]

    # Fill missing delay-related values with 0
    delay_cols = [
        "arr_delay", "carrier_delay", "weather_delay",
        "nas_delay", "security_delay", "late_aircraft_delay"
    ]
    for col in delay_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Calculate % of delayed flights if arr_flights > 0
    if "arr_del15" in df.columns and "arr_flights" in df.columns:
        df["delay_rate"] = (df["arr_del15"] / df["arr_flights"]) * 100

    return df
