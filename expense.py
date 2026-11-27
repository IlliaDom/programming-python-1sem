
import csv
import json
from datetime import datetime


class Expense:
    currency = "UAH"
    created = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment
        Expense.created += 1

    @classmethod
    def from_csv_line(cls, line):
        try:
            date, category, amount, comment = line.strip().split(";", 3)

            if not cls.is_valid_date(date):
                raise ValueError("неправильна дата")

            if not cls.is_valid_amount(amount):
                raise ValueError("неправильна сума")

            return cls(date, category, float(amount), comment)

        except ValueError as error:
            print(f"Рядок пропущено: {line.strip()} ({error})")
            return None

    @classmethod
    def from_dict(cls, data):
        date = str(data["date"])
        amount = data["amount"]

        if not cls.is_valid_date(date):
            raise ValueError("Неправильна дата у JSON")

        if not cls.is_valid_amount(amount):
            raise ValueError("Неправильна сума у JSON")

        return cls(
            date,
            data["category"],
            float(amount),
            data.get("comment", "")
        )

    @classmethod
    def from_input(cls):
        date = input("Введіть дату (YYYY-MM-DD): ")
        category = input("Введіть категорію: ")
        amount = input("Введіть суму: ")
        comment = input("Введіть коментар: ")

        if not cls.is_valid_date(date):
            print("Помилка: неправильний формат дати")
            return None

        if not cls.is_valid_amount(amount):
            print("Помилка: неправильна сума")
            return None

        return cls(date, category, float(amount), comment)

    @staticmethod
    def is_valid_date(text):
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return True
        except ValueError:
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

    def __str__(self):
        return (
            f"{self.date} | {self.category} | "
            f"{self.amount:.2f} {self.currency} | {self.comment}"
        )


def load_csv(filename):
    expenses = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            if not line.strip():
                continue

            if line.lower().startswith("date;"):
                continue

            expense = Expense.from_csv_line(line)

            if expense is not None:
                expenses.append(expense)

    return expenses


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        data = data["expenses"]

    return [Expense.from_dict(item) for item in data]


if __name__ == "__main__":
    csv_expenses = load_csv("data/expenses.csv")
    json_expenses = load_json("data/expenses.json")

    print("Витрати з CSV:")
    for expense in csv_expenses:
        print(expense)

    print("\nВитрати з JSON:")
    for expense in json_expenses:
        print(expense)

    print("\nКількість витрат:")
    print("CSV:", len(csv_expenses))
    print("JSON:", len(json_expenses))

    print("\nКількість створених об'єктів:", Expense.created)