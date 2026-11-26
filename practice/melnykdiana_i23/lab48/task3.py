"""Завдання 3. Книга витрат як колекція."""

import csv
from pathlib import Path
from task1 import Money


class ExpenseBook:
    def __init__(self, expenses=(), title="Книга витрат"):
        self.expenses = list(expenses)
        self.title = title

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(expense["category"] == category for expense in self.expenses)

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses, f"{self.title} + {other.title}")

    def total(self):
        return sum((Money(expense["amount"]) for expense in self), Money(0))

    def __gt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total() > budget

    def __str__(self):
        return f"{self.title}: {len(self)} витрат, разом {self.total()}"


def load_expenses():
    with Path(__file__).with_name("expenses.csv").open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def main():
    expenses = load_expenses()
    first_half = ExpenseBook([row for row in expenses if int(row["date"][8:10]) <= 15], "Перша половина місяця")
    second_half = ExpenseBook([row for row in expenses if int(row["date"][8:10]) > 15], "Друга половина місяця")
    combined = first_half + second_half
    print(first_half)
    print(second_half)
    print(combined)
    print(f"Довжина об'єднаної книги дорівнює сумі довжин: {len(combined) == len(first_half) + len(second_half)}")
    print(f"Категорія food є в книзі: {'food' in combined}")
    print(f"Перша витрата: {combined[0]['date']} {combined[0]['category']} {Money(combined[0]['amount'])}")
    print("Перелік категорій: " + ", ".join(row["category"] for row in combined))


if __name__ == "__main__":
    main()
