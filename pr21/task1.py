import json
import sys
from datetime import datetime
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

BASE = Path(__file__).resolve().parent
CSV_FILE = BASE / "data" / "expenses.csv"
JSON_FILE = BASE / "data" / "expenses.json"


class Expense:
    currency = "UAH"    
    count = 0            

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.count += 1

   
    @classmethod
    def from_csv_line(cls, line):
        """Рядок CSV -> Expense. Некоректний рядок -> ValueError."""
        parts = line.strip().split(";")
        if len(parts) != 4:
            raise ValueError(f"expected 4 fields, got {len(parts)}")
        date, category, amount, comment = (p.strip() for p in parts)
        if not cls.is_valid_date(date):
            raise ValueError(f"bad date: {date!r}")
        if not cls.is_valid_amount(amount):
            raise ValueError(f"bad amount: {amount!r}")
        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"],
                   float(data["amount"]), data.get("comment", ""))

    @classmethod
    def from_input(cls):
        date = input("date (YYYY-MM-DD): ").strip()
        category = input("category: ").strip()
        amount = input("amount: ").strip()
        comment = input("comment: ").strip()
        if not cls.is_valid_date(date) or not cls.is_valid_amount(amount):
            raise ValueError("invalid date or amount")
        return cls(date, category, float(amount), comment)

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
        cls.currency = code

    def balance_change(self):
        return -self.amount

    def __eq__(self, other):
        return (isinstance(other, Expense)
                and (self.date, self.category, self.amount, self.comment)
                == (other.date, other.category, other.amount, other.comment))

    def __str__(self):
        return (f"{self.date} {self.category} "
                f"{self.amount:.2f} {self.currency} ({self.comment})")


def load_csv(path):
    expenses = []
    with path.open(encoding="utf-8-sig") as f:
        for number, line in enumerate(f, start=1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            try:
                expenses.append(Expense.from_csv_line(line))
            except ValueError as e:
                print(f"warning: line {number} skipped ({e}): {line.strip()}",
                      file=sys.stderr)
    return expenses


def load_json(path):
    with path.open(encoding="utf-8-sig") as f:
        return [Expense.from_dict(item) for item in json.load(f)]


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    for path in (CSV_FILE, JSON_FILE):
        if not path.is_file():
            print(f"error: {path} not found", file=sys.stderr)
            sys.exit(1)

    from_csv = load_csv(CSV_FILE)
    from_json = load_json(JSON_FILE)
    print(f"from CSV:  {len(from_csv)} expenses")
    print(f"from JSON: {len(from_json)} expenses")
    print("same count:", len(from_csv) == len(from_json))
    print("same data: ", from_csv == from_json)
    print("first from CSV: ", from_csv[0])
    print("first from JSON:", from_json[0])


if __name__ == "__main__":
    main()
