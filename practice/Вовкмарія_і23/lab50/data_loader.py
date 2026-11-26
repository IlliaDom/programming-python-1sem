import csv
from pathlib import Path
from expense import Expense


def load_expenses():
    source = Path(__file__).parent / "data" / "expenses.csv"
    expenses = []
    with source.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            expenses.append(Expense.from_dict(row))
    return expenses
