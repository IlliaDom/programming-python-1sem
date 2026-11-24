from task3 import Expense, RecurringExpense, SharedExpense, read_csv


class YearlyExpense(Expense):
    def monthly_cost(self):
        return super().monthly_cost() / 12


def main():
    rows = read_csv()
    transport = [r for r in rows if r["category"].lower() == "transport"]
    food = [r for r in rows if r["category"].lower() == "food"]
    other = [r for r in rows if r["category"].lower() not in ("transport", "food")]

    if len(transport) < 2 or len(food) < 2 or len(other) < 2:
        raise ValueError("У CSV недостатньо записів для демонстрації всіх типів витрат.")

    people = int(input("На скількох людей поділити спільні витрати? "))
    if people < 1:
        raise ValueError("Кількість людей має бути не меншою за 1.")
    yearly_amount = float(input("Введіть суму річної підписки у гривнях: "))
    if yearly_amount < 0:
        raise ValueError("Сума не може бути від'ємною.")

    expenses = [
        Expense(other[0]["date"], other[0]["category"], other[0]["amount"]),
        Expense(other[1]["date"], other[1]["category"], other[1]["amount"]),
        RecurringExpense(transport[0]["date"], transport[0]["category"], transport[0]["amount"], 4),
        RecurringExpense(transport[1]["date"], transport[1]["category"], transport[1]["amount"], 4),
        SharedExpense(food[0]["date"], food[0]["category"], food[0]["amount"], people),
        SharedExpense(food[1]["date"], food[1]["category"], food[1]["amount"], people),
        YearlyExpense("2026-01-01", "Річна підписка", yearly_amount),
    ]

    print("\nМісячна вартість витрат з урахуванням річної підписки:")
    total = 0
    for expense in expenses:
        cost = expense.monthly_cost()
        total += cost
        print(f"{expense.category}: {cost:.2f} грн")
    print(f"Загальна сума: {total:.2f} грн")


if __name__ == "__main__":
    main()
