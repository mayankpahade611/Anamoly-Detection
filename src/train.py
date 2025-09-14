import joblib
from xgboost import XGBClassifier
from src.features import select_features
from src.data_pipeline import load_data, preprocess_data
import os

def train_model(df, model_path="models/xgb_model.pkl"):
    X = select_features(df)
    y = df["anomaly"]

    model = XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05,
        random_state=42
    )
    model.fit(X, y)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model saved at {model_path}")
    return model


if __name__ == "__main__":
    # 1. Load and preprocess data
    df = load_data("BTCUSDT_with_anomalies.csv")
    df = preprocess_data(df)

    # 2. Train and save model
    train_model(df)
