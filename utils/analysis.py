def average_delay_by_airline(df):
    if "carrier_name" in df.columns and "arr_delay" in df.columns:
        return df.groupby("carrier_name")["arr_delay"].mean().sort_values()
    return None

def monthly_delay_trend(df):
    if "year" in df.columns and "month" in df.columns and "arr_delay" in df.columns:
        df["year_month"] = df["year"].astype(str) + "-" + df["month"].astype(str)
        return df.groupby("year_month")["arr_delay"].mean().reset_index()
    return None

def cancellation_rate(df):
    if "arr_cancelled" in df.columns and "arr_flights" in df.columns:
        return (df["arr_cancelled"].sum() / df["arr_flights"].sum()) * 100
    return None

def busiest_airports(df):
    if "airport_name" in df.columns:
        return df["airport_name"].value_counts().head(10)
    return None
