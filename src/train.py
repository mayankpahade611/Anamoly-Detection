import joblib
from xgboost import XGBClassifier
from src.features import select_features

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
    joblib.dump(model, model_path)
    return model
