"""
Клас Expense: альтернативні конструктори (Завдання 1), статичні
методи-перевірки (Завдання 2), змінна класу currency і лічильник
(Завдання 3). Логіка розбору рядків/словників не потрапляє в __init__.
"""
import datetime


class Expense:
    currency = "UAH"  # змінна класу - спільна для всіх витрат
    count = 0  # лічильник створених обʼєктів

    def __init__(self, date: str, category: str, amount: float, comment: str = ""):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
        Expense.count += 1

    @classmethod
    def from_csv_line(cls, line: str) -> "Expense | None":
        date, category, amount, comment = line.strip().split(";")

        if not cls.is_valid_date(date):
            print(f"пропущено (некоректна дата): {line.strip()}")
            return None
        if not cls.is_valid_amount(amount):
            print(f"пропущено (некоректна сума): {line.strip()}")
            return None

        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            date=data["date"],
            category=data["category"],
            amount=float(data["amount"]),
            comment=data.get("comment", ""),
        )

    @classmethod
    def from_input(cls) -> "Expense":
        date = input("дата (YYYY-MM-DD): ").strip()
        category = input("категорія: ").strip()
        amount = input("сума: ").strip()
        comment = input("коментар (можна пусто): ").strip()
        return cls(date, category, float(amount), comment)

    @staticmethod
    def is_valid_date(text: str) -> bool:
        try:
            datetime.datetime.strptime(text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_amount(value) -> bool:
        try:
            return float(value) >= 0
        except (TypeError, ValueError):
            return False

    @classmethod
    def set_currency(cls, code: str) -> None:
        cls.currency = code

    def describe(self) -> str:
        comment = f" ({self.comment})" if self.comment else ""
        return f"{self.date} {self.category}: {self.amount:.2f} {Expense.currency}{comment}"
