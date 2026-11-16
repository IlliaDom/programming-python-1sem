import csv
import json
import os

print("Nikita Krilovets, IT-31")

records = []

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    reader.fieldnames = [name.lstrip("# ").strip() for name in reader.fieldnames]

    for row in reader:
        records.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["description"]
        })

with open("data/expenses.json", "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

size = os.path.getsize("data/expenses.json")

print(f"records: {len(records)}")
print(f"saved: data/expenses.json ({size} bytes)")
