
from pathlib import Path
from task3 import Expense, load_expenses


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self, category):
        return sum(
            expense.amount
            for expense in self.expenses
            if expense.category == category
        )

    def top(self, n):
        return sorted(
            self.expenses,
            key=lambda expense: expense.amount,
            reverse=True
        )[:n]


def main():
    path = Path(__file__).parent / "data" / "expenses.csv"

    if not path.exists():
        print("Помилка: expenses.csv не знайдено")
        raise SystemExit(1)

    expenses = load_expenses(path)

    book = ExpenseBook()

    for expense in expenses:
        book.add(expense)

    print("Воробей Ілля, ІТ-21")
    print("Number of expenses:", len(book.expenses))

    print(f"\nTotal expenses: {book.total():.2f} UAH")

    print("\nExpenses by category:")

    categories = sorted(set(
        expense.category for expense in book.expenses
    ))

    for category in categories:
        print(f"{category}: {book.by_category(category):.2f} UAH")

    print("\nTop 5 expenses:")

    for expense in book.top(5):
        print(expense.describe())


if __name__ == "__main__":
    main()
