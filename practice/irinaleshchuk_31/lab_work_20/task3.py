
class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


expenses = [
    RecurringExpense("01.11.2026", "Проїзд", 15, 40),
    RecurringExpense("01.11.2026", "Мобільний зв'язок", 200, 1),
    SharedExpense("01.11.2026", "Інтернет", 300, 3),
    SharedExpense("01.11.2026", "Оренда", 6000, 2),
    YearlyExpense("01.11.2026", "Річна підписка", 1200)
]

total = 0

for expense in expenses:
    cost = expense.monthly_cost()
    total += cost
    print(f"{expense.category}: {cost:.2f} грн")

print(f"\nЗагальна місячна вартість: {total:.2f} грн")
