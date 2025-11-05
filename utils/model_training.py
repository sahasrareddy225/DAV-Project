import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(file_path):
    df = pd.read_csv(file_path)

    # Clean column names (remove spaces, lowercase)
    df.columns = df.columns.str.strip().str.lower()

    # Debug print (optional)
    print("📋 Columns in dataset:", list(df.columns))

    required_cols = ["arr_delay", "carrier_delay", "weather_delay", "nas_delay", "late_aircraft_delay"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise KeyError(f"❌ Missing required columns: {missing}")

    df = df.dropna(subset=required_cols)
    df["delay_flag"] = (df["arr_delay"] > 15).astype(int)
    return df


def train_model(df):
    features = ["carrier_delay", "weather_delay", "nas_delay", "security_delay", "late_aircraft_delay"]
    target = "delay_flag"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model trained successfully with accuracy: {acc:.2f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")
    print("💾 Model saved to models/model.pkl")


if __name__ == "__main__":
    file_path = "data/flight_data.csv"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found at: {file_path}")

    df = load_data(file_path)
    train_model(df)
