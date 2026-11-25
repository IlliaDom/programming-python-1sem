from expense_types import RecurringExpense, SharedExpense

# TODO: заміни на свої реальні витрати
expenses = [
    RecurringExpense("2026-10-01", "transport", 20.0, times_per_month=22),
    RecurringExpense("2026-10-01", "mobile", 150.0, times_per_month=1),
    SharedExpense("2026-10-01", "rent", 12000.0, people=3),
    SharedExpense("2026-10-01", "internet", 400.0, people=3),
]


def main() -> None:
    total = 0.0
    for expense in expenses:
        print(expense.describe())
        total += expense.monthly_cost()  # жодного if isinstance(...)

    print(f"\nзагальна місячна вартість: {total:.2f} UAH")


if __name__ == "__main__":
    main()
