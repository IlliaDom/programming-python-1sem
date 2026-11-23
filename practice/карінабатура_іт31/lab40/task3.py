import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Expense:
    date: str
    category: str
    amount: float
    comment: str = ""

    def is_big(self, limit: float) -> bool:
        return self.amount > limit

    def describe(self) -> str:
        parts: list[str] = []
        if self.date:
            parts.append(self.date)
        parts.append(self.category)
        parts.append(f"{self.amount:.2f}")
        if self.comment:
            parts.append(f"({self.comment})")
        return " ".join(parts)


def load_expenses(csv_path: Path) -> list[Expense]:
    expenses: list[Expense] = []
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = (row.get("category") or "").strip()
            raw_amount = (row.get("amount_uah") or row.get("amount") or "").strip().replace(",", ".")
            if not category or not raw_amount:
                continue
            date_val = (row.get("date") or "").strip()
            comment_val = (row.get("comment") or "").strip()
            expenses.append(
                Expense(
                    date=date_val,
                    category=category,
                    amount=float(raw_amount),
                    comment=comment_val,
                )
            )
    return expenses


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent / "data" / "expenses.csv"
    expenses = load_expenses(csv_path)
    limit = 300.0

    print(f"Кількість об'єктів Expense: {len(expenses)}")
    print(f"Великі витрати (> {limit:.2f}):")
    for item in expenses:
        if item.is_big(limit):
            print(" ", item.describe())