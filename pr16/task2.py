import json
from datetime import date
from pathlib import Path

NAME = "Nazar Mischuk IT-32"

BASE = Path(__file__).parent
SOURCE = BASE / "data" / "expenses.json"
TARGET = BASE / "data" / "expenses_updated.json"


def main():
    print(NAME)

    with open(SOURCE, encoding="utf-8") as file:
        records = json.load(file)

    new_record = {
        "date": date.today().isoformat(),
        "category": "study",
        "amount": 45.0,
        "comment": "lab 36 notebook",
    }
    records.append(new_record)
    added = 1

    before = len(records)
    records = [r for r in records if r["amount"] >= 10]
    removed = before - len(records)

    with open(TARGET, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)

    print(f"added: {added}")
    print(f"removed: {removed}")
    print(f"saved: data/expenses_updated.json ({len(records)} records)")


if __name__ == "__main__":
    main()
