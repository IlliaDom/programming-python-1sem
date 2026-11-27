import json


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
        comment = data.get("comment", data.get("note", ""))
        return cls(data["date"], data["category"], float(data["amount"]), comment)

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
            if not line.strip() or line.startswith("#"):
                continue
            expenses.append(Expense.from_csv_line(line))
    return expenses


def load_json(path):
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    return [Expense.from_dict(item) for item in data]


from_csv = load_csv("data/expenses.csv")
from_json = load_json("data/expenses.json")

print("csv:", len(from_csv))
print("json:", len(from_json))
print("same count:", len(from_csv) == len(from_json))

first_csv = from_csv[0]
first_json = from_json[0]
print(first_csv.date, first_csv.category, first_csv.amount, first_csv.comment)
print(first_json.date, first_json.category, first_json.amount, first_json.comment)
print("same data:", first_csv.__dict__ == first_json.__dict__)
