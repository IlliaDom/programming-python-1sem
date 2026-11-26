import json
from datetime import date

print("Лещук Ірина, IT-31")

input_file = "data/expenses.json"
output_file = "data/expenses_updated.json"

with open(input_file, "r", encoding="utf-8") as file:
    records = json.load(file)

new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 120.0,
    "comment": "lunch"
}

records.append(new_record)
added = 1

old_count = len(records)

records = [record for record in records if record["amount"] >= 10]

deleted = old_count - len(records)

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"added: {added}")
print(f"deleted: {deleted}")
print(f"saved: {output_file}")