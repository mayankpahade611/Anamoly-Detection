import pandas as pd

def load_data(file_path):
    """Load raw dataset"""
    return pd.read_csv(file_path, index_col=0, parse_dates=True)

def preprocess_data(df, window=60, threshold=3):
    """Preprocess dataset and generate anomaly column"""
    df["returns"] = df["close"].pct_change()
    df["rolling_mean"] = df["returns"].rolling(window).mean()
    df["rolling_std"] = df["returns"].rolling(window).std()
    df["zscore"] = (df["returns"] - df["rolling_mean"]) / df["rolling_std"]
    df["anomaly"] = df["zscore"].apply(lambda x: 1 if abs(x) > threshold else 0)
    return df.dropna()
