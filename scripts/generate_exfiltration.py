import csv

data_types = [
    "customer records",
    "financial reports",
    "employee data",
    "source code",
    "database backups"
]

destinations = [
    "unknown external host",
    "unauthorized cloud storage",
    "remote FTP server",
    "personal Dropbox account",
    "external file sharing service"
]

protocols = [
    "HTTPS",
    "FTP",
    "SFTP",
    "DNS tunneling",
    "encrypted channel"
]

with open("data_exfiltration_generated.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["alert", "category"])

    for data in data_types:
        writer.writerow([
            f"Large outbound transfer of {data} detected",
            "Data Exfiltration"
        ])

    for dest in destinations:
        writer.writerow([
            f"Sensitive files uploaded to {dest}",
            "Data Exfiltration"
        ])

    for proto in protocols:
        writer.writerow([
            f"Confidential data transferred over {proto}",
            "Data Exfiltration"
        ])

print("Done")
