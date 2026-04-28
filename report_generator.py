import time
import random
from datetime import datetime

def fetch_background_data(person_id):
    print(f"Fetching background data for {person_id}...")
    time.sleep(1)

    return {
        "police_record": random.choice(["clear", "record_found"]),
        "government_record": random.choice(["clear", "warning"]),
    }

def generate_qr_code(person_id):
    print("Generating QR code...")
    time.sleep(0.5)
    return f"QR-{person_id}"

def generate_report(person_id, data):
    print("Generating PDF report...")
    time.sleep(1)

    report = {
        "person_id": person_id,
        "date": str(datetime.now()),
        "status": "approved" if data["police_record"] == "clear" else "review",
        "details": data
    }

    return report

def process_person(person_id):
    data = fetch_background_data(person_id)
    qr = generate_qr_code(person_id)
    report = generate_report(person_id, data)

    print("Report generated:", report)
    print("QR:", qr)
    print("-" * 40)

if __name__ == "__main__":
    for i in range(3):
        process_person(f"ID-{100+i}")
