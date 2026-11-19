from pathlib import Path

from task3 import Expense, read_expenses


class ExpenseBook:
    def __init__(self, expenses: list[Expense] | None = None) -> None:
        self.expenses = list(expenses) if expenses is not None else []

    def add(self, expense: Expense) -> None:
        if not isinstance(expense, Expense):
            raise TypeError("До книги можна додавати лише об'єкти Expense")
        self.expenses.append(expense)

    def total(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def by_category(self, category: str) -> float:
        return sum(expense.amount for expense in self.expenses if expense.category == category)

    def top(self, n: int) -> list[Expense]:
        if n < 0:
            raise ValueError("n не може бути від'ємним")
        return sorted(self.expenses, key=lambda expense: expense.amount, reverse=True)[:n]


def main() -> None:
    data_file = Path(__file__).with_name("expenses.csv")
    book = ExpenseBook(read_expenses(data_file))

    print("Мельник Діана, І-23")
    print(f"Кількість витрат: {len(book.expenses)}")
    print(f"Разом: {book.total():.2f} грн")
    print("За категоріями:")
    categories = sorted({expense.category for expense in book.expenses})
    for category in categories:
        print(f"{category}: {book.by_category(category):.2f} грн")
    print("Три найбільші витрати:")
    for expense in book.top(3):
        print(expense.describe())


if __name__ == "__main__":
    main()
