from expense import ExpenseBook

EXPENSES_FILE = "data/expenses.csv"
BIG_LIMIT = 150.0  # власний ліміт "великої" витрати, UAH


def main() -> None:
    book = ExpenseBook.from_csv(EXPENSES_FILE)

    print(f"усього витрат: {len(book.expenses)}")
    print(f"великі витрати (> {BIG_LIMIT:.2f} UAH):")

    for expense in book.expenses:
        if expense.is_big(BIG_LIMIT):
            print(" -", expense.describe())


if __name__ == "__main__":
    main()
