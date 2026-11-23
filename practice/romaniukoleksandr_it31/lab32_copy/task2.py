print("Oleksandr Romaniuk, IT-31")

from pathlib import Path

import tabulate

print(tabulate.__version__)

data = Path("data/expenses.csv")

expenses = []

with open(data, "r", encoding="utf-8") as f:
    for line in f.readlines():
        if line == " " or line.startswith("#"):
            continue

        expense = line.split(";")

        expenses.append(expense)

sorted_expenses = []

total_expenses = 0
total_sum = 0

for record in expenses:
    found = False

    for item in sorted_expenses:
        if record[1] == item[0]:
            item[1] += 1
            item[2] += float(record[2])
            
            found = True

    if not found:
        sorted_expenses.append([record[1], 1, float(record[2])])

    total_expenses += 1
    total_sum += float(record[2])

sorted_expenses.append(["TOTAL", total_expenses, total_sum])

print(tabulate.tabulate(sorted_expenses, headers=["category", "count", "total"], tablefmt="github"))