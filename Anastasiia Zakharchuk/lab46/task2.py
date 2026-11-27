from datetime import datetime


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
            print("skip (wrong number of fields):", line.strip())
            return None
        date, category, amount, comment = parts
        if not cls.is_valid_date(date):
            print("skip (bad date):", line.strip())
            return None
        if not cls.is_valid_amount(amount):
            print("skip (bad amount):", line.strip())
            return None
        return cls(date, category, float(amount), comment)


def load_csv(path):
    expenses = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            expense = Expense.from_csv_line(line)
            if expense:
                expenses.append(expense)
    return expenses


print(Expense.is_valid_date("2026-02-30"))
print(Expense.is_valid_date("2026-09-21"))
print(Expense.is_valid_amount("85.50"))
print(Expense.is_valid_amount("abc"))
print(Expense.is_valid_amount("-5"))

test_lines = [
    "2026-10-04;food;90.00;lunch",
    "2026-02-30;food;50.00;wrong date",
    "2026-10-05;coffee;abc;wrong amount",
    "2026-10-06;transport;28.00",
]
for line in test_lines:
    expense = Expense.from_csv_line(line)
    if expense:
        print("ok:", expense.date, expense.category, expense.amount)

expenses = load_csv("data/expenses.csv")
print("loaded:", len(expenses))
