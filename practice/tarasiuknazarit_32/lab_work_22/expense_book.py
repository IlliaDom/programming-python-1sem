"""
Expense і ExpenseBook: книга витрат, що поводиться як колекція
(len, in, for, [], +) і має людиночитний str() (Завдання 3), а також
порівняння з бюджетом (Завдання 4).
"""
import csv

from money import Money


class Expense:
    def __init__(self, date: str, category: str, amount: Money, comment: str = ""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def __str__(self) -> str:
        return f"{self.date} {self.category}: {self.amount}"


class ExpenseBook:
    def __init__(self, expenses: list[Expense] | None = None):
        self.expenses: list[Expense] = list(expenses) if expenses else []

    def add(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def total(self) -> Money:
        return sum((e.amount for e in self.expenses), Money(0))

    def __len__(self) -> int:
        return len(self.expenses)

    def __contains__(self, category: str) -> bool:
        return any(e.category == category for e in self.expenses)

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses)

    def __str__(self) -> str:
        return f"ExpenseBook: {len(self)} витрат, усього {self.total()}"

    def __gt__(self, budget: Money):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total().cents > budget.cents

    def __lt__(self, budget: Money):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total().cents < budget.cents

    @classmethod
    def from_csv(cls, path: str) -> "ExpenseBook":
        book = cls()
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                book.add(
                    Expense(
                        date=row["date"],
                        category=row["category"],
                        amount=Money(float(row["amount"])),
                        comment=row.get("comment", ""),
                    )
                )
        return book
