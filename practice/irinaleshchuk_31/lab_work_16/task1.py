import csv
import json
import os

print("Лещук Ірина, IT-31")

input_file = "data/expenses.csv"
output_file = "data/expenses.json"

records = []

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        records.append({
            "date": row[0],
            "category": row[1],
            "amount": float(row[2]),
            "comment": row[3]
        })

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

size = os.path.getsize(output_file)

print(f"records: {len(records)}")
print(f"saved: {output_file} ({size} bytes)")