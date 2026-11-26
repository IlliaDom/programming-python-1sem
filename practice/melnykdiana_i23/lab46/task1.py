"""Завдання 1. Альтернативні конструктори Expense."""

import csv
import json
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    @classmethod
    def from_csv_line(cls, line):
        # Підтримує і формат із умови (крапка з комою), і CSV з комами.
        delimiter = ";" if ";" in line else ","
        date, category, amount, comment = next(csv.reader([line], delimiter=delimiter))
        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"], data["amount"],
                   data.get("comment", data.get("note", "")))

    @classmethod
    def from_input(cls):
        date = input("Дата (YYYY-MM-DD): ")
        category = input("Категорія: ")
        amount = input("Сума: ")
        comment = input("Коментар: ")
        return cls(date, category, float(amount), comment)

    def as_tuple(self):
        return self.date, self.category, self.amount, self.comment


def main():
    folder = Path(__file__).parent
    with (folder / "expenses.csv").open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        csv_expenses = [Expense.from_dict(row) for row in reader]
    with (folder / "expenses.json").open(encoding="utf-8") as file:
        json_expenses = [Expense.from_dict(row) for row in json.load(file)]

    print(f"Записів у CSV:  {len(csv_expenses)}")
    print(f"Записів у JSON: {len(json_expenses)}")
    print(f"Дані збігаються: {len(csv_expenses) == len(json_expenses) and all(a.as_tuple() == b.as_tuple() for a, b in zip(csv_expenses, json_expenses))}")
    sample = Expense.from_csv_line("2026-09-21;food;85.50;lunch")
    print(f"Приклад із рядка CSV: {sample.category}, {sample.amount:.2f}")
    print(f"Перший запис JSON: {json_expenses[0].category}, {json_expenses[0].amount:.2f}, {json_expenses[0].comment}")


if __name__ == "__main__":
    main()
