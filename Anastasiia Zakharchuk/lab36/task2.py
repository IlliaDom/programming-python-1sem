import json
from datetime import date

print("Anastasia Zakharchuk, IT-32")

with open("data/expenses.json", encoding="utf-8") as f:
    records = json.load(f)

new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 75.0,
    "comment": "new record",
}
records.append(new_record)
added = 1

before = len(records)
records = [r for r in records if r["amount"] >= 10]
removed = before - len(records)

with open("data/expenses_updated.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)

print("added:", added)
print("removed:", removed)
print("saved: data/expenses_updated.json")
