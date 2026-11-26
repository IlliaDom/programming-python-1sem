import csv
from pathlib import Path
from task1 import Money


class ExpenseBook:
    def __init__(self, expenses=None):
        self.expenses = list(expenses) if expenses is not None else []

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(
            expense["category"].casefold() == str(category).casefold()
            for expense in self.expenses
        )

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses)

    def __gt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total > budget

    @property
    def total(self):
        return sum(
            (expense["amount"] for expense in self.expenses),
            Money(0)
        )

    def __str__(self):
        return f"Книга витрат: {len(self)} записів, загальна сума {self.total}"


def load_expenses():
    file_path = Path(__file__).parent / "data" / "expenses.csv"
    result = []
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file, delimiter=";"):
            result.append({
                "date": row["date"],
                "category": row["category"],
                "amount": Money(row["amount"]),
                "note": row["note"]
            })
    return result


if __name__ == "__main__":
    expenses = load_expenses()
    first_half = ExpenseBook([
        expense for expense in expenses
        if int(expense["date"].split("-")[2]) <= 15
    ])
    second_half = ExpenseBook([
        expense for expense in expenses
        if int(expense["date"].split("-")[2]) > 15
    ])
    combined = first_half + second_half

    print("Перша половина місяця:", first_half)
    print("Друга половина місяця:", second_half)
    print("Об'єднана книга:", combined)
    print("Кількість записів:", len(combined))
    print("Перевірка категорії Food:", "Food" in combined)
    print("Перший запис:", combined[0])
    print("Перебір витрат:")
    for expense in combined:
        print(expense["date"], expense["category"], expense["amount"])
