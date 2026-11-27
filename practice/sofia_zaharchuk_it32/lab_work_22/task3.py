"""Practice 22, task 3: ExpenseBook, a custom collection."""
from task1 import CSV_PATH, GROUP, NAME, Expense, Money, load_expenses


class ExpenseBook:
    def __init__(self, expenses=()):
        self._expenses = list(expenses)

    def __len__(self):
        return len(self._expenses)

    def __contains__(self, category):
        return any(e.category == category for e in self._expenses)

    def __iter__(self):
        return iter(self._expenses)

    def __getitem__(self, index):
        return self._expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return type(self)(self._expenses + other._expenses)

    def total(self):
        return sum((e.money for e in self._expenses), Money(0))

    def __str__(self):
        return f"ExpenseBook: {len(self)} expenses, total {self.total()}"

    def __repr__(self):
        return f"ExpenseBook({len(self)} items)"


def split_by_half(expenses):
    first = [e for e in expenses if e.date.day <= 15]
    second = [e for e in expenses if e.date.day > 15]
    return ExpenseBook(first), ExpenseBook(second)


if __name__ == "__main__":
    print(f"{NAME}, {GROUP}")
    first, second = split_by_half(load_expenses(CSV_PATH))
    print("first half: ", first)
    print("second half:", second)

    month = first + second
    print("merged:     ", month)
    print("len check:", len(month), "==", len(first), "+", len(second), "->", len(month) == len(first) + len(second))

    categories = sorted({e.category for e in month})
    print("categories:", ", ".join(categories))
    print("in:", categories[0] in month, "| 'unicorn' in:", "unicorn" in month)
    print("book[0]:", month[0])
    print("book[-1]:", month[-1])
    print("book[1:3]:", len(month[1:3]), "items")
    print("--- first 3 by iteration ---")
    for number, expense in enumerate(month):
        if number == 3:
            break
        print(f"{expense.date}  {expense.category:<12}{expense.money}")
    print("bool(empty book):", bool(ExpenseBook()))
    try:
        month + 5
    except TypeError as error:
        print("error:", error)
