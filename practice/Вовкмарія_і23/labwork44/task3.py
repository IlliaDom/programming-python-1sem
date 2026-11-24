import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"


class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = float(amount)

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = int(times_per_month)

    def monthly_cost(self):
        return super().monthly_cost() * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        if people < 1:
            raise ValueError("Кількість людей має бути не меншою за 1.")
        self.people = int(people)

    def monthly_cost(self):
        return super().monthly_cost() / self.people


def read_csv():
    with DATA_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def main():
    rows = read_csv()
    transport = [r for r in rows if r["category"].lower() == "transport"]
    food = [r for r in rows if r["category"].lower() == "food"]
    other = [r for r in rows if r["category"].lower() not in ("transport", "food")]

    if len(transport) < 2 or len(food) < 2 or len(other) < 2:
        raise ValueError("У CSV недостатньо записів для демонстрації всіх типів витрат.")

    people = int(input("На скількох людей поділити спільні витрати? "))
    if people < 1:
        raise ValueError("Кількість людей має бути не меншою за 1.")

    # Значення беруться з особистого CSV; множник 4 демонструє повторення 4 рази на місяць.
    expenses = [
        Expense(other[0]["date"], other[0]["category"], other[0]["amount"]),
        Expense(other[1]["date"], other[1]["category"], other[1]["amount"]),
        RecurringExpense(transport[0]["date"], transport[0]["category"], transport[0]["amount"], 4),
        RecurringExpense(transport[1]["date"], transport[1]["category"], transport[1]["amount"], 4),
        SharedExpense(food[0]["date"], food[0]["category"], food[0]["amount"], people),
        SharedExpense(food[1]["date"], food[1]["category"], food[1]["amount"], people),
    ]

    print("\nМісячна вартість витрат:")
    total = 0
    for expense in expenses:
        cost = expense.monthly_cost()
        total += cost
        print(f"{expense.category}: {cost:.2f} грн")
    print(f"Загальна сума: {total:.2f} грн")


if __name__ == "__main__":
    main()
