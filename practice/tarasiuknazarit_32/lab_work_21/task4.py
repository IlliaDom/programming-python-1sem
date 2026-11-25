"""
Завдання 4. Поліморфізм.
Expense, Income і Transfer - три незалежні класи без спільного предка.
У кожного свій balance_change(): цикл викликає цей метод однаково для
всіх обʼєктів, не перевіряючи тип.
"""

# TODO: заміни на свої справжні імʼя, прізвище та групу
STUDENT = "Назар Прізвище, ГР-11"


class Expense:
    def __init__(self, category: str, amount: float, comment: str = ""):
        self.category = category
        self.amount = amount
        self.comment = comment

    def balance_change(self) -> float:
        return -abs(self.amount)

    def kind(self) -> str:
        return "expense"


class Income:
    def __init__(self, source: str, amount: float):
        self.source = source
        self.amount = amount

    def balance_change(self) -> float:
        return abs(self.amount)

    def kind(self) -> str:
        return "income"


class Transfer:
    def __init__(self, amount: float, comment: str = ""):
        self.amount = amount
        self.comment = comment

    def balance_change(self) -> float:
        return 0.0

    def kind(self) -> str:
        return "transfer"


# TODO: заміни на свій реальний місячний список операцій
transactions = [
    Income("стипендія", 2000.0),
    Income("підробіток", 600.0),
    Expense("food", 459.00),
    Expense("transport", 120.00),
    Expense("entertainment", 200.00),
    Expense("utilities", 299.50),
    Expense("food", 169.50),
    Transfer(500.0, "своя картка -> своя картка"),
]


def main() -> None:
    print(STUDENT)

    totals = {"income": 0.0, "expense": 0.0, "transfer": 0.0}
    balance = 0.0

    for transaction in transactions:
        change = transaction.balance_change()  # без жодної перевірки типу
        balance += change
        totals[transaction.kind()] += change

    rows = [
        ("income:", totals["income"]),
        ("expenses:", totals["expense"]),
        ("transfers:", totals["transfer"]),
        ("balance:", balance),
    ]
    for label, value in rows:
        print(f"{label:<10}{value:>9.2f}")


if __name__ == "__main__":
    main()
