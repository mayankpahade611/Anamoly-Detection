from src.data_pipeline import load_data, preprocess_data
from src.train import train_model
from src.evaluate import evaluate_model
from src.features import select_features

# Load + preprocess
df = load_data("BTCUSDT_1m_merged.csv")
df = preprocess_data(df)

# Train
model = train_model(df)

# Evaluate
X = select_features(df)
y = df["anomaly"]
evaluate_model(model, X, y)
