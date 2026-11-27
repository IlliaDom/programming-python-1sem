from task1 import Money


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def __str__(self):
        year, month, day = self.date.split("-")
        return f"{day}.{month}.{year} {self.category} {self.amount} ({self.comment})"


class ExpenseBook:
    def __init__(self, expenses=None):
        self.expenses = list(expenses or [])

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(e.category == category for e in self.expenses)

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses)

    def total(self):
        return sum((e.amount for e in self.expenses), Money(0))

    def __str__(self):
        return f"{len(self)} expenses, total {self.total()}"


def load_expenses(path):
    expenses = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if not line.strip() or line.startswith("#"):
                continue
            date, category, amount, comment = line.strip().split(";")
            expenses.append(Expense(date, category, Money(float(amount)), comment))
    return expenses


if __name__ == "__main__":
    all_expenses = load_expenses("data/expenses.csv")

    first = ExpenseBook(e for e in all_expenses if int(e.date.split("-")[2]) <= 15)
    second = ExpenseBook(e for e in all_expenses if int(e.date.split("-")[2]) > 15)

    print("first half:", first)
    print("second half:", second)

    book = first + second
    print("merged:", book)
    print("len:", len(book), len(first) + len(second))
    print("food" in book, "cinema" in book)
    print(book[0])

    for expense in book:
        print(expense)
