
class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        date_parts = self.date.split("-")
        formatted_date = ".".join(reversed(date_parts))
        return (
            f"{formatted_date} {self.category} "
            f"{self.amount:.2f} ({self.comment})"
        )


if __name__ == "__main__":
    expenses = []

    with open("lab_work_18/data/expenses.csv", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            date, category, amount, comment = line.split(";")
            expense = Expense(date, category, amount, comment)
            expenses.append(expense)

    limit = 50

    print("Total expenses:", len(expenses))
    print("Big expenses:")

    for expense in expenses:
        if expense.is_big(limit):
            print(expense.describe())
