from pathlib import Path

NAME = "Nazarii Mischuk, IT-32"
MONTH = "2026-11"
DATA = Path(__file__).parent / "data"


class Expense:
    def __init__(self, amount):
        self.amount = amount

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, amount, source):
        self.amount = amount
        self.source = source

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, amount):
        self.amount = amount

    def balance_change(self):
        return 0


operations = []

with open(DATA / "expenses.csv", encoding="utf-8") as file:
    for line in file:
        if line.startswith(MONTH):
            amount = float(line.split(";")[2])
            operations.append(Expense(amount))

operations.append(Income(1500, "scholarship"))
operations.append(Income(800, "part-time job"))
operations.append(Transfer(500))

income = 0
expenses = 0
transfers = 0
balance = 0

for operation in operations:
    change = operation.balance_change()
    balance += change
    if change > 0:
        income += change
    elif change < 0:
        expenses += change
    else:
        transfers += change

print(NAME)
print(f"income:    {income:8.2f}")
print(f"expenses:  {expenses:8.2f}")
print(f"transfers: {transfers:8.2f}")
print(f"balance:   {balance:8.2f}")
