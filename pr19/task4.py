import sys
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
MONTHLY_BUDGET = 6000.0

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"


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


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    wallet = Wallet(f"{NAME} {SURNAME}", MONTHLY_BUDGET)
    print(f"budget: {wallet.balance:.2f}")

    spent = 0.0
    with DATA_FILE.open(encoding="utf-8-sig") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            try:
                amount = float(parts[2])
            except (IndexError, ValueError):
                print(f"warning: line {number} skipped: {line}",
                      file=sys.stderr)
                continue
            try:
                wallet.withdraw(amount)
            except ValueError:
                print(f"stopped: not enough money for line {number}: {line}")
                break
            spent += amount

    print(f"spent: {spent:.2f}")
    print(f"left:  {wallet.balance:.2f}")


if __name__ == "__main__":
    main()
