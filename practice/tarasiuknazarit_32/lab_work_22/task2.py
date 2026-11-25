"""
Завдання 2. Сортування та сума.
sorted() працює завдяки __lt__; sum() потребує стартове значення
Money(0); Money(10) + 5 завершується TypeError, бо __add__
повертає NotImplemented для непідтримуваних типів.
"""
import csv

from money import Money

EXPENSES_FILE = "data/expenses.csv"


def load_amounts(path: str) -> list[Money]:
    amounts = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            amounts.append(Money(float(row["amount"])))
    return amounts


def main() -> None:
    amounts = load_amounts(EXPENSES_FILE)

    print("відсортовано:")
    for money in sorted(amounts):
        print(" -", money)

    # sum() за замовчуванням починає з int 0, а 0 + Money(...) не має
    # сенсу (різні типи) - тому обов'язково передаємо стартове значення
    # того ж типу, Money(0), інакше перше ж додавання впаде з помилкою.
    total = sum(amounts, Money(0))
    print("\nзагальна сума:", total)

    # Money(10) + 5: __add__ бачить, що 5 - не Money, повертає
    # NotImplemented; Python тоді пробує 5.__radd__(Money(10)),
    # якого теж немає - і зрештою генерує TypeError.
    try:
        Money(10) + 5
    except TypeError as exc:
        print(f"\nerror: {exc}")


if __name__ == "__main__":
    main()
