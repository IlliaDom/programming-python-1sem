import json
import sys
from pathlib import Path


NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

BASE = Path(__file__).resolve().parent
SRC = BASE / "data" / "expenses.csv"
DST = BASE / "data" / "expenses.json"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not SRC.is_file():
        print(f"error: {SRC} not found", file=sys.stderr)
        sys.exit(1)

    records = []
    with SRC.open(encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            try:
                if len(parts) != 4:
                    raise ValueError("expected 4 fields")
                records.append({
                    "date": parts[0].strip(),
                    "category": parts[1].strip(),
                    "amount": float(parts[2].strip()),
                    "comment": parts[3].strip(),
                })
            except ValueError as e:
                print(f"warning: line {number} skipped ({e}): {line}",
                      file=sys.stderr)

    with DST.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    print(f"records: {len(records)}")
    print(f"saved: data/{DST.name} ({DST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
