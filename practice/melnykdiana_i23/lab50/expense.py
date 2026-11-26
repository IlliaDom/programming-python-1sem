"""Клас Expense, використаний у практичній роботі № 46."""


class Expense:
    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    @classmethod
    def from_dict(cls, data):
        return cls(data["date"], data["category"], data["amount"],
                   data.get("comment", data.get("note", "")))

    def as_dict(self):
        return {"date": self.date, "category": self.category,
                "amount": self.amount, "comment": self.comment}
