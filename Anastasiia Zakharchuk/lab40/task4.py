class Expense:
    """One expense record."""

    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        year, month, day = self.date.split("-")
        return f"{day}.{month}.{year} {self.category} {self.amount:.2f} ({self.comment})"


def read_expenses(path):
    expenses = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            date, category, amount, comment = line.split(";")
            expenses.append(Expense(date, category, float(amount), comment))
    return expenses


class ExpenseBook:
    """A collection of Expense objects."""

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


book = ExpenseBook()
for expense in read_expenses("data/expenses.csv"):
    book.add(expense)

print("rows:", len(book.expenses))
print(f"total: {book.total():.2f}")

for category in ["food", "transport", "coffee", "books", "internet"]:
    print(f"{category}: {book.by_category(category):.2f}")

print("top 3:")
for expense in book.top(3):
    print(" ", expense.describe())