from task3 import Expense, RecurringExpense, SharedExpense


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


expenses = [
    RecurringExpense("01.11.2026", "Проїзд", 20, 40),
    RecurringExpense("05.11.2026", "Мобільний зв'язок", 200, 1),
    SharedExpense("10.11.2026", "Оренда", 6000, 3),
    SharedExpense("15.11.2026", "Комунальні послуги", 1500, 3),
    YearlyExpense("20.11.2026", "Річна підписка", 1200)
]

total = 0

for expense in expenses:
    cost = expense.monthly_cost()
    total += cost
    print(f"{expense.category}: {cost:.2f} грн")

print(f"\nЗагальна місячна вартість: {total:.2f} грн")