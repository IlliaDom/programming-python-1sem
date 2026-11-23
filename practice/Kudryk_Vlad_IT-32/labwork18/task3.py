import csv


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        y, m, d = self.date.split("-")
        return f"{d}.{m}.{y} {self.category} {self.amount:.2f} ({self.comment})"


def read_expenses(path):
    expenses = []
    with open(path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f, delimiter=";"):
            expenses.append(Expense(
                row["date"],
                row["category"],
                float(row["amount"]),
                row["comment"],
            ))
    return expenses


if __name__ == "__main__":
    print("Vlad Kudryk, IT-32")

    expenses = read_expenses("data/expenses.csv")
    print("objects:", len(expenses))

    LIMIT = 50
    print("big expenses (> " + str(LIMIT) + "):")
    for e in expenses:
        if e.is_big(LIMIT):
            print(e.describe())