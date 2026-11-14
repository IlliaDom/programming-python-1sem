import json
from pathlib import Path

print("Oleksandr Romaniuk, IT-31")

file = Path("data/expenses.csv")

json_file = Path("data/expenses.json")

changed_csv = []

with open(file, "r", encoding="utf-8") as f:
    for line in f.readlines():
        if line.startswith("#") or line == "":
            continue

        date, category, amount, note = line.strip().split(";")

        record = {
            "date": date,
            "category": category,
            "amount": float(amount),
            "comment": note
        }

        changed_csv.append(record)


with open(json_file, "w", encoding="utf-8") as f:
    json.dump(changed_csv, f, indent=2, ensure_ascii=False)

print(f"records: {len(changed_csv)}")
print(f"saved: data/expenses.json ({json_file.stat().st_size} bytes)")