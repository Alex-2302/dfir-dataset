import json
import random
from datetime import datetime, timedelta

HOSTS = [
    "WIN-DC01",
    "WIN-FS01",
    "WIN-FS02",
    "WIN-WKS01",
    "WIN-WKS02",
    "SRV-APP01",
    "SRV-DB01"
]

STATUSES = [
    "Open",
    "Investigating",
    "Resolved"
]

def random_ip():
    return f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def random_timestamp():
    start = datetime(2026,1,1)
    end = datetime(2026,12,31)

    diff = end - start

    return (
        start +
        timedelta(seconds=random.randint(0, int(diff.total_seconds())))
    ).isoformat()

with open("final/templates/alerts_lateral_movement.json") as f:
    templates = json.load(f)

dataset = []

counter = 1

for alert in templates:

    count = random.randint(50,150)

    for _ in range(count):

      record = dict(alert)

      record["id"] = f"ALT-{counter:06d}"

      record["timestamp"] = random_timestamp()

      record["hostname"] = random.choice(HOSTS)

      record["source_ip"] = random_ip()

      record["destination_ip"] = random_ip()
 
      record["confidence"] = random.randint(70,100)

      record["status"] = random.choice(STATUSES)

      dataset.append(record)

    counter += 1

with open(
    "final/generated/lateral_movement_dataset.json",
    "w"
) as f:
    json.dump(dataset, f, indent=2)