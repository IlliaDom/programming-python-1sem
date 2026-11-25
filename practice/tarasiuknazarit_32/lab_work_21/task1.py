"""
Завдання 1. Альтернативні конструктори.
Завантажуємо витрати з CSV (from_csv_line) і з JSON (from_dict),
порівнюємо кількість.
"""
import json

from expense import Expense

CSV_FILE = "data/expenses.csv"
JSON_FILE = "data/expenses.json"


def load_from_csv(path: str) -> list[Expense]:
    expenses = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                expenses.append(Expense.from_csv_line(line))
    return expenses


def load_from_json(path: str) -> list[Expense]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [Expense.from_dict(item) for item in data]


def main() -> None:
    from_csv = load_from_csv(CSV_FILE)
    from_json = load_from_json(JSON_FILE)

    print(f"з CSV: {len(from_csv)}")
    print(f"з JSON: {len(from_json)}")

    print("\nперший запис з CSV:", from_csv[0].describe())
    print("перший запис з JSON:", from_json[0].describe())

    # демонстрація from_input() - розкоментуй, щоб ввести витрату вручну
    # manual = Expense.from_input()
    # print("введено вручну:", manual.describe())


if __name__ == "__main__":
    main()
