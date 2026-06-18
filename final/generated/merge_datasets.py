import json
import glob
import os

master = []

for file in glob.glob("*_dataset.json"):
    with open(file) as f:
        data = json.load(f)

    master.extend(data)
    print(f"{file}: {len(data)} alerts")

os.makedirs("../../full-dataset", exist_ok=True)

with open("../../full-dataset/alerts_master_dataset.json", "w") as f:
    json.dump(master, f, indent=2)

print(f"\nTotal alerts: {len(master)}")
