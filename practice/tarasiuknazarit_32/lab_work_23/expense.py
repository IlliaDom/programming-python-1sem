"""Expense model compatible with data/expenses.csv."""
from dataclasses import dataclass


@dataclass
class Expense:
    category: str
    amount: float
    currency: str

    @classmethod
    def from_row(cls, row):
        return cls(row["category"], float(row["amount"]), row["currency"])

    def as_dict(self):
        return {"category": self.category, "amount": self.amount, "currency": self.currency}
