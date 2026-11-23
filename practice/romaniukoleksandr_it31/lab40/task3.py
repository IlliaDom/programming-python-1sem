from pathlib import Path

EXPENSES_PATH = Path("data/expenses.csv")

class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return f"{self.date} {self.category} {self.amount} {self.comment}"


if __name__ == "__main__":
    expenses_list = []

    records_count = 0

    with open(EXPENSES_PATH, "r", encoding="utf-8") as f:
        for record in f.readlines():
            if record.startswith("#") or record == "":
                continue

            date, category, amount, comment = record.strip().split(";")

            expenses_list.append(Expense(date, category, float(amount), comment))

            records_count += 1

    for record in expenses_list:
        if record.is_big(500):
            print(record.describe())

    print(f"Is equal count: {len(expenses_list) == records_count}")