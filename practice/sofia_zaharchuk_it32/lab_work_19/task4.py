import csv

from task3 import Wallet

BUDGET = 15000          # <- ваш реальний місячний бюджет
OWNER = "Ваше Імʼя"     # <- ваше імʼя

wallet = Wallet(OWNER, BUDGET)
total = 0.0

with open("data/expenses.csv", encoding="utf-8", newline="") as file:
    for number, row in enumerate(csv.DictReader(file), start=1):
        amount = float(row["amount"])
        if amount > wallet.balance:
            print(f"stop: not enough money on expense #{number}: "
                  f"{row} (balance {wallet.balance:.2f})")
            break
        wallet.balance = wallet.balance - amount
        total += amount
    else:
        print(f"all expenses processed, spent {total:.2f}")

print(f"balance left: {wallet.balance:.2f}")
