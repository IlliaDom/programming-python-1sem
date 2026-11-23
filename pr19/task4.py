import csv
import os

# Шлях до файлу рахується від папки, де лежить сам скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "expenses.csv")


class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not value or not value.strip():
            raise ValueError("owner name can not be empty")
        self.__owner = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(value, 2)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("not enough money")
        self.balance = self.balance - amount


def spend_all(budget, path=CSV_PATH):
    wallet = Wallet("Nazar Mischuk", budget)
    print(f"Budget: {wallet.balance:.2f}")
    total = 0.0
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            amount = float(row["amount"])
            try:
                wallet.withdraw(amount)
            except ValueError:
                print(f"STOP: not enough money for {row['date']} "
                      f"{row['category']} {amount:.2f} ({row['comment']})")
                break
            total += amount
    print(f"Spent: {total:.2f}, left: {wallet.balance:.2f}")
    return wallet.balance


if __name__ == "__main__":
    print("--- Case 1: budget is enough ---")
    left = spend_all(3000)
    print("check (budget - sum):", round(3000 - 1696.00, 2), "==", left)

    print("\n--- Case 2: budget is too small ---")
    spend_all(1000)