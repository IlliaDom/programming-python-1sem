from pathlib import Path
from task3 import Expense, load_expenses


class ExpenseBook:
    def __init__(self, expenses: list[Expense] | None = None) -> None:
        self.expenses: list[Expense] = list(expenses) if expenses else []

    def add(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def total(self) -> float:
        return sum(item.amount for item in self.expenses)

    def by_category(self, category: str) -> float:
        target = category.strip().casefold()
        return sum(
            item.amount
            for item in self.expenses
            if item.category.strip().casefold() == target
        )

    def top(self, n: int) -> list[Expense]:
        if n <= 0:
            return []
        return sorted(self.expenses, key=lambda item: item.amount, reverse=True)[:n]


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent / "data" / "expenses.csv"
    book = ExpenseBook(load_expenses(csv_path))

    print(f"Загальна сума витрат: {book.total():.2f}")

    categories = sorted({item.category for item in book.expenses})
    print("\nСуми за категоріями:")
    for category in categories:
        print(f"  {category}: {book.by_category(category):.2f}")

    print("\nТоп-2 витрати:")
    for item in book.top(2):
        print(f"  {item.describe()}")