import csv
from pathlib import Path


class Wallet:
    def __init__(self, owner, balance):
        if not str(owner).strip():
            raise ValueError("Власник гаманця не може бути порожнім")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.owner = owner.strip()
        self.__balance = round(float(balance), 2)

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума витрати має бути більшою за нуль")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів")
        self.__balance = round(self.__balance - amount, 2)


monthly_budget = 2000.00
wallet = Wallet("Марія Вовк", monthly_budget)
expenses_file = Path(__file__).parent / "data" / "expenses.csv"
total_spent = 0.0

print(f"Власник: {wallet.owner}")
print(f"Місячний бюджет: {monthly_budget:.2f} грн")

with expenses_file.open("r", encoding="utf-8", newline="") as file:
    for expense in csv.DictReader(file):
        amount = float(expense["amount"])
        try:
            wallet.withdraw(amount)
            total_spent += amount
            print(
                f'{expense["date"]} | {expense["category"]} | '
                f'{amount:.2f} грн | залишок: {wallet.balance:.2f} грн'
            )
        except ValueError as error:
            print(
                f'Недостатньо коштів на витраті '
                f'{expense["date"]} {expense["category"]} ({amount:.2f} грн): {error}'
            )
            break

print(f"Усього витрачено: {total_spent:.2f} грн")
print(f"Залишок: {wallet.balance:.2f} грн")
