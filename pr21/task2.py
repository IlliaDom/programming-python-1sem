from datetime import datetime
from pathlib import Path

NAME = "Nazarii Mischuk, IT-32"
DATA = Path(__file__).parent / "data"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @staticmethod
    def is_valid_date(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            return float(value) > 0
        except ValueError:
            return False

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(";")
        if len(parts) != 4:
            print("skipped (wrong number of fields):", line.strip())
            return None
        date, category, amount, comment = parts
        if not cls.is_valid_date(date):
            print("skipped (bad date):", line.strip())
            return None
        if not cls.is_valid_amount(amount):
            print("skipped (bad amount):", line.strip())
            return None
        return cls(date, category, float(amount), comment)


print(NAME)
print("2026-02-30 ->", Expense.is_valid_date("2026-02-30"))
print("2009-01-30 ->", Expense.is_valid_date("2009-01-30"))
print("85.50 ->", Expense.is_valid_amount("85.50"))
print("-5 ->", Expense.is_valid_amount("-5"))
print("abc ->", Expense.is_valid_amount("abc"))

with open(DATA / "expenses.csv", encoding="utf-8") as file:
    lines = file.readlines()

# bad lines to test the checks
lines.append("2026-02-30;food;50.00;wrong date")
lines.append("2026-11-12;food;abc;wrong amount")

expenses = []
for line in lines:
    if line.startswith("#") or not line.strip():
        continue
    expense = Expense.from_csv_line(line)
    if expense is not None:
        expenses.append(expense)

print("loaded:", len(expenses))
