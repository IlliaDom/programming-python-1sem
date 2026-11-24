import json
from datetime import date
from pathlib import Path
expenses_json_path = Path(__file__).resolve().parent / "data" / "expenses.json"
expenses_json_updated_path = Path(__file__).resolve().parent /"data" / "expenses_updated.json"
with open(expenses_json_path, "r", encoding="utf-8") as f:
    expenses = json.load(f)
print(expenses)
expenses.append({'date': date.today().isoformat(), 'category': 'Coffee', 'amount': 95.0, 'comment': 'Кава'})
count = 0
expenses_updated = []

for expense in expenses:
    if expense["amount"] >= 10:
        expenses_updated.append(expense)
    else:
        count += 1
print(expenses_updated)

with open(expenses_json_updated_path, "w", encoding="utf-8") as updated:
    json.dump(expenses_updated, updated, ensure_ascii=False, indent=2)
print("Deleted:",count)
print("Added: 1")