"""Practice 22, task 4: comparing the book with a budget."""
import sys
from functools import total_ordering

from task1 import CSV_PATH, GROUP, NAME, Money, load_expenses
from task3 import ExpenseBook

BUDGET = 4500  # <- your real monthly budget


@total_ordering
class BudgetBook(ExpenseBook):
    """ExpenseBook that can be compared with Money (its total vs. a budget)."""

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.total() == other

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.total() < other

    __hash__ = None  # mutable collection, not hashable


if __name__ == "__main__":
    budget = Money(float(sys.argv[1]) if len(sys.argv) > 1 else BUDGET)
    book = BudgetBook(load_expenses(CSV_PATH))
    print(f"{NAME}, {GROUP}")
    print(book)
    print("budget:", budget)
    print("book > budget:", book > budget)
    print("book <= budget:", book <= budget)
    if book > budget:
        print("over budget by", book.total() - budget)
    else:
        print("within budget, left:", budget - book.total())
