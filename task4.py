
from task1 import Money
from task3 import ExpenseBook, load_expenses


expenses = load_expenses("data/expenses.csv")
month = ExpenseBook(expenses)

budget_amount = float(input("Введіть свій місячний бюджет (грн): "))
budget = Money(budget_amount)

print("\nЗагальна сума витрат:", month.total())
print("Місячний бюджет:", budget)

if month > budget:
    print("Ви перевищили місячний бюджет.")
else:
    print("Ви вкладаєтеся у місячний бюджет.")

difference = budget_amount - month.total().cents / 100

if difference >= 0:
    print(f"Залишилося: {difference:.2f} грн")
else:
    print(f"Перевищення: {abs(difference):.2f} грн")
