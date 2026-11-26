"""Завдання 2. Статичні методи перевірки даних."""

from datetime import datetime
from task1 import Expense as BaseExpense


class Expense(BaseExpense):
    @staticmethod
    def is_valid_date(text):
        try:
            parsed = datetime.strptime(text, "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d") == text
        except (TypeError, ValueError):
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            amount = float(value)
            return amount >= 0 and amount != float("inf") and amount == amount
        except (TypeError, ValueError):
            return False

    @classmethod
    def from_csv_line(cls, line):
        delimiter = ";" if ";" in line else ","
        import csv
        parts = next(csv.reader([line], delimiter=delimiter))
        if len(parts) != 4:
            raise ValueError("Очікується чотири поля")
        date, category, amount, comment = parts
        if not cls.is_valid_date(date):
            raise ValueError(f"некоректна дата: {date}")
        if not category.strip():
            raise ValueError("порожня категорія")
        if not cls.is_valid_amount(amount):
            raise ValueError(f"некоректна сума: {amount}")
        return cls(date, category, float(amount), comment)


def main():
    print(f"Дата 2026-02-30 коректна: {Expense.is_valid_date('2026-02-30')}")
    print(f"Дата 2026-10-01 коректна: {Expense.is_valid_date('2026-10-01')}")
    print(f"Сума 12.50 коректна: {Expense.is_valid_amount('12.50')}")
    print(f"Сума -5 коректна: {Expense.is_valid_amount('-5')}")
    lines = ["2026-10-01;transport;60;Проїзд",
             "2026-02-30;food;100;некоректна дата",
             "2026-10-02;food;не число;некоректна сума"]
    accepted = []
    for line in lines:
        try:
            accepted.append(Expense.from_csv_line(line))
        except ValueError as error:
            print(f"Рядок пропущено: {error}")
    print(f"Коректних тестових рядків: {len(accepted)}")


if __name__ == "__main__":
    main()
