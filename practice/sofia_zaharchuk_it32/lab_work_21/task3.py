"""Practice 21, task 3: class variables and a class method."""
import json
from datetime import datetime

NAME = "Sofiia Zakharchuk"
GROUP = "IT-32"
CSV_PATH = "data/expenses.csv"
JSON_PATH = "data/expenses.json"


class Expense:
    currency = "UAH"
    created = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.created += 1

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
    def set_currency(cls, code):
        if not code.strip():
            raise ValueError("currency code can not be empty")
        cls.currency = code.strip().upper()

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

    def __str__(self):
        return f"{self.date}  {self.category:<12} {self.amount:>9.2f} {self.currency}"


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
    expenses = load_csv(CSV_PATH)
    print("created:", Expense.created)
    print("--- currency", Expense.currency, "---")
    for expense in expenses[:3]:
        print(expense)

    Expense.set_currency("USD")
    print("--- after set_currency('USD') ---")
    for expense in expenses[:3]:
        print(expense)
    print("class:", Expense.currency, "| object:", expenses[0].currency)

    # a mistake from the lecture: assignment through self creates an own attribute
    expenses[0].currency = "EUR"
    Expense.set_currency("PLN")
    print("--- after self.currency = 'EUR' on the first object, then set_currency('PLN') ---")
    print(expenses[0])
    print(expenses[1])
