import csv
from task3 import Wallet


MONTHLY_BUDGET = 5000

wallet = Wallet("Ілля Воробей", MONTHLY_BUDGET)

print("Власник:", wallet.owner)
print("Початковий бюджет:", wallet.balance, "грн")

try:
    with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            if not row or len(row) < 3:
                continue

            try:
                amount = float(row[2].replace(",", "."))
            except ValueError:
                continue

            if amount <= 0:
                continue

            category = row[1]
            comment = row[3] if len(row) > 3 else ""

            try:
                wallet.balance = round(wallet.balance - amount, 2)
                print(
                    f"Витрата: {category} — {amount:.2f} грн. "
                    f"{comment}. Залишок: {wallet.balance:.2f} грн"
                )

            except ValueError:
                print("Недостатньо коштів для витрати:", category, amount)
                break

    print("\nЗалишок коштів:", wallet.balance, "грн")

except FileNotFoundError:
    print("Помилка: файл data/expenses.csv не знайдено")