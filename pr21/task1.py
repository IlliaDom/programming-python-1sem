import json
from pathlib import Path

NAME = "Nazarii Mischuk, IT-32"
BIRTH_DATE = "2009-01-30"
DATA = Path(__file__).parent / "data"


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    @classmethod
    def from_csv_line(cls, line):
        date, category, amount, comment = line.strip().split(";")
        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"], float(data["amount"]), data["comment"])

    @classmethod
    def from_input(cls):
        date = input("date (YYYY-MM-DD): ")
        category = input("category: ")
        amount = float(input("amount: "))
        comment = input("comment: ")
        return cls(date, category, amount, comment)


def load_csv(path):
    expenses = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if line.startswith("#") or not line.strip():
                continue
            expenses.append(Expense.from_csv_line(line))
    return expenses


def load_json(path):
    with open(path, encoding="utf-8") as file:
        records = json.load(file)
    expenses = []
    for record in records:
        expenses.append(Expense.from_dict(record))
    return expenses


print(NAME)
print("birth date:", BIRTH_DATE)

from_csv = load_csv(DATA / "expenses.csv")
from_json = load_json(DATA / "expenses.json")

print("from CSV: ", len(from_csv))
print("from JSON:", len(from_json))

same = len(from_csv) == len(from_json)
for a, b in zip(from_csv, from_json):
    if a.__dict__ != b.__dict__:
        same = False
print("same data:", same)

first = from_csv[0]
print("first:", first.date, first.category, first.amount, first.comment)

print("\nNew expense")
new = Expense.from_input()
print("added:", new.date, new.category, new.amount, new.comment)
