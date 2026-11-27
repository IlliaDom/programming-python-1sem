from task1 import Money


def load_money(path):
    items = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            date, category, amount, comment = line.strip().split(";")
            items.append(Money(float(amount)))
    return items


items = load_money("data/expenses.csv")
print("count:", len(items))

for item in sorted(items):
    print(item)

total = sum(items, Money(0))
print("total:", total)

try:
    Money(10) + 5
except TypeError as error:
    print("TypeError:", error)
