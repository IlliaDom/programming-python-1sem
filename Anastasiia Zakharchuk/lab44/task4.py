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
    Expense("2026-10-02", "books", 220.00),
    RecurringExpense("2026-10-01", "transport", 28.00, 20),
    RecurringExpense("2026-10-01", "coffee", 65.00, 8),
    SharedExpense("2026-10-01", "internet", 250.00, 2),
    SharedExpense("2026-10-01", "rent", 6000.00, 3),
    YearlyExpense("2026-09-15", "subscription", 1200.00),
]

total = 0
for expense in expenses:
    cost = expense.monthly_cost()
    total += cost
    print(f"{expense.category:<12} {cost:>8.2f}")

print(f"total: {total:.2f}")
