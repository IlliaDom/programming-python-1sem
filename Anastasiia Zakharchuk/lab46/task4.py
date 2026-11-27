class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, source, amount):
        self.source = source
        self.amount = amount

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, from_card, to_card, amount):
        self.from_card = from_card
        self.to_card = to_card
        self.amount = amount

    def balance_change(self):
        return 0


def load_expenses(path):
    expenses = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            date, category, amount, comment = line.strip().split(";")
            expenses.append(Expense(category, float(amount)))
    return expenses


expenses = load_expenses("data/expenses.csv")
incomes = [
    Income("scholarship", 1700.00),
    Income("part-time job", 900.00),
]
transfers = [
    Transfer("main card", "savings card", 500.00),
    Transfer("main card", "savings card", 300.00),
]

operations = incomes + expenses + transfers

balance = 0
for operation in operations:
    balance += operation.balance_change()

income_total = sum(item.balance_change() for item in incomes)
expense_total = sum(item.balance_change() for item in expenses)
transfer_total = sum(item.balance_change() for item in transfers)

print("Anastasia Zakharchuk, IT-32")
print(f"{'income:':<10}{income_total:>8.2f}")
print(f"{'expenses:':<10}{expense_total:>8.2f}")
print(f"{'transfers:':<10}{transfer_total:>8.2f}")
print(f"{'balance:':<10}{balance:>8.2f}")
