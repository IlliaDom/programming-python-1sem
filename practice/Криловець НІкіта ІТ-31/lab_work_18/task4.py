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
            expense
            for expense in self.expenses
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
        if not row or row[0].startswith("#"):
            continue

        if row[0].lower() == "date":
            continue

        date, category, amount, comment = row
        expense = Expense(date, category, amount, comment)
        book.add(expense)


print("Total expenses:", book.total())

category = "Продукти"
category_expenses = book.by_category(category)

print(f"\nExpenses in category {category}:")
for expense in category_expenses:
    print(expense.describe())

print(
    f"Total in category {category}:",
    sum(expense.amount for expense in category_expenses)
)

print("\nTop 3 expenses:")
for expense in book.top(3):
    print(expense.describe())