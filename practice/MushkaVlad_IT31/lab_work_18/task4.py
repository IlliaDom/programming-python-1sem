from task3 import Expense


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self, category):
        return sum(
            expense.amount
            for expense in self.expenses
            if expense.category == category
        )

    def top(self, n):
        return sorted(
            self.expenses,
            key=lambda expense: expense.amount,
            reverse=True
        )[:n]


book = ExpenseBook()

with open("lab_work_18/data/expenses.csv", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        date, category, amount, comment = line.split(";")
        book.add(Expense(date, category, amount, comment))


print("Total:", f"{book.total():.2f}")

print("\nBy category:")
categories = sorted(set(expense.category for expense in book.expenses))

for category in categories:
    print(f"{category}: {book.by_category(category):.2f}")

print("\nTop 3 expenses:")
for expense in book.top(3):
    print(expense.describe())
