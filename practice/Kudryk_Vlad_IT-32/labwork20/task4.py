from task3 import Expense, build_expenses, total_monthly_cost


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


expenses = build_expenses()
print("До додавання річної витрати:")
print(f"Разом: {total_monthly_cost(expenses):.2f}\n")

expenses.append(YearlyExpense("2026-11-15", "Підписка", 2400.00))
print("Після додавання YearlyExpense:")
print(f"Разом: {total_monthly_cost(expenses):.2f}")
