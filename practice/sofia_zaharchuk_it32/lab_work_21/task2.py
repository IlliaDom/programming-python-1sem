"""Practice 21, task 2: static validation methods."""
import json
from datetime import datetime

NAME = "Sofiia Zakharchuk"
GROUP = "IT-32"
CSV_PATH = "data/expenses.csv"
JSON_PATH = "data/expenses.json"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @staticmethod
    def is_valid_date(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            return float(value) > 0
        except (ValueError, TypeError):
            return False

    @classmethod
    def _build(cls, date, category, amount, comment=""):
        if not cls.is_valid_date(date):
            raise ValueError(f"bad date {date!r}")
        if not cls.is_valid_amount(amount):
            raise ValueError(f"bad amount {amount!r}")
        if not str(category).strip():
            raise ValueError("empty category")
        return cls(date, str(category).strip(), float(amount), comment)

    @classmethod
    def from_csv_line(cls, line):
        sep = ";" if ";" in line else ","
        parts = [p.strip() for p in line.strip().split(sep, 3)]
        if len(parts) < 3:
            raise ValueError(f"expected 3-4 fields, got {len(parts)}")
        comment = parts[3] if len(parts) > 3 else ""
        return cls._build(parts[0], parts[1], parts[2], comment)

    @classmethod
    def from_dict(cls, data):
        return cls._build(data["date"], data["category"], data["amount"], data.get("comment", ""))

    def __repr__(self):
        return f"Expense({self.date}, {self.category!r}, {self.amount}, {self.comment!r})"


def load_csv(path):
    expenses = []
    with open(path, encoding="utf-8-sig") as file:
        for number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            if number == 1 and not line.strip()[0].isdigit():
                continue  # header row
            try:
                expenses.append(Expense.from_csv_line(line))
            except ValueError as error:
                print(f"skip line {number}: {error}")
    return expenses


if __name__ == "__main__":
    print(f"{NAME}, {GROUP}")
    print(Expense.is_valid_date("2026-02-28"), Expense.is_valid_date("2026-02-30"))
    print(Expense.is_valid_amount("85.5"), Expense.is_valid_amount("-3"), Expense.is_valid_amount("abc"))

    test_lines = [
        "2026-09-21;food;85.50;lunch",
        "2026-02-30;food;50;wrong date",
        "2026-09-22;transport;abc;wrong amount",
        "2026-09-23;transport;-10;negative",
        "2026-09-24;coffee",
    ]
    print("--- test lines ---")
    for number, line in enumerate(test_lines, start=1):
        try:
            print("ok:", Expense.from_csv_line(line))
        except ValueError as error:
            print(f"skip line {number}: {error}")

    print("--- real data ---")
    expenses = load_csv(CSV_PATH)
    print("loaded:", len(expenses))
