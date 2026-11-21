import sys
from datetime import date
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"
LIMIT = 100.0      


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return (f"{self.date:%d.%m.%Y} {self.category} "
                f"{self.amount:.2f} ({self.comment})")


def load_expenses(path):
    expenses = []
    with path.open(encoding="utf-8-sig") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            try:
                if len(parts) != 4:
                    raise ValueError("expected 4 fields")
                expenses.append(Expense(
                    date.fromisoformat(parts[0].strip()),
                    parts[1].strip(),
                    float(parts[2].strip()),
                    parts[3].strip()))
            except ValueError as e:
                print(f"warning: line {number} skipped ({e}): {line}",
                      file=sys.stderr)
    return expenses


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)
    expenses = load_expenses(DATA_FILE)
    print(f"expenses: {len(expenses)}")
    print(f"big expenses (> {LIMIT:.2f}):")
    for e in expenses:
        if e.is_big(LIMIT):
            print("  " + e.describe())


if __name__ == "__main__":
    main()
