import plotly.express as px

def plot_avg_delay_airline(df):
    if "carrier_name" not in df.columns or "arr_delay" not in df.columns:
        return None
    avg_delay = df.groupby("carrier_name")["arr_delay"].mean().reset_index()
    return px.bar(avg_delay, x="carrier_name", y="arr_delay",
                  title="Average Arrival Delay by Airline (Minutes)",
                  color="arr_delay")

def plot_monthly_trend(df):
    if "year" not in df.columns or "month" not in df.columns:
        return None
    df["year_month"] = df["year"].astype(str) + "-" + df["month"].astype(str)
    monthly = df.groupby("year_month")["arr_delay"].mean().reset_index()
    return px.line(monthly, x="year_month", y="arr_delay",
                   title="Monthly Average Arrival Delay Trend")

def plot_cancellation_by_airline(df):
    if "carrier_name" not in df.columns or "arr_cancelled" not in df.columns or "arr_flights" not in df.columns:
        return None
    cancel = df.groupby("carrier_name")[["arr_cancelled", "arr_flights"]].sum().reset_index()
    cancel["cancel_rate"] = (cancel["arr_cancelled"] / cancel["arr_flights"]) * 100
    return px.bar(cancel, x="carrier_name", y="cancel_rate",
                  title="Cancellation Rate by Airline (%)",
                  color="cancel_rate")

def plot_airport_performance(df):
    if "airport_name" not in df.columns or "arr_delay" not in df.columns:
        return None
    airport_delays = df.groupby("airport_name")["arr_delay"].mean().reset_index().sort_values(by="arr_delay", ascending=False).head(15)
    return px.bar(airport_delays, x="airport_name", y="arr_delay",
                  title="Top 15 Airports by Average Arrival Delay",
                  color="arr_delay")
