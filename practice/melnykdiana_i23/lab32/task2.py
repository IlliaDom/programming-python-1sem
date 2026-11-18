import csv
import sys
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from datetime import datetime
from pathlib import Path

from tabulate import tabulate

NAME = "Diana Melnyk"
GROUP = "I-23"


def main():
    print(f"{NAME}, {GROUP}")
    csv_path = Path(__file__).parent / "data" / "expenses.csv"
    totals = defaultdict(Decimal)
    counts = defaultdict(int)

    try:
        with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
            lines = (line for line in file if line.strip() and not line.lstrip().startswith("#"))
            reader = csv.DictReader(lines)
            for line_number, row in enumerate(reader, start=2):
                try:
                    category = (row.get("category") or "").strip()
                    datetime.strptime((row.get("date") or "").strip(), "%Y-%m-%d")
                    amount = Decimal((row.get("amount") or "").strip())
                    if not category or amount <= 0:
                        raise ValueError("порожня категорія або сума не більша за нуль")
                    totals[category] += amount
                    counts[category] += 1
                except (InvalidOperation, ValueError, AttributeError) as error:
                    print(f"warning: рядок {line_number} пропущено: {error}", file=sys.stderr)
    except FileNotFoundError:
        print(f"error: файл не знайдено: {csv_path}", file=sys.stderr)
        raise SystemExit(1)

    rows = [
        [category, counts[category], f"{totals[category]:.2f}"]
        for category in sorted(totals)
    ]
    grand_total = sum(totals.values(), Decimal("0.00"))
    rows.append(["TOTAL", sum(counts.values()), f"{grand_total:.2f}"])
    print(tabulate(rows, headers=["category", "count", "total"], tablefmt="github", colalign=("left", "right", "right")))


if __name__ == "__main__":
    main()
