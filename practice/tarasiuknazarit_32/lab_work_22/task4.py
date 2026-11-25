"""
Завдання 4. Бюджет.
book > Money(budget) повертає True, якщо загальна сума витрат
більша за бюджет.
"""
from expense_book import ExpenseBook
from money import Money

EXPENSES_FILE = "data/expenses.csv"
MONTHLY_BUDGET = 1200.0  # TODO: заміни на свій реальний місячний бюджет


def main() -> None:
    book = ExpenseBook.from_csv(EXPENSES_FILE)
    budget = Money(MONTHLY_BUDGET)

    print(book)
    print("бюджет:", budget)

    if book > budget:
        over = book.total() - budget
        print(f"бюджет перевищено на {over}")
    elif book < budget:
        remaining = budget - book.total()
        print(f"укладаєтесь у бюджет, залишок {remaining}")
    else:
        print("витрати точно дорівнюють бюджету")


if __name__ == "__main__":
    main()
