from task3 import Expense, expenses, print_total


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


expenses.append(YearlyExpense("2026-11-15", "music", 1200))

print_total(expenses)
