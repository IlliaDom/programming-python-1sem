import csv
from pathlib import Path

class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("owner name must not be empty")
        self.__owner = value.strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(value, 2)

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.balance = self.__balance - amount

def process(budget):
    wallet = Wallet("Vlad Kudryk", budget)
    print(f"\nБюджет: {wallet.balance:.2f}")
    total = 0.0
    path = Path(__file__).parent / "data" / "expenses.csv"
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            amount = float(row["amount"])
            try:
                wallet.withdraw(amount)
            except ValueError:
                print(f"Не вистачає коштів на витрату «{row['category']}» "
                      f"({row['date']}, {amount:.2f}); залишок {wallet.balance:.2f}. Зупинка.")
                return
            total += amount
            print(f"  списано {amount:>9.2f}  ({row['category']}), залишок {wallet.balance:.2f}")
    print(f"Сума витрат: {total:.2f}; залишок: {wallet.balance:.2f}")

process(20000)
process(10000)