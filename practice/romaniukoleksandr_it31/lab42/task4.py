from pathlib import Path

EXPENSES_PATH = Path("data/expenses.csv")

class Wallet():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("wallet was created")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("wallet does not have enough money")
        self.balance -= amount

    @property
    def balance(self):
        return self.__balance

    @property
    def is_empty(self):
        return self.__balance == 0

    @property
    def owner(self):
        return self.__owner

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance cannot be negative")

        self.__balance = round(value, 2)

    @owner.setter
    def owner(self, value):
        if not value.strip():
            raise ValueError("name must be filled")

        self.__owner = value


if __name__ == "__main__":
    oleksandr = Wallet("Oleksandr", 6000)

    with open(EXPENSES_PATH, "r", encoding="utf-8") as f:
        for record in f.readlines():
            if record.startswith("#") or record.strip() == "":
                continue

            line = record.strip("\n").split(";")

            try:
                oleksandr.withdraw(float(line[2]))
            except ValueError as err:
                print(f"error: {err} in {line}")
                break

    print(oleksandr.balance)