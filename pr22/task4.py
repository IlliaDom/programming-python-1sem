import sys

from task1 import GROUP, NAME, SURNAME, Money
from task3 import DATA_FILE, ExpenseBook, load_expenses

BUDGET = Money(6000)


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    book = ExpenseBook(load_expenses(DATA_FILE))
    print("total: ", book.total())
    print("budget:", BUDGET)
    print("book > budget:", book > BUDGET)
    if book > BUDGET:
        print(f"over budget by {book.total() - BUDGET}")
    else:
        print(f"within budget, left {BUDGET - book.total()}")


if __name__ == "__main__":
    main()
