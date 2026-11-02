from tabulate import tabulate

print("Yaroslav Korolchuk, IT-31")

totals = {}
counts = {}

with open("data/expenses.csv", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";", 3)
        if len(parts) < 3:
            continue
        category = parts[1]
        amount = float(parts[2])
        totals[category] = totals.get(category, 0) + amount
        counts[category] = counts.get(category, 0) + 1

table = [[c, counts[c], totals[c]] for c in totals]
table.append(["TOTAL", sum(counts.values()), sum(totals.values())])

print(tabulate(table, headers=["category", "count", "total"], tablefmt="github", floatfmt=".2f"))
