
from datetime import datetime


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

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
    def from_csv_line(cls, line):
        try:
            date, category, amount, comment = line.strip().split(";")

            if not cls.is_valid_date(date):
                print("Некоректна дата:", date)
                return None

            if not cls.is_valid_amount(amount):
                print("Некоректна сума:", amount)
                return None

            return cls(date, category, float(amount), comment)

        except ValueError:
            print("Некоректний формат рядка")
            return None


print("Ірина Лещук, IT-31")
print("Перевірка дати:", Expense.is_valid_date("2026-02-30"))
print("Перевірка суми:", Expense.is_valid_amount(120.50))

expense = Expense.from_csv_line(
    "2026-11-25;food;120.50;lunch"
)

if expense:
    print("Категорія:", expense.category)
    print("Сума:", expense.amount)
