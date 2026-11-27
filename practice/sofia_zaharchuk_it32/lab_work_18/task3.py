"""Lab 18, task 3: class Expense."""

import csv
import sys
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"
LIMIT = 50.0  # an expense above this amount is "big"


class Expense:
    """One expense."""

    def __init__(self, date: str, category: str, amount: float, comment: str = ""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit: float) -> bool:
        """Return True if the amount is greater than the limit."""
        return self.amount > limit

    def describe(self) -> str:
        """Return a one-line description."""
        text = f"{self.date} {self.category} {self.amount:.2f}"
        if self.comment:
            text += f" ({self.comment})"
        return text


def load_expenses(path: Path) -> list[Expense]:
    """Read a CSV file (';' or ',') into a list of Expense objects."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        lines = [line for line in f if line.strip() and not line.startswith("#")]
    if not lines:
        return []

    delimiter = ";" if ";" in lines[0] else ","
    rows = list(csv.reader(lines, delimiter=delimiter))

    # Column order: date, category, amount, comment (or as named in the header)
    columns = {"date": 0, "category": 1, "amount": 2, "comment": 3}
    header = [cell.strip().lower() for cell in rows[0]]
    if "category" in header and "amount" in header:
        columns = {name: i for i, name in enumerate(header)}
        rows = rows[1:]

    expenses = []
    for row in rows:
        comment_index = columns.get("comment", len(row))
        comment = row[comment_index].strip() if comment_index < len(row) else ""
        expenses.append(Expense(
            row[columns["date"]].strip(),
            row[columns["category"]].strip(),
            float(row[columns["amount"]]),
            comment,
        ))
    return expenses


def main() -> None:
    print("Sofiia Zakharchuk, IT-32")
    try:
        expenses = load_expenses(DATA_FILE)
    except (OSError, ValueError, KeyError, IndexError) as error:
        sys.exit(f"error: cannot read {DATA_FILE}: {error}")

    print(f"objects: {len(expenses)}")
    print(f"big expenses (more than {LIMIT:.2f}):")
    for expense in expenses:
        if expense.is_big(LIMIT):
            print(" ", expense.describe())


if __name__ == "__main__":
    main()
