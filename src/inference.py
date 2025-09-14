import joblib
from src.data_pipeline import preprocess_data
from src.features import select_features

def predict_anomaly(df, model_path="models/xgb_model.pkl"):
    """Run inference on new data"""
    model = joblib.load(model_path)
    df = preprocess_data(df)
    X = select_features(df)
    preds = model.predict(X)
    df["pred_anomaly"] = preds
    return df
