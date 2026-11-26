"""Завдання 3. Змінна класу та лічильник створених витрат."""

from task2 import Expense as BaseExpense


class Expense(BaseExpense):
    currency = "UAH"
    created_count = 0

    def __init__(self, date, category, amount, comment=""):
        super().__init__(date, category, amount, comment)
        Expense.created_count += 1

    @classmethod
    def set_currency(cls, code):
        cls.currency = code.upper()

    def __str__(self):
        return f"{self.category}: {self.amount:.2f} {self.currency}"


def main():
    expenses = [Expense("2026-10-01", "transport", 60, "Проїзд"),
                Expense("2026-10-04", "internet", 300, "Інтернет")]
    print("До зміни валюти:")
    for expense in expenses:
        print(expense)
    print(f"Створено об'єктів: {Expense.created_count}")
    Expense.set_currency("USD")
    print("Після Expense.set_currency('USD'):")
    for expense in expenses:
        print(expense)


if __name__ == "__main__":
    main()
