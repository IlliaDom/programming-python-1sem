from task3 import Expense, RecurringExpense, SharedExpense, build_expenses, total_monthly_cost


class YearlyExpense(Expense):
    def __init__(self, date: str, category: str, amount: float):
        super().__init__(date, category, amount)

    def monthly_cost(self) -> float:
        return self.amount / 12


if __name__ == "__main__":
    expenses = build_expenses()
    expenses.extend([
        YearlyExpense("2026-11-01", "Хмарне сховище (річна підписка)", 1200.00),
        YearlyExpense("2026-11-10", "Освітній сервіс (річна підписка)", 3600.00),
    ])

    for exp in expenses:
        print(f"{exp.date} | {exp.category:<34} | місячна вартість: {exp.monthly_cost():.2f} грн")

    print(f"\nЗагальна місячна вартість (з річними витратами): {total_monthly_cost(expenses):.2f} грн")