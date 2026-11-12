import json
from datetime import date

print("Vlad Kudryk, IT-32")

with open("data/expenses.json", encoding="utf-8") as f:
    data = json.load(f)

new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 100.0,
    "comment": "new record",
}
data.append(new_record)
added = 1

count_before = len(data)
data = [r for r in data if r["amount"] >= 10]
removed = count_before - len(data)

with open("data/expenses_updated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("added:", added)
print("removed:", removed)