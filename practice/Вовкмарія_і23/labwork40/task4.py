from task3 import Expense
import csv
from pathlib import Path


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self, category):
        return sum(
            expense.amount for expense in self.expenses
            if expense.category == category
        )

    def top(self, n):
        return sorted(
            self.expenses, key=lambda expense: expense.amount, reverse=True
        )[:n]


csv_path = Path(__file__).parent / "data" / "expenses.csv"
book = ExpenseBook()

with open(csv_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        book.add(Expense(
            row["date"], row["category"], row["amount"], row["note"]
        ))

print("Кількість витрат:", len(book.expenses))
print(f"Загальна сума: {book.total():.2f} грн")
print("Суми за категоріями:")
for category in sorted({expense.category for expense in book.expenses}):
    print(f"{category}: {book.by_category(category):.2f} грн")

print("Три найбільші витрати:")
for expense in book.top(3):
    print(expense.describe())
