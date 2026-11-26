"""Завдання 4. Порівняння місячних витрат із бюджетом."""

from task3 import ExpenseBook, load_expenses
from task1 import Money


MONTHLY_BUDGET = Money(5000)  # Замініть на власний реальний бюджет.


def main():
    expenses = load_expenses()
    book = ExpenseBook(expenses, "Місячні витрати")
    total = book.total()
    print(f"Загальні витрати: {total}")
    print(f"Місячний бюджет: {MONTHLY_BUDGET}")
    print(f"Витрати перевищують бюджет: {book > MONTHLY_BUDGET}")
    if book > MONTHLY_BUDGET:
        print(f"Перевищення бюджету: {total - MONTHLY_BUDGET}")
    else:
        print(f"Залишок бюджету: {MONTHLY_BUDGET - total}")


if __name__ == "__main__":
    main()
