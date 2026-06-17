import csv

targets = [
    "Microsoft 365",
    "Google Workspace",
    "Okta",
    "VPN Portal",
    "Corporate SSO"
]

roles = [
    "CEO",
    "HR Manager",
    "Finance Director",
    "IT Administrator",
    "Security Analyst"
]

departments = [
    "Finance",
    "HR",
    "Engineering",
    "Operations",
    "Sales"
]

with open("phishing_generated.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["alert", "category"])

    for target in targets:
        writer.writerow([f"Credential harvesting phishing URL detected targeting {target}", "Phishing"])
        writer.writerow([f"Suspicious login portal impersonating {target} detected", "Phishing"])
        writer.writerow([f"Verified phishing domain spoofing {target} detected", "Phishing"])

    for role in roles:
        writer.writerow([f"Email impersonating {role} detected", "Phishing"])
        writer.writerow([f"Business email compromise attempt targeting {role} identified", "Phishing"])

    for dept in departments:
        writer.writerow([f"Malicious attachment delivered to {dept} department", "Phishing"])
        writer.writerow([f"Phishing campaign targeting {dept} users detected", "Phishing"])
        writer.writerow([f"Credential theft email sent to {dept} department", "Phishing"])

print("Done")