import csv
from decimal import Decimal
from collections import defaultdict
from tabulate import tabulate

print("Ira Leshchuk, IT-31")

expenses = defaultdict(lambda: {"count": 0, "total": Decimal("0")})

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        if not row or row[0].strip().startswith("#"):
            continue
        category = row[1].strip()
        amount = Decimal(row[2].strip())
        expenses[category]["count"] += 1
        expenses[category]["total"] += amount

table = []
for category, data in sorted(expenses.items()):
    table.append([category, data["count"], f'{data["total"]:.2f}'])

total_count = sum(data["count"] for data in expenses.values())
total_sum = sum((data["total"] for data in expenses.values()), Decimal("0"))

table.append(["TOTAL", total_count, f"{total_sum:.2f}"])

print(tabulate(table, headers=["category", "count", "total"], tablefmt="github"))
