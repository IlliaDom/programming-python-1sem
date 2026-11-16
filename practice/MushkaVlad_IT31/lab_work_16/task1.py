import csv
import json
import os

print("Vlad Mushka, IT31")

records = []

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        if not row or row[0].startswith("#"):
            continue

        date, category, amount, comment = row

        records.append({
            "date": date,
            "category": category,
            "amount": float(amount),
            "comment": comment
        })

with open("data/expenses.json", "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

size = os.path.getsize("data/expenses.json")

print(f"records: {len(records)}")
print(f"saved: data/expenses.json ({size} bytes)")