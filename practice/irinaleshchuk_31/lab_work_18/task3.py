import csv


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return f"{self.date} | {self.category} | {self.amount:.2f} грн | {self.comment}"


expenses = []

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        expense = Expense(row[0], row[1], row[2], row[3])
        expenses.append(expense)

print("Усього витрат:", len(expenses))

limit = 100

print(f"\nВеликі витрати (понад {limit} грн):")

for expense in expenses:
    if expense.is_big(limit):
        print(expense.describe())