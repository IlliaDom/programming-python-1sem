import json
from pathlib import Path
from datetime import date

print("Karina Pikul, IT-32")

BASE_DIR = Path(__file__).parent
JSON_FILE = BASE_DIR / "data" / "expenses.json"
UPDATED_FILE = BASE_DIR / "data" / "expenses_updated.json"

with open(JSON_FILE, "r", encoding="utf-8") as file:
    expenses = json.load(file)

new_expense = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 50.0,
    "comment": "lunch"
}

expenses.append(new_expense)

expenses_before = len(expenses)

expenses = [
    expense for expense in expenses
    if expense["amount"] >= 10
]

deleted_count = expenses_before - len(expenses)

with open(UPDATED_FILE, "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=2, ensure_ascii=False)

print("Додано записів: 1")
print(f"Видалено записів: {deleted_count}")
print(f"Залишилося записів: {len(expenses)}")
print(f"Оновлений файл: {UPDATED_FILE}")
