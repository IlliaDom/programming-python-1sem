import csv
import json
import os

print("Vlad Kudryk, IT-32")

records = []
with open("data/expenses.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        records.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["comment"],
        })

with open("data/expenses.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)

print("records:", len(records))
print("saved: data/expenses.json (" + str(os.path.getsize("data/expenses.json")) + " bytes)")