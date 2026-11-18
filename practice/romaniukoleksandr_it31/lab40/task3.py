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
        return f"{self.date} {self.category} {self.amount} {self.comment}"


expenses_path = Path("data/expenses.csv")
expenses_list = []

records_count = 0

with open(expenses_path, "r", encoding="utf-8") as f:
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