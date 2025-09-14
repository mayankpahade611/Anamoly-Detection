import os
import zipfile
import pandas as pd

# Folder where your downloaded .zip files are stored
data = "data"

# Empty list to collect DataFrames
dfs = []

# Loop through all zip files in folder
for file in sorted(os.listdir(data)):
    if file.endswith(".zip"):
        zip_path = os.path.join(data, file)
        print(f"Extracting {file}...")

        # Unzip
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data)

        # Binance files have same name as zip but .csv
        csv_file = file.replace(".zip", ".csv")
        csv_path = os.path.join(data, csv_file)

        # Load CSV into DataFrame
        df = pd.read_csv(csv_path, header=None)
        df.columns = [
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "num_trades",
            "taker_buy_base", "taker_buy_quote", "ignore"
        ]

        # Convert timestamp
        try:
        # If numbers (epoch in ms)
            df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
        except Exception:
    # If already a string date
            df["open_time"] = pd.to_datetime(df["open_time"])

        df.set_index("open_time", inplace=True)

        # Keep only useful columns
        df = df[["open","high","low","close","volume"]].astype(float)

        dfs.append(df)

# Merge all into one DataFrame
merged_df = pd.concat(dfs).sort_index()

print("Final shape:", merged_df.shape)
print(merged_df.head())

# Save to one big CSV
merged_df.to_csv("BTCUSDT_1m_merged.csv")
print("Saved merged dataset ✅")
