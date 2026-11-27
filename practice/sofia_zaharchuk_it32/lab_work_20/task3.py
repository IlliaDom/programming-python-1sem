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


def total_monthly(expenses):
    total = 0.0
    for expense in expenses:
        cost = expense.monthly_cost()
        print(f"  {expense.category:<12} {type(expense).__name__:<18} {cost:>9.2f}")
        total += cost
    return total


def make_expenses():
    return [
        Expense("2026-09-24", "stationery", 35),
        RecurringExpense("2026-09-01", "transport", 16, times_per_month=22),
        RecurringExpense("2026-09-01", "coffee", 45, times_per_month=8),
        SharedExpense("2026-09-01", "rent", 6000, people=2),
        SharedExpense("2026-09-01", "internet", 300, people=3),
    ]


if __name__ == "__main__":
    print("Sofiia Zakharchuk, IT-32")
    print("monthly costs:")
    print(f"total: {total_monthly(make_expenses()):.2f}")
