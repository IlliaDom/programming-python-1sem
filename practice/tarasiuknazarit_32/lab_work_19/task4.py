"""
Завдання 4. Гаманець і ваші витрати.
Створюємо гаманець з місячним бюджетом і по черзі списуємо з нього
всі витрати з data/expenses.csv. Якщо грошей не вистачає -
повідомляємо, на якій витраті, і зупиняємося.
"""
import csv
import sys

from wallet import Wallet

EXPENSES_FILE = "data/expenses.csv"
MONTHLY_BUDGET = 1200.0  # TODO: заміни на свій реальний місячний бюджет


def main() -> int:
    try:
        wallet = Wallet("Назар", MONTHLY_BUDGET)
    except ValueError as exc:
        print(f"Не вдалося створити гаманець: {exc}", file=sys.stderr)
        return 1

    print(f"стартовий баланс: {wallet.balance:.2f} UAH")

    try:
        with open(EXPENSES_FILE, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                amount = float(row["amount"])
                try:
                    wallet.withdraw(amount)
                except ValueError:
                    print(
                        f"Не вистачило коштів на витрату: "
                        f"{row['date']} {row['category']} {amount:.2f} "
                        f"({row.get('comment', '')}). "
                        f"Залишок на цей момент: {wallet.balance:.2f} UAH"
                    )
                    return 1
                print(
                    f"  списано {amount:.2f} UAH "
                    f"({row['category']}, {row.get('comment', '')}) "
                    f"-> залишок {wallet.balance:.2f} UAH"
                )
    except FileNotFoundError:
        print(f"Файл {EXPENSES_FILE} не знайдено", file=sys.stderr)
        return 1

    print(f"кінцевий баланс: {wallet.balance:.2f} UAH")
    return 0


if __name__ == "__main__":
    sys.exit(main())
