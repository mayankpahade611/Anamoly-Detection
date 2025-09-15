import os
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

def save_raw_data(df: pd.DataFrame, filename: str):
    """Save raw dataset in data/raw/"""
    os.makedirs(RAW_DIR, exist_ok=True)
    path = os.path.join(RAW_DIR, filename)
    df.to_csv(path, index=True)
    print(f"Raw data saved at {path}")


def save_processed_data(df: pd.DataFrame, filename: str):
    """Save processed dataset in data/processed/"""
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    path = os.path.join(PROCESSED_DIR, filename)
    df.to_csv(path, index=True)
    print(f"Processed data saved at {path}")


def load_raw_data(filename: str) -> pd.DataFrame:
    """Load raw dataset from data/raw/"""
    path = os.path.join(RAW_DIR, filename)
    return pd.read_csv(path, index_col=0, parse_dates=True)


def load_processed_data(filename: str) -> pd.DataFrame:
    """Load processed dataset from data/processed/"""
    path = os.path.join(PROCESSED_DIR, filename)
    return pd.read_csv(path, index_col=0, parse_dates=True)
