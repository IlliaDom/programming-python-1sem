from task3 import Expense, read_expenses


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(e.amount for e in self.expenses)

    def by_category(self, category):
        return sum(e.amount for e in self.expenses if e.category == category)

    def top(self, n):
        return sorted(self.expenses, key=lambda e: e.amount, reverse=True)[:n]


print("Vlad Kudryk, IT-32")

book = ExpenseBook()
for e in read_expenses("data/expenses.csv"):
    book.add(e)

print(f"total: {book.total():.2f} UAH")

for category in ("food", "transport"):
    print(f"{category}: {book.by_category(category):.2f} UAH")

print("top 3:")
for e in book.top(3):
    print(e.describe())