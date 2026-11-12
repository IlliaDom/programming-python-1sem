import csv, json
from pathlib import Path

BASE = Path(__file__).resolve().parent
print("Anatolii Kurotych, PZ-11")
records = []

with (BASE / "data/expenses.csv").open(encoding="utf-8", newline="") as file:
    for row in csv.reader(file, delimiter=";"):
        if not row or not row[0].strip() or row[0].lstrip().startswith("#"):
            continue
        if len(row) >= 4:
            records.append({
                "date": row[0].strip(),
                "category": row[1].strip(),
                "amount": float(row[2].strip()),
                "comment": ";".join(row[3:]).strip()
            })

target = BASE / "data/expenses.json"
with target.open("w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"records: {len(records)}")
print(f"saved: data/expenses.json ({target.stat().st_size} bytes)")
