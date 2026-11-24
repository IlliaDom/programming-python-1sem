
"""Практична робота №46 (П21).
Поліморфізм, методи класу та статичні методи.
"""

import csv
import json
from datetime import datetime
from pathlib import Path


class Expense:
    currency = "UAH"
    created_count = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment
        Expense.created_count += 1

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
            amount = float(value)
            return amount >= 0 and amount != float("inf") and amount == amount
        except (ValueError, TypeError):
            return False

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(";", 3)

        if len(parts) != 4:
            raise ValueError("Неправильна кількість полів")

        date, category, amount, comment = parts

        if not cls.is_valid_date(date):
            raise ValueError("Некоректна дата")

        if not cls.is_valid_amount(amount):
            raise ValueError("Некоректна сума")

        if not category.strip():
            raise ValueError("Порожня категорія")

        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        date = str(data["date"])
        category = str(data["category"]).strip()
        amount = data["amount"]
        comment = data.get("comment", data.get("description", ""))

        if not cls.is_valid_date(date):
            raise ValueError("Некоректна дата")

        if not cls.is_valid_amount(amount):
            raise ValueError("Некоректна сума")

        if not category:
            raise ValueError("Порожня категорія")

        return cls(date, category, float(amount), comment)

    @classmethod
    def from_input(cls):
        date = input("Дата (YYYY-MM-DD): ").strip()
        category = input("Категорія: ").strip()
        amount = input("Сума: ").strip().replace(",", ".")
        comment = input("Коментар: ").strip()

        if not cls.is_valid_date(date):
            raise ValueError("Некоректна дата")

        if not cls.is_valid_amount(amount):
            raise ValueError("Некоректна сума")

        if not category:
            raise ValueError("Порожня категорія")

        return cls(date, category, float(amount), comment)

    @classmethod
    def set_currency(cls, code):
        code = str(code).strip().upper()
        if not code:
            raise ValueError("Вкажіть валюту")
        cls.currency = code

    def __str__(self):
        return (
            f"{self.date} | {self.category:<14} | "
            f"{self.amount:8.2f} {self.currency} | {self.comment}"
        )


def load_csv(path):
    expenses = []

    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=";")

        for number, row in enumerate(reader, start=1):
            if not row:
                continue

            if row[0].strip().lower() == "date":
                continue

            try:
                line = ";".join(row)
                expenses.append(Expense.from_csv_line(line))
            except ValueError as error:
                print(f"Рядок {number} пропущено: {error}")

    return expenses


def load_json(path):
    expenses = []

    with path.open(encoding="utf-8") as file:
        records = json.load(file)

    for number, record in enumerate(records, start=1):
        try:
            expenses.append(Expense.from_dict(record))
        except (KeyError, ValueError, TypeError) as error:
            print(f"Запис {number} пропущено: {error}")

    return expenses


def main():
    data_dir = Path(__file__).parent / "data"

    csv_expenses = load_csv(data_dir / "expenses.csv")
    json_expenses = load_json(data_dir / "expenses.json")

    print("Вовк Марія Віталіївна, група І-23")
    print("Дата народження: 02.12.2008")

    print("\nВитрати з CSV:")
    for expense in csv_expenses:
        print(expense)

    print("\nВитрати з JSON:")
    for expense in json_expenses:
        print(expense)

    csv_data = [
        (e.date, e.category, e.amount, e.comment)
        for e in csv_expenses
    ]
    json_data = [
        (e.date, e.category, e.amount, e.comment)
        for e in json_expenses
    ]

    print("\nКількість записів CSV:", len(csv_expenses))
    print("Кількість записів JSON:", len(json_expenses))
    print("Дані CSV та JSON однакові:", csv_data == json_data)

    print("\nПеревірка статичних методів:")
    print(
        "Дата 2026-02-30:",
        Expense.is_valid_date("2026-02-30")
    )
    print(
        "Сума 125.50:",
        Expense.is_valid_amount("125.50")
    )

    print("\nЗмінна класу:")
    print("Створено об'єктів:", Expense.created_count)

    Expense.set_currency("USD")

    print("Після зміни валюти:")
    for expense in csv_expenses[:2]:
        print(expense)


if __name__ == "__main__":
    main()
