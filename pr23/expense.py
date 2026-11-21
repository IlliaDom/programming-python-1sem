"""Клас Expense з роботи 46 (спрощений) і завантаження з CSV."""
import sys
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "data" / "expenses.csv"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(";")
        if len(parts) != 4:
            raise ValueError(f"expected 4 fields, got {len(parts)}")
        date, category, amount, comment = (p.strip() for p in parts)
        datetime.strptime(date, "%Y-%m-%d")     # ValueError для поганої дати
        return cls(date, category, float(amount), comment)


def load_expenses(path=DATA_FILE):
    expenses = []
    with Path(path).open(encoding="utf-8-sig") as f:
        for number, line in enumerate(f, start=1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            try:
                expenses.append(Expense.from_csv_line(line))
            except ValueError as e:
                print(f"warning: line {number} skipped ({e}): {line.strip()}",
                      file=sys.stderr)
    return expenses
