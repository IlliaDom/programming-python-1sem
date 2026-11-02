import csv
from collections import defaultdict
from decimal import Decimal
from tabulate import tabulate

print("Nikita Krilovets, IT-31")

expenses = defaultdict(lambda: {"count": 0, "total": Decimal("0.00")})

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

total_count = 0
total_sum = Decimal("0.00")

for category, data in expenses.items():
    table.append([
        category,
        data["count"],
        data["total"]
    ])

    total_count += data["count"]
    total_sum += data["total"]

table.append(["TOTAL", total_count, total_sum])

print(tabulate(
    table,
    headers=["category", "count", "total"],
    tablefmt="github",
    floatfmt=".2f"
))
