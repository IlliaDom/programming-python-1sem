import json
from datetime import date
from pathlib import Path

print("Oleksandr Romaniuk, IT-31")

old_json_file = Path("data/expenses.json")
new_json_file = Path("data/expenses_updated.json")

expenses = []

with open(old_json_file, "r", encoding="utf-8") as f:
    expenses = json.load(f)

new_data = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 74.00,
    "comment": "tomato"
}



new_expenses = []

new_expenses.append(new_data)

for record in expenses:
    if record["amount"] < 10:
        continue

    new_expenses.append(record)

with open(new_json_file, "w", encoding="utf-8") as f:
    json.dump(new_expenses, f)

print(f"added {0 if len(new_expenses) - len(expenses) < 0 else len(new_expenses) - len(expenses)}, deleted {0 if len(expenses) - len(new_expenses) < 0 else len(expenses) - len(new_expenses)}")