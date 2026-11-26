"""Завдання 3. Поліморфний розрахунок місячних витрат із expenses.csv."""

import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = float(amount)

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return super().monthly_cost() * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        if people <= 0:
            raise ValueError("Кількість людей має бути більшою за нуль")
        self.people = people

    def monthly_cost(self):
        return super().monthly_cost() / self.people


def main():
    csv_path = Path(__file__).with_name("expenses.csv")
    with csv_path.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    transport_rows = [row for row in rows if row["category"] == "transport"][:2]
    food_rows = [row for row in rows if row["category"] == "food"][:2]
    expenses = [RecurringExpense(row["date"], row["category"], row["amount"], 3)
                for row in transport_rows]
    expenses += [SharedExpense(row["date"], row["category"], row["amount"], 2)
                 for row in food_rows]

    print("Витрати (суми взято з expenses.csv):")
    total = 0
    for expense in expenses:
        cost = expense.monthly_cost()
        total += cost
        print(f"{expense.date} | {expense.category:<10} | {expense.amount:>6.2f} грн | "
              f"місячна частка: {cost:>6.2f} грн")
    print(f"Загальна місячна вартість: {total:.2f} грн")


if __name__ == "__main__":
    main()
