import json
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent
print("Anatolii Kurotych, PZ-11")

with (BASE / "data/expenses.json").open(encoding="utf-8") as file:
    records = json.load(file)

records.append({
    "date": date.today().isoformat(),
    "category": "other",
    "amount": 25.0,
    "comment": "Test record for JSON practice"
})
before = len(records)
records = [item for item in records if float(item["amount"]) >= 10]
deleted = before - len(records)

target = BASE / "data/expenses_updated.json"
with target.open("w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print("added: 1")
print(f"deleted: {deleted}")
print(f"saved: data/expenses_updated.json ({len(records)} records)")
