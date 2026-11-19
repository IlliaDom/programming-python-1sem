import sys
from pathlib import Path

from tabulate import tabulate

# --- ВАШІ ДАНІ: замініть на справжні ---
NAME = "Ivan"
SURNAME = "Petrenko"
GROUP = "PZ-11"

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    stats = {}  # category -> [count, total]
    with DATA_FILE.open(encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            try:
                category = parts[1].strip()
                amount = float(parts[2].strip())
            except (IndexError, ValueError):
                print(f"warning: line {number} skipped: {line}",
                      file=sys.stderr)
                continue
            entry = stats.setdefault(category, [0, 0.0])
            entry[0] += 1
            entry[1] += amount

    if not stats:
        print("error: no valid expenses", file=sys.stderr)
        sys.exit(1)

    rows = [[cat, count, total] for cat, (count, total) in stats.items()]
    rows.append(["TOTAL",
                 sum(c for c, _ in stats.values()),
                 sum(t for _, t in stats.values())])
    print(tabulate(rows, headers=["category", "count", "total"],
                   tablefmt="github", floatfmt=".2f"))


if __name__ == "__main__":
    main()
