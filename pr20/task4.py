import task3
from task3 import GROUP, NAME, SURNAME, Expense


class YearlyExpense(Expense):
    """Річна підписка: сума / 12."""
    def __init__(self, date, category, amount):
        super().__init__(date, category, amount)

    def monthly_cost(self):
        return self.amount / 12


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    # ті самі витрати + нова, код базового класу і цикл не змінювалися
    expenses = task3.build_expenses()
    expenses.append(YearlyExpense("2026-11-01", "subscription", 1200.00))

    total = 0.0
    for e in expenses:
        cost = e.monthly_cost()
        total += cost
        print(f"{type(e).__name__:<17} {e.category:<12} {cost:>9.2f}")
    print(f"{'total':<30} {total:>9.2f}")


if __name__ == "__main__":
    main()
