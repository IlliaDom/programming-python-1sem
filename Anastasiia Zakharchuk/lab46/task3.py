class Expense:
    currency = "UAH"
    count = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.count += 1

    @classmethod
    def set_currency(cls, code):
        cls.currency = code

    def describe(self):
        return f"{self.date} {self.category} {self.amount:.2f} {self.currency} ({self.comment})"


def load_csv(path):
    expenses = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            date, category, amount, comment = line.strip().split(";")
            expenses.append(Expense(date, category, float(amount), comment))
    return expenses


expenses = load_csv("data/expenses.csv")
print("created:", Expense.count)

print(expenses[0].describe())
print(expenses[-1].describe())

Expense.set_currency("USD")

print(expenses[0].describe())
print(expenses[-1].describe())
print(expenses[0].__dict__)
print("currency" in expenses[0].__dict__, "currency" in Expense.__dict__)
