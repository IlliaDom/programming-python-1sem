import csv
from pathlib import Path


class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        self.owner = owner.strip()
        self.balance = round(float(balance), 2)
        if self.balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сума витрати має бути більшою за нуль")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів")
        self.balance = round(self.balance - amount, 2)


def main() -> None:
    # Замініть демонстраційний бюджет на свій фактичний місячний бюджет.
    monthly_budget = 2000.00
    wallet = Wallet("Діана Мельник", monthly_budget)
    expenses_path = Path(__file__).with_name("expenses.csv")

    print(f"Власниця: {wallet.owner}")
    print(f"Початковий бюджет: {monthly_budget:.2f} грн")
    with expenses_path.open("r", encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            amount = float(row["amount"])
            description = f"{row['date']} {row['category']} {amount:.2f} ({row.get('note', '')})"
            try:
                wallet.withdraw(amount)
                print(f"Списано {description}; залишок {wallet.balance:.2f} грн")
            except ValueError:
                print(f"Недостатньо коштів на витрату: {description}")
                print(f"Обробку зупинено; залишок: {wallet.balance:.2f} грн")
                break
    else:
        print(f"Усі витрати оброблено; залишок: {wallet.balance:.2f} грн")


if __name__ == "__main__":
    main()
