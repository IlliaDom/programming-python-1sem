import csv
import json
from pathlib import Path

print("Maria Vovk, І-23")

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "data" / "expenses.csv"
json_path = BASE_DIR / "data" / "expenses.json"

records = []
with csv_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        records.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row.get("comment") or row.get("note", "")
        })

with json_path.open("w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

size = json_path.stat().st_size
print(f"records: {len(records)}")
print(f"saved: data/expenses.json ({size} bytes)")
