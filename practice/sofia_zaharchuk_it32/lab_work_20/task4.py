from task3 import Expense, make_expenses, total_monthly


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


if __name__ == "__main__":
    print("Sofiia Zakharchuk, IT-32")
    expenses = make_expenses()
    print("before:")
    print(f"total: {total_monthly(expenses):.2f}")

    expenses.append(YearlyExpense("2026-09-10", "subscription", 1200))
    print("after adding YearlyExpense:")
    print(f"total: {total_monthly(expenses):.2f}")
