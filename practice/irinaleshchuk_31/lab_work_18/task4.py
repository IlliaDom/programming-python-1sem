import csv
from task3 import Expense


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self, category):
        return [
            expense for expense in self.expenses
            if expense.category == category
        ]

    def top(self, n):
        return sorted(
            self.expenses,
            key=lambda expense: expense.amount,
            reverse=True
        )[:n]


book = ExpenseBook()

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        book.add(Expense(row[0], row[1], row[2], row[3]))

print("Загальна сума витрат:", book.total(), "грн")

print("\nВитрати на food:")
for expense in book.by_category("food"):
    print(expense.describe())

print("\nТри найбільші витрати:")
for expense in book.top(3):
    print(expense.describe())