from expense import ExpenseBook

EXPENSES_FILE = "data/expenses.csv"
TOP_N = 3


def main() -> None:
    book = ExpenseBook.from_csv(EXPENSES_FILE)

    print(f"усього витрачено: {book.total():.2f} UAH")

    categories = sorted({e.category for e in book.expenses})
    print("за категоріями:")
    for category in categories:
        print(f"  {category}: {book.by_category(category):.2f} UAH")

    print(f"топ-{TOP_N} найбільших витрат:")
    for expense in book.top(TOP_N):
        print(" -", expense.describe())


if __name__ == "__main__":
    main()
