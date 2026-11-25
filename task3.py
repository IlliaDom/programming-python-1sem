
import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return (
            f"{self.date} {self.category} "
            f"{self.amount:.2f} ({self.comment})"
        )


def load_expenses(path):
    expenses = []

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            if not row or row[0].strip().startswith("#"):
                continue

            if len(row) < 3:
                continue

            try:
                date = row[0].strip()
                category = row[1].strip()
                amount = float(row[2].strip().replace(",", "."))
                comment = row[3].strip() if len(row) > 3 else ""

                expense = Expense(date, category, amount, comment)
                expenses.append(expense)

            except ValueError:
                continue

    return expenses


if __name__ == "__main__":
    path = Path(__file__).parent / "data" / "expenses.csv"

    if not path.exists():
        print("Помилка: expenses.csv не знайдено")
        raise SystemExit(1)

    expenses = load_expenses(path)

    print("Воробей Ілля, ІТ-31")
    print("Total expenses:", len(expenses))

    print("\nBig expenses:")

    limit = 100

    for expense in expenses:
        if expense.is_big(limit):
            print(expense.describe())
