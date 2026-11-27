"""Lab 18, task 4: class ExpenseBook."""

import sys

from task3 import DATA_FILE, Expense, load_expenses


class ExpenseBook:
    """A collection of expenses."""

    def __init__(self):
        self.expenses: list[Expense] = []  # own list for every object

    def add(self, expense: Expense) -> None:
        """Add one expense."""
        self.expenses.append(expense)

    def total(self) -> float:
        """Return the sum of all expenses."""
        return sum(e.amount for e in self.expenses)

    def by_category(self, category: str) -> list[Expense]:
        """Return the expenses of one category."""
        return [e for e in self.expenses if e.category == category]

    def top(self, n: int) -> list[Expense]:
        """Return the n biggest expenses."""
        return sorted(self.expenses, key=lambda e: e.amount, reverse=True)[:n]


def main() -> None:
    print("Sofiia Zakharchuk, IT-32")
    book = ExpenseBook()
    try:
        for expense in load_expenses(DATA_FILE):
            book.add(expense)
    except (OSError, ValueError, KeyError, IndexError) as error:
        sys.exit(f"error: cannot read {DATA_FILE}: {error}")

    print(f"expenses: {len(book.expenses)}")
    print(f"total: {book.total():.2f}")

    print("\nby category:")
    for category in sorted({e.category for e in book.expenses}):
        items = book.by_category(category)
        amount = sum(e.amount for e in items)
        print(f"  {category:<12} {len(items):>2} {amount:>8.2f}")

    print("\ntop 3:")
    for expense in book.top(3):
        print(" ", expense.describe())


if __name__ == "__main__":
    main()
