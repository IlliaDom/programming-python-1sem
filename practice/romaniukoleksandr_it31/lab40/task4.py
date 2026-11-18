from pathlib import Path

class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return f"{self.date} {self.category} {self.amount} {self.comment}"


class ExpenseBook:
    def __init__(self):
        self.expenses: list[Expense] = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        total_amount = 0

        for record in self.expenses:
            total_amount += record.amount

        return total_amount

    def by_category(self, category):
        categorize = {}

        for record in self.expenses:

            if record.category == category:
                if category in categorize:
                    categorize[category] += record.amount
                else:
                    categorize[category] = record.amount 

        return categorize

    def top(self, n):
       sorted_expenses = sorted(self.expenses, key=lambda expense: expense.amount, reverse=True)
       return sorted_expenses[:n]


expenses_path = Path("data/expenses.csv")
book = ExpenseBook()

with open(expenses_path, "r", encoding="utf-8") as f:
    for record in f.readlines():
        if record.startswith("#") or record == "":
            continue

        date, category, amount, comment = record.strip().split(";")

        expense = Expense(date, category, float(amount), comment)

        book.add(expense)

print(f'Total expenses: {book.total()}')
print(f'Books expenses: {book.by_category("books")}')
print(f'Food expenses: {book.by_category("food")}')
print(f'Transport expenses: {book.by_category("transport")}')
print(f'Top 3 expenses: {[record.describe() for record in book.top(3)]}')