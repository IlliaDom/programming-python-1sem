# Task 2: expenses table with tabulate
from pathlib import Path

from tabulate import tabulate

NAME = "Anastasia Zakharchuk"
GROUP = "IT-32"
FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"


def read_expenses(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            date, category, amount, note = line.split(";", 3)
            records.append((category, float(amount)))
    return records


def main():
    print(f"{NAME}, {GROUP}")
    records = read_expenses(FILE)

    totals = {}
    for category, amount in records:
        count, total = totals.get(category, (0, 0))
        totals[category] = (count + 1, total + amount)

    rows = []
    for category, (count, total) in totals.items():
        rows.append([category, count, total])

    all_count = len(records)
    all_total = sum(amount for category, amount in records)
    rows.append(["TOTAL", all_count, all_total])

    print(tabulate(rows, headers=["category", "count", "total"], tablefmt="github", floatfmt=".2f"))


main()