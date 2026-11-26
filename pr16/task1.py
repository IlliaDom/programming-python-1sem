import json
import os
from pathlib import Path

NAME = "Nazar Mischuk IT-32"

BASE = Path(__file__).parent
CSV_PATH = BASE / "data" / "expenses.csv"
JSON_PATH = BASE / "data" / "expenses.json"


def read_csv(path):
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            date, category, amount, comment = line.split(";")
            records.append(
                {
                    "date": date,
                    "category": category,
                    "amount": float(amount),  
                    "comment": comment,
                }
            )
    return records


def main():
    print(NAME)
    records = read_csv(CSV_PATH)
    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)
    size = os.path.getsize(JSON_PATH)
    print(f"records: {len(records)}")
    print(f"saved: data/expenses.json ({size} bytes)")


if __name__ == "__main__":
    main()
