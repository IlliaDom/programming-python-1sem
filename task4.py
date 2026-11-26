
from task1 import load_csv


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, date, amount, comment=""):
        self.date = date
        self.amount = float(amount)
        self.comment = comment

    def balance_change(self):
        return 0


name = "Ілля Воробей"
group = "ІТ-31"
birthday = input("Введіть вашу дату народження (YYYY-MM-DD): ")

month = input("Введіть місяць для розрахунку (YYYY-MM): ")

all_expenses = load_csv("data/expenses.csv")

expenses = [
    Expense(item.date, item.category, item.amount, item.comment)
    for item in all_expenses
    if item.date.startswith(month)
]

income_amount = float(input("Введіть суму доходу за місяць (грн): "))

operations = [
    Income(month + "-01", "Стипендія / підробіток", income_amount)
]

operations.extend(expenses)

operations.append(Transfer(month + "-01", 500, "Переказ між власними картками"))

total_income = sum(
    op.balance_change() for op in operations
    if isinstance(op, Income)
)

total_expenses = sum(
    op.balance_change() for op in operations
    if isinstance(op, Expense)
)

total_transfers = sum(
    op.balance_change() for op in operations
    if isinstance(op, Transfer)
)

balance = 0

for operation in operations:
    balance += operation.balance_change()

print(f"\n{name}, {group}")
print(f"Дата народження: {birthday}")
print(f"Місяць: {month}")
print(f"income:    {total_income:10.2f}")
print(f"expenses:  {total_expenses:10.2f}")
print(f"transfers: {total_transfers:10.2f}")
print(f"balance:   {balance:10.2f}")
