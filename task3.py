
from task1 import Expense, load_csv

expenses = load_csv("data/expenses.csv")

print("Початкова валюта:")
for expense in expenses:
    print(expense)

print("\nКількість створених об'єктів:", Expense.created)

Expense.set_currency("USD")

print("\nПісля зміни валюти:")
for expense in expenses:
    print(expense)

print("\nКількість створених об'єктів:", Expense.created)
