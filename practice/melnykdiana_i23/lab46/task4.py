"""Завдання 4. Поліморфізм для витрат, доходів і переказів."""

import csv
from pathlib import Path


class Expense:
    def __init__(self, amount):
        self.amount = float(amount)

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, amount, source):
        self.amount = float(amount)
        self.source = source

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, amount, description):
        self.amount = float(amount)
        self.description = description

    def balance_change(self):
        return 0.0


def main():
    name = "Diana Melnik"
    birth_date = "2008-01-02"  
    csv_path = Path(__file__).with_name("expenses.csv")
    with csv_path.open(encoding="utf-8", newline="") as file:
        october_expenses = [float(row["amount"]) for row in csv.DictReader(file)
                            if row["date"].startswith("2026-10")]

    transactions = [Income(2600, "стипендія")]
    transactions.extend(Expense(amount) for amount in october_expenses)
    transactions.append(Transfer(500, "переказ між своїми картками"))

    income_total = expense_total = transfer_total = balance = 0.0
    for item in transactions:
        change = item.balance_change()
        balance += change
        if change > 0:
            income_total += change
        elif change < 0:
            expense_total += change
        else:
            transfer_total += change
    print(f"{name}, дата народження: {birth_date}")
    print(f"income:    {income_total:8.2f}")
    print(f"expenses: {expense_total:8.2f}")
    print(f"transfers:{transfer_total:8.2f}")
    print(f"balance:  {balance:8.2f}")


if __name__ == "__main__":
    main()
