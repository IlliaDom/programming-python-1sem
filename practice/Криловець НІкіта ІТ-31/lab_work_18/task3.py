import csv
from datetime import datetime


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        try:
            date = datetime.strptime(
                self.date, "%Y-%m-%d"
            ).strftime("%d.%m.%Y")
        except ValueError:
            date = self.date

        return f"{date} {self.category} {self.amount:.2f} ({self.comment})"


if __name__ == "__main__":
    expenses = []

    with open("data/expenses.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            if not row or row[0].startswith("#"):
                continue

            if row[0].lower() == "date":
                continue

            date, category, amount, comment = row
            expense = Expense(date, category, amount, comment)
            expenses.append(expense)

    limit = 300

    print("All expenses:", len(expenses))
    print(f"Big expenses (over {limit}):")

    for expense in expenses:
        if expense.is_big(limit):
            print(expense.describe())