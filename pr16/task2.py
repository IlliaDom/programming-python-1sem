import json
import sys
from datetime import date
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

BASE = Path(__file__).resolve().parent
SRC = BASE / "data" / "expenses.json"
DST = BASE / "data" / "expenses_updated.json"

NEW_RECORD = {                      # ваш новий запис (дата підставляється сама)
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 55.0,
    "comment": "added by task2",
}


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not SRC.is_file():
        print(f"error: {SRC} not found, run task1.py first", file=sys.stderr)
        sys.exit(1)

    with SRC.open(encoding="utf-8") as f:
        records = json.load(f)

    records.append(NEW_RECORD)
    added = 1
    before = len(records)
    records = [r for r in records if r["amount"] >= 10]
    removed = before - len(records)

    with DST.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    print(f"added: {added}, removed: {removed}")
    print(f"saved: data/{DST.name} ({len(records)} records)")


if __name__ == "__main__":
    main()
