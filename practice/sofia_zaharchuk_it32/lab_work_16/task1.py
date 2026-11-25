import json
import sys
from pathlib import Path

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

BASE = Path(__file__).resolve().parent
SRC = BASE / "data" / "expenses.csv"
DST = BASE / "data" / "expenses.json"


def load_csv(path: Path) -> list[dict]:
    """Read date;category;amount;comment, skip comments and empty lines."""
    records = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        sys.exit(f"error: cannot read {path}: {e}")
    for n, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";")
        try:
            records.append({
                "date": parts[0].strip(),
                "category": parts[1].strip(),
                "amount": float(parts[2].replace(",", ".")),
                "comment": parts[3].strip() if len(parts) > 3 else "",
            })
        except (ValueError, IndexError):
            print(f"warning: line {n} skipped: {line!r}", file=sys.stderr)
    return records


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    records = load_csv(SRC)
    with DST.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)
    print(f"records: {len(records)}")
    print(f"saved: data/{DST.name} ({DST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
