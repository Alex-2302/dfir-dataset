import json
import glob
import os

master = []

for file in glob.glob("*_dataset.json"):

    with open(file) as f:
        data = json.load(f)

    master.extend(data)

    print(f"{file}: {len(data)} alerts")

os.makedirs("../", exist_ok=True)

with open("/home/alex/Documents/Dfir-dataset/full_dataset/alerts_master_dataset.json", "w") as f:
    json.dump(master, f, indent=2)

print()
print("Total alerts:", len(master))