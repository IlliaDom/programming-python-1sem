
"""Практична робота №46 (П21).
Поліморфізм.
"""

import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, date, source, amount):
        self.date = date
        self.source = source
        self.amount = float(amount)

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = float(amount)

    def balance_change(self):
        return 0.0


def load_expenses(path):
    expenses = []

    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            if not row:
                continue

            if row[0].strip().lower() == "date":
                continue

            if len(row) == 4:
                date, category, amount, comment = row
                expenses.append(
                    Expense(date, category, float(amount), comment)
                )

    return expenses


def main():
    data_path = Path(__file__).parent / "data" / "expenses.csv"

    expenses = load_expenses(data_path)

    income = Income("2026-09-01", "стипендія", 2600.00)
    transfer = Transfer(
        "2026-09-15",
        "переказ між власними картками",
        300.00
    )

    operations = [income, *expenses, transfer]

    income_total = income.balance_change()
    expenses_total = sum(e.balance_change() for e in expenses)
    transfers_total = transfer.balance_change()

    balance = 0
    for operation in operations:
        balance += operation.balance_change()

    print("Вовк Марія Віталіївна, І-23")
    print(f"income:    {income_total:8.2f}")
    print(f"expenses:  {expenses_total:8.2f}")
    print(f"transfers: {transfers_total:8.2f}")
    print(f"balance:   {balance:8.2f}")


if __name__ == "__main__":
    main()
