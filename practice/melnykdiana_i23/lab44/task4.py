"""Завдання 4. Новий клас YearlyExpense без змін у базових класах/циклі."""

from task3 import Expense, RecurringExpense, SharedExpense


class YearlyExpense(Expense):
    def monthly_cost(self):
        return super().monthly_cost() / 12


def main():
    # Цикл залишився тим самим; YearlyExpense додається до списку.
    expenses = [
        RecurringExpense("2026-10-01", "transport", 60, 3),
        RecurringExpense("2026-10-04", "internet", 300, 1),
        SharedExpense("2026-10-02", "food", 220, 2),
        SharedExpense("2026-10-05", "food", 320, 2),
        YearlyExpense("2026-10-06", "subscription", 1200),
    ]
    total = 0
    for expense in expenses:
        cost = expense.monthly_cost()
        total += cost
        print(f"{expense.category:<14} {cost:>7.2f} грн/місяць")
    print(f"Загальна місячна вартість: {total:.2f} грн")


if __name__ == "__main__":
    main()
