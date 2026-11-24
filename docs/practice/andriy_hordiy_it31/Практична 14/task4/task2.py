from pathlib import Path
from tabulate import tabulate
expenses_path = Path(__file__).parent / "data" / "expenses.csv"
categories = []
with open(expenses_path, "r", encoding="utf-8") as expenses_file:
    for line in expenses_file.readlines()[1:]:
        category = line.split('|')[1]
        if category not in categories:
            categories.append(category)
headers = ["Category", "Count", "Total"]
table = []

count_categories = {}
total_sum = {}
with open(expenses_path, "r", encoding="utf-8") as expenses_file:
    for line in expenses_file.readlines()[1:]:
        category = line.split('|')[1]
        count_categories[category] = count_categories.get(category, 0) + 1
with open(expenses_path, "r", encoding="utf-8") as expenses_file:
    for line in expenses_file.readlines()[1:]:
        category = line.split('|')[1]
        amount = float(line.split('|')[2])
        total_sum[category] = total_sum.get(category, 0) + amount
for item in categories:
    table.append([item, count_categories[item], total_sum[item]])
categories_count_sum = sum(count_categories.values())
total_sum_sum = sum(total_sum.values())
table.append(["Total",categories_count_sum, total_sum_sum])
print(tabulate(table, headers))

