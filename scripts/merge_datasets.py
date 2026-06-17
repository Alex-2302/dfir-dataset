import pandas as pd
from pathlib import Path

raw_dir = Path("data/raw")

all_data = []

for file in raw_dir.glob("*.csv"):
    df = pd.read_csv(file)
    all_data.append(df)

merged = pd.concat(all_data, ignore_index=True)

merged.insert(0, "id", range(1, len(merged) + 1))

merged.to_csv(
    "data/processed/master_dataset.csv",
    index=False
)

print(f"Saved {len(merged)} records to data/processed/master_dataset.csv")