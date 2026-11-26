from datetime import date


class Expense:
    currency = "UAH"
    objects_created = 0

    def __init__(self, expense_date, category, amount, description):
        self.date = self.validate_date(expense_date)
        self.category = str(category).strip()
        self.amount = self.validate_amount(amount)
        self.description = str(description).strip()
        type(self).objects_created += 1

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(";")
        if len(parts) != 4:
            raise ValueError("Рядок CSV повинен містити чотири поля")
        return cls(parts[0], parts[1], parts[2], parts[3])

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"], data["amount"], data["description"])

    @classmethod
    def from_input(cls):
        return cls(
            input("Дата: "),
            input("Категорія: "),
            input("Сума: "),
            input("Опис: ")
        )

    @staticmethod
    def validate_date(value):
        return date.fromisoformat(str(value)).isoformat()

    @staticmethod
    def validate_amount(value):
        amount = round(float(value), 2)
        if amount < 0:
            raise ValueError("Сума не може бути від'ємною")
        return amount

    @classmethod
    def set_currency(cls, currency):
        cls.currency = currency

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

    def __repr__(self):
        return (
            f"Expense({self.date!r}, {self.category!r}, "
            f"{self.amount!r}, {self.description!r})"
        )
