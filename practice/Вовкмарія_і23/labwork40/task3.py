import csv
from datetime import datetime
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        date_text = datetime.strptime(self.date, "%Y-%m-%d").strftime("%d.%m.%Y")
        return f"{date_text} {self.category} {self.amount:.2f} ({self.comment})"


def main():
    csv_path = Path(__file__).parent / "data" / "expenses.csv"
    expenses = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            expenses.append(Expense(
                row["date"], row["category"], row["amount"], row["note"]
            ))

    limit = 100
    print("Кількість витрат:", len(expenses))
    print(f"Великі витрати (понад {limit:.2f} грн):")
    for expense in expenses:
        if expense.is_big(limit):
            print(expense.describe())


if __name__ == "__main__":
    main()
