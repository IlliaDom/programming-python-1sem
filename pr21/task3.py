from pathlib import Path

NAME = "Nazarii Mischuk, IT-32"
DATA = Path(__file__).parent / "data"


class Expense:
    currency = "UAH"
    count = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.count += 1

    @classmethod
    def from_csv_line(cls, line):
        date, category, amount, comment = line.strip().split(";")
        return cls(date, category, float(amount), comment)

    @classmethod
    def set_currency(cls, code):
        cls.currency = code

    def show(self):
        print(f"{self.date}  {self.category:<10} {self.amount:>8.2f} {self.currency}")


print(NAME)

expenses = []
with open(DATA / "expenses.csv", encoding="utf-8") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue
        expenses.append(Expense.from_csv_line(line))

print("created objects:", Expense.count)

print("\nbefore:")
for expense in expenses[:3]:
    expense.show()

# only the label changes, amounts are not converted
Expense.set_currency("USD")

print("\nafter:")
for expense in expenses[:3]:
    expense.show()
