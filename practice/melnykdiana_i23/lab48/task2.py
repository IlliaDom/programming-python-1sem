"""Завдання 2. Сортування та підсумовування витрат з CSV."""

import csv
from pathlib import Path
from task1 import Money


def main():
    with Path(__file__).with_name("expenses.csv").open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))
    items = [Money(row["amount"]) for row in rows]
    print("Витрати за сумою, від меншої до більшої:")
    print(", ".join(str(item) for item in sorted(items)))
    total = sum(items, Money(0))
    print(f"Кількість записів: {len(items)}")
    print(f"Загальна сума: {total}")
    print("Другий аргумент sum — початкове значення того ж типу Money;")
    print("він дає сумі коректний нуль і дозволяє додавати об'єкти Money.")
    try:
        print(Money(10) + 5)
    except TypeError as error:
        print(f"Money(10) + 5: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
