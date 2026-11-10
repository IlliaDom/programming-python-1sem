import csv
from collections import defaultdict
from tabulate import tabulate

print("Mushka Vlad IT31")

categories = defaultdict(lambda: [0, 0.0])

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("#") or not line.strip():
            continue

        date, category, amount, note = line.strip().split(";")
        categories[category][0] += 1
        categories[category][1] += float(amount)

rows = []
total_count = 0
total_amount = 0.0

for category, (count, amount) in categories.items():
    rows.append([category, count, f"{amount:.2f}"])
    total_count += count
    total_amount += amount

rows.append(["TOTAL", total_count, f"{total_amount:.2f}"])

print(tabulate(rows, headers=["Category", "Count", "Total"], tablefmt="github"))
