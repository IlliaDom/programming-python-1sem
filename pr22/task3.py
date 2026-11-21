import sys
from datetime import date
from pathlib import Path

from task1 import GROUP, NAME, SURNAME, Money

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"


class Expense:
    def __init__(self, day, category, amount, comment=""):
        self.date = day
        self.category = category
        self.amount = amount            # Money
        self.comment = comment

    def __str__(self):
        return (f"{self.date:%d.%m.%Y} {self.category} "
                f"{self.amount} ({self.comment})")


class ExpenseBook:
    def __init__(self, expenses=None):
        self.expenses = list(expenses or [])

    def total(self):
        return sum((e.amount for e in self.expenses), Money(0))

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(e.category == category for e in self.expenses)

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses)

    def __str__(self):
        categories = sorted({e.category for e in self.expenses})
        return (f"ExpenseBook: {len(self)} expenses, "
                f"total {self.total()}, categories: {', '.join(categories)}")

    # ---- порівняння з бюджетом (завдання 4) ----
    def __gt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total() > budget

    def __lt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total() < budget


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
                expenses.append(Expense(date.fromisoformat(parts[0].strip()),
                                        parts[1].strip(),
                                        Money(float(parts[2].strip())),
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
    first = ExpenseBook(e for e in expenses if e.date.day <= 15)
    second = ExpenseBook(e for e in expenses if e.date.day > 15)
    merged = first + second

    print("first half: ", first)
    print("second half:", second)
    print("merged:     ", merged)
    print(f"len: {len(first)} + {len(second)} = {len(merged)}")
    print("'food' in merged:", "food" in merged)
    print("'cinema' in merged:", "cinema" in merged)
    print("merged[0]:", merged[0])
    print("all expenses:")
    for expense in merged:
        print("  ", expense)


if __name__ == "__main__":
    main()
