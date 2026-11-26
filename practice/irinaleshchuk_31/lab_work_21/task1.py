
from datetime import datetime
import csv
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
        return cls(
            data["date"],
            data["category"],
            float(data["amount"]),
            data.get("comment", "")
        )

    @classmethod
    def from_input(cls):
        date = input("Введіть дату (YYYY-MM-DD): ")
        category = input("Введіть категорію: ")
        amount = float(input("Введіть суму: "))
        comment = input("Введіть коментар: ")
        return cls(date, category, amount, comment)


expense = Expense.from_csv_line(
    "2026-11-25;food;120.50;lunch"
)

print("Ірина Лещук, IT-31")
print("Категорія:", expense.category)
print("Сума:", expense.amount)
