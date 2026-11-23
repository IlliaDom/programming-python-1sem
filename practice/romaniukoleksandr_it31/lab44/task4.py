class Expense():
    def __init__(self, date, category, amount):
        self.date = date
        self.catefory = category
        self.amount = amount

    def monthly_cost(self):
        return self.amount


class ReccuringExpense(Expense):
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
    def __init__(self, date, category, amount):
        super().__init__(date, category, amount)

    def monthly_cost(self):
        return self.amount / 12


if __name__ == "__main__":
    expenses_list = [Expense("2026-10-24", "books", 699.00), Expense("2026-10-12", "food", 480.00), ReccuringExpense("2026-11-20", "transport", 120.00, 4), ReccuringExpense("2026-11-23", "food", 42.00, 15), SharedExpense("2026-11-31", "internet", 359.00, 3), SharedExpense("2026-11-15", "bill", 1230.00, 3), YearlyExpense("2026-11-23", "subsription", 4520.59), YearlyExpense("2026-11-23", "subsription", 5424.80)]

    total = 0

    for expense in expenses_list:
        total += expense.monthly_cost()

    print("Total monthly expenses:", round(total, 2))