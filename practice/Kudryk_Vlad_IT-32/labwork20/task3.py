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


def total_monthly_cost(expenses):
    total = 0.0
    for e in expenses:
        cost = e.monthly_cost()
        print(f"  {e.category:<12}{type(e).__name__:<18}{cost:>10.2f}")
        total += cost
    return total


def build_expenses():
    return [
        Expense("2026-11-03", "Продукти", 2150.75),
        RecurringExpense("2026-11-05", "Проїзний", 320.25, 2),
        RecurringExpense("2026-11-09", "Звʼязок", 175.00, 2),
        SharedExpense("2026-11-01", "Оренда", 8500.00, 2),
        SharedExpense("2026-11-12", "Комунальні", 1800.20, 3),
    ]


if __name__ == "__main__":
    expenses = build_expenses()
    print(f"Разом за місяць: {total_monthly_cost(expenses):.2f}")
