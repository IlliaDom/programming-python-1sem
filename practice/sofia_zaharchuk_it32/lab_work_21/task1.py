"""Practice 21, task 1: alternative constructors with @classmethod."""
import json
import sys

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

    @classmethod
    def from_csv_line(cls, line):
        sep = ";" if ";" in line else ","
        date, category, amount, *rest = [p.strip() for p in line.strip().split(sep, 3)]
        return cls(date, category, float(amount), rest[0] if rest else "")

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"], float(data["amount"]), data.get("comment", ""))

    @classmethod
    def from_input(cls):
        date = input("date (YYYY-MM-DD): ").strip()
        category = input("category: ").strip()
        amount = float(input("amount: "))
        comment = input("comment: ").strip()
        return cls(date, category, amount, comment)

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
                print(f"skip csv line {number}: {error}")
    return expenses


def load_json(path):
    with open(path, encoding="utf-8-sig") as file:
        data = json.load(file)
    if isinstance(data, dict):  # {"expenses": [...]}
        data = next((v for v in data.values() if isinstance(v, list)), [])
    expenses = []
    for number, item in enumerate(data, start=1):
        try:
            expenses.append(Expense.from_dict(item))
        except (ValueError, KeyError, TypeError) as error:
            print(f"skip json item {number}: {error!r}")
    return expenses


if __name__ == "__main__":
    print(f"{NAME}, {GROUP}")
    expense = Expense.from_csv_line("2026-09-21;food;85.50;lunch")
    print(expense.category, expense.amount)
    print(Expense.from_dict({"date": "2026-09-22", "category": "transport", "amount": "30"}))

    from_csv = load_csv(CSV_PATH)
    from_json = load_json(JSON_PATH)
    print("from csv: ", len(from_csv))
    print("from json:", len(from_json))
    print("same data:", [vars(e) for e in from_csv] == [vars(e) for e in from_json])

    if "--input" in sys.argv:
        print(Expense.from_input())
