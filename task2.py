
from task1 import Money


def load_expenses(filename):
    items = []

    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            if not line.strip():
                continue

            parts = line.strip().split(";")

            # Пропускаємо заголовок таблиці
            if parts[0].lower() in ("date", "дата"):
                continue

            if len(parts) < 3:
                print("Рядок пропущено:", line.strip())
                continue

            try:
                date = parts[0]
                category = parts[1]
                amount = float(parts[2].replace(",", "."))

                items.append((date, category, Money(amount)))

            except ValueError:
                print("Некоректний рядок:", line.strip())

    return items


expenses = load_expenses("data/expenses.csv")

money_items = [item[2] for item in expenses]
sorted_items = sorted(money_items)

print("Витрати від найменшої до найбільшої:")
for item in sorted_items:
    print(item)

total = sum(money_items, Money(0))

print("\nЗагальна сума витрат:", total)

try:
    print(Money(10) + 5)
except TypeError as error:
    print("\nОчікувана помилка:", error)
