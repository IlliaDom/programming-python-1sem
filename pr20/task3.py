NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"


class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    """Регулярна витрата: сума * кількість разів на місяць."""
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    """Спільна витрата: сума / кількість людей."""
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people


def build_expenses():
    # ЗАМІНІТЬ на свої реальні витрати
    return [
        Expense("2026-11-01", "food", 1500.00),
        RecurringExpense("2026-11-01", "transport", 20.00, 40),
        RecurringExpense("2026-11-01", "mobile", 150.00, 1),
        SharedExpense("2026-11-01", "rent", 12000.00, 3),
        SharedExpense("2026-11-01", "internet", 400.00, 2),
    ]


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    expenses = build_expenses()
    total = 0.0
    for e in expenses:                      # без isinstance
        cost = e.monthly_cost()
        total += cost
        print(f"{type(e).__name__:<17} {e.category:<10} {cost:>9.2f}")
    print(f"{'total':<28} {total:>9.2f}")


if __name__ == "__main__":
    main()
