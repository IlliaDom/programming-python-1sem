import sys

from task3 import DATA_FILE, GROUP, NAME, SURNAME, load_expenses


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


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    book = ExpenseBook()
    for expense in load_expenses(DATA_FILE):
        book.add(expense)

    print(f"total: {book.total():.2f}")
    for category in sorted({e.category for e in book.expenses}):
        print(f"  {category:<12} {book.by_category(category):>9.2f}")
    print("top 3:")
    for e in book.top(3):
        print("  " + e.describe())


if __name__ == "__main__":
    main()
