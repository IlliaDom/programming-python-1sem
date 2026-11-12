import json
from datetime import date
from pathlib import Path

print("Maria Vovk, І-23")

BASE_DIR = Path(__file__).parent
source = BASE_DIR / "data" / "expenses.json"
destination = BASE_DIR / "data" / "expenses_updated.json"

with source.open("r", encoding="utf-8") as file:
    records = json.load(file)

new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 50.0,
    "comment": "особисті витрати"
}
records.append(new_record)
added = 1

before = len(records)
records = [item for item in records if float(item["amount"]) >= 10]
deleted = before - len(records)

with destination.open("w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"added: {added}")
print(f"deleted (amount < 10): {deleted}")
print(f"records after update: {len(records)}")
print("saved: data/expenses_updated.json")
