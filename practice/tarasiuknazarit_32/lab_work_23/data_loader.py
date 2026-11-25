import csv
from pathlib import Path

from expense import Expense

DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"


def load_expenses(path=DATA_FILE):
    with Path(path).open(encoding="utf-8", newline="") as file:
        return [Expense.from_row(row) for row in csv.DictReader(file)]
