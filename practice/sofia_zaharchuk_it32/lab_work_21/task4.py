"""Practice 21, task 4: polymorphism without a common parent class."""
from datetime import date, datetime

NAME = "Sofiia Zakharchuk"
GROUP = "IT-32"
CSV_PATH = "data/expenses.csv"
BIRTHDAY = date(2026, 9, 14)


class Expense:
    def __init__(self, day, amount, comment=""):
        self.day, self.amount, self.comment = day, amount, comment

    @classmethod
    def from_csv_line(cls, line):
        sep = ";" if ";" in line else ","
        day, _category, amount, *rest = [p.strip() for p in line.strip().split(sep, 3)]
        return cls(datetime.strptime(day, "%Y-%m-%d").date(), float(amount), rest[0] if rest else "")

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, day, amount, comment=""):
        self.day, self.amount, self.comment = day, amount, comment

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, day, amount, comment=""):
        self.day, self.amount, self.comment = day, amount, comment

    def balance_change(self):
        return 0.0  # between own cards: the total does not change


def load_expenses(path):
    result = []
    with open(path, encoding="utf-8-sig") as file:
        for number, line in enumerate(file, start=1):
            if not line.strip() or (number == 1 and not line.strip()[0].isdigit()):
                continue
            try:
                result.append(Expense.from_csv_line(line))
            except ValueError as error:
                print(f"skip line {number}: {error}")
    return result


if __name__ == "__main__":
    first_day = date(2026, 9, 1)
    operations = [
        Income(first_day, 2600.00, "scholarship"),
        Income(date(2026, 9, 20), 700.00, "part-time job"),
        Income(BIRTHDAY, 300.00, "birthday gift"),
        Transfer(date(2026, 9, 3), 500.00, "to savings card"),
        Transfer(date(2026, 9, 18), 200.00, "to main card"),
    ]
    operations += load_expenses(CSV_PATH)  # mixed list: three unrelated classes

    income = expenses = transfers = 0.0
    for operation in operations:
        change = operation.balance_change()  # no type checks
        if change > 0:
            income += change
        elif change < 0:
            expenses += change
        else:
            transfers += change

    print(f"{NAME}, {GROUP}")
    print(f"{'income:':<10}{income:>8.2f}")
    print(f"{'expenses:':<10}{expenses:>8.2f}")
    print(f"{'transfers:':<10}{transfers:>8.2f}")
    print(f"{'balance:':<10}{income + expenses + transfers:>8.2f}")
