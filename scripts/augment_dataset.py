import pandas as pd
import random

df = pd.read_csv("data/processed/master_dataset.csv")

augmented = []

ips = [
    "10.0.0.5",
    "192.168.1.10",
    "172.16.0.15",
    "10.10.10.20",
]

hosts = [
    "web01",
    "dc01",
    "srv-db",
    "workstation-22",
]

users = [
    "admin",
    "administrator",
    "svc_backup",
    "john",
]

for _, row in df.iterrows():
    augmented.append(row.to_dict())

    for i in range(5):
        text = row["alert_text"]

        text += f" from {random.choice(ips)}"
        text += f" targeting {random.choice(hosts)}"
        text += f" user {random.choice(users)}"

        new_row = row.copy()
        new_row["alert_text"] = text

        augmented.append(new_row.to_dict())

out = pd.DataFrame(augmented)

out.to_csv(
    "data/processed/augmented_dataset.csv",
    index=False
)

print(f"Generated {len(out)} alerts")