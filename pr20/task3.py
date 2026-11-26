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


expenses = [
    RecurringExpense("2026-11-02", "transport", 15, 40),
    RecurringExpense("2026-11-03", "lunch", 120, 20),
    SharedExpense("2026-11-05", "rent", 9000, 3),
    SharedExpense("2026-11-10", "internet", 300, 3),
]


def print_total(items):
    total = 0
    for item in items:
        cost = item.monthly_cost()
        total += cost
        print(f"{item.date}  {item.category:<10} {cost:>9.2f} UAH")
    print(f"Total: {total:.2f} UAH")


if __name__ == "__main__":
    print_total(expenses)
