from expense_types import Expense, RecurringExpense, SharedExpense


class YearlyExpense(Expense):
    """Річна витрата (наприклад, підписка), що розкладається на 12 місяців."""

    def monthly_cost(self) -> float:
        return self.amount / 12


# той самий список, що й у task3.py, плюс один новий вид витрати
expenses = [
    RecurringExpense("2026-10-01", "transport", 20.0, times_per_month=22),
    RecurringExpense("2026-10-01", "mobile", 150.0, times_per_month=1),
    SharedExpense("2026-10-01", "rent", 12000.0, people=3),
    SharedExpense("2026-10-01", "internet", 400.0, people=3),
    YearlyExpense("2026-01-15", "software subscription", 1800.0),
]


def main() -> None:
    # Цикл - буквально той самий, що й у Завданні 3, без жодної зміни
    total = 0.0
    for expense in expenses:
        print(expense.describe())
        total += expense.monthly_cost()

    print(f"\nзагальна місячна вартість: {total:.2f} UAH")


if __name__ == "__main__":
    main()
