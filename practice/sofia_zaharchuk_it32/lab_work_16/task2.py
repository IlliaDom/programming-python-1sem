import json
import sys
from datetime import date
from pathlib import Path

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

BASE = Path(__file__).resolve().parent
SRC = BASE / "data" / "expenses.json"
DST = BASE / "data" / "expenses_updated.json"

NEW_RECORD = {
    "date": date.today().isoformat(),
    "category": "coffee",
    "amount": 45.0,
    "comment": "added by task2",
}
MIN_AMOUNT = 10


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    try:
        with SRC.open(encoding="utf-8") as file:
            records = json.load(file)
    except OSError as e:
        sys.exit(f"error: cannot read {SRC}: {e} (run task1.py first)")
    except json.JSONDecodeError as e:
        sys.exit(f"error: {SRC.name} is broken at line {e.lineno}: {e.msg}")

    before = len(records)
    records.append(NEW_RECORD)
    records = [r for r in records if r["amount"] >= MIN_AMOUNT]
    removed = before + 1 - len(records)

    with DST.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)

    print(f"read: {before}, added: 1, removed (amount < {MIN_AMOUNT}): {removed}")
    print(f"saved: data/{DST.name} ({len(records)} records)")


if __name__ == "__main__":
    main()
