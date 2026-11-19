import csv
from pathlib import Path


class Expense:
    def __init__(self, date: str, category: str, amount: float, comment: str = "") -> None:
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit: float) -> bool:
        return self.amount > limit

    def describe(self) -> str:
        year, month, day = self.date.split("-")
        date_text = f"{day}.{month}.{year}"
        return f"{date_text} {self.category} {self.amount:.2f} ({self.comment})"


def read_expenses(path: Path) -> list[Expense]:
    expenses = []
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            expenses.append(
                Expense(
                    date=row["date"],
                    category=row["category"],
                    amount=float(row["amount"]),
                    comment=row.get("comment") or row.get("note", ""),
                )
            )
    return expenses


def main() -> None:
    data_file = Path(__file__).with_name("expenses.csv")
    expenses = read_expenses(data_file)
    limit = 200.0
    print("Мельник Діана, І-23")
    print(f"Завантажено об'єктів Expense: {len(expenses)}")
    print(f"Великі витрати (понад {limit:.2f} грн):")
    for expense in expenses:
        if expense.is_big(limit):
            print(expense.describe())


if __name__ == "__main__":
    main()
