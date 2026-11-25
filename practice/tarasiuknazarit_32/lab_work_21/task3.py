"""
Завдання 3. Змінна класу.
Expense.currency і Expense.count спільні для всіх обʼєктів;
set_currency() змінює валюту одразу для всіх витрат.
"""
from expense import Expense

EXPENSES_FILE = "data/expenses.csv"


def main() -> None:
    expenses = []
    with open(EXPENSES_FILE, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                expense = Expense.from_csv_line(line)
                if expense is not None:
                    expenses.append(expense)

    print(f"створено обʼєктів: {Expense.count}")
    print(f"валюта: {Expense.currency}")
    for expense in expenses:
        print(" -", expense.describe())

    print("\n--- Expense.set_currency('USD') ---")
    Expense.set_currency("USD")
    print(f"валюта: {Expense.currency}")
    for expense in expenses:
        print(" -", expense.describe())


if __name__ == "__main__":
    main()
