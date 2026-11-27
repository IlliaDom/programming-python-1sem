class Expense:
    """One expense record."""

    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        year, month, day = self.date.split("-")
        return f"{day}.{month}.{year} {self.category} {self.amount:.2f} ({self.comment})"


def read_expenses(path):
    expenses = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            date, category, amount, comment = line.split(";")
            expenses.append(Expense(date, category, float(amount), comment))
    return expenses


expenses = read_expenses("data/expenses.csv")
print("rows:", len(expenses))

LIMIT = 100
for expense in expenses:
    if expense.is_big(LIMIT):
        print(expense.describe())