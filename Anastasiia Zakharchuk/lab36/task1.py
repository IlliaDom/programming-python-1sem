import json
import os

print("Anastasia Zakharchuk, IT-32")

records = []
with open("data/expenses.csv", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        date, category, amount, comment = line.split(";")
        records.append({
            "date": date,
            "category": category,
            "amount": float(amount),
            "comment": comment,
        })

with open("data/expenses.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)

print("records:", len(records))
print(f"saved: data/expenses.json ({os.path.getsize('data/expenses.json')} bytes)")
