import csv
import datetime


class Expense:
    def __init__(self, date: str, category: str, amount: float, comment: str = ""):
        # date зберігаємо як date-об'єкт, щоб легко сортувати і форматувати
        self.date = datetime.date.fromisoformat(date)
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit: float) -> bool:
        return self.amount > limit

    def describe(self) -> str:
        line = f"{self.date.strftime('%d.%m.%Y')} {self.category} {self.amount:.2f}"
        if self.comment:
            line += f" ({self.comment})"
        return line


class ExpenseBook:
    def __init__(self):
        self.expenses: list[Expense] = []

    def add(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def total(self) -> float:
        return sum(e.amount for e in self.expenses)

    def by_category(self, category: str) -> float:
        return sum(e.amount for e in self.expenses if e.category == category)

    def top(self, n: int) -> list[Expense]:
        return sorted(self.expenses, key=lambda e: e.amount, reverse=True)[:n]

    @classmethod
    def from_csv(cls, path: str) -> "ExpenseBook":
        book = cls()
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                book.add(
                    Expense(
                        date=row["date"],
                        category=row["category"],
                        amount=row["amount"],
                        comment=row.get("comment", ""),
                    )
                )
        return book
