import csv
from pathlib import Path
from task1 import Money


def load_expenses():
    file_path = Path(__file__).parent / "data" / "expenses.csv"
    expenses = []
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file, delimiter=";"):
            expenses.append({
                "date": row["date"],
                "category": row["category"],
                "amount": Money(row["amount"]),
                "note": row["note"]
            })
    return expenses


if __name__ == "__main__":
    expenses = load_expenses()
    items = [expense["amount"] for expense in expenses]
    sorted_items = sorted(items)
    total = sum(items, Money(0))

    print("Витрати за зростанням суми:")
    for item in sorted_items:
        print(item)
    print("Кількість витрат:", len(items))
    print("Загальна сума:", total)

    try:
        print(Money(10) + 5)
    except TypeError as error:
        print("Несумісні типи:", error)
