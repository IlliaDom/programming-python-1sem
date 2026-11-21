NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
START_BALANCE = 1500.0


class Wallet:
    def __init__(self, owner, balance):
        if not owner or not owner.strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("start balance can not be negative")
        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw must be positive")
        if amount > self.__balance:
            raise ValueError("not enough money")
        self.__balance = round(self.__balance - amount, 2)

    def show(self):
        return self.__balance


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    wallet = Wallet(f"{NAME} {SURNAME}", START_BALANCE)
    wallet.deposit(200)
    wallet.withdraw(50.5)
    print("balance:", wallet.show())

    try:
        wallet.withdraw(10_000)
    except ValueError as e:
        print("withdraw error:", e)

    try:
        print(wallet.__balance)
    except AttributeError as e:
        print("AttributeError:", e)

    print("wallet._Wallet__balance:", wallet._Wallet__balance)
    print("wallet.__dict__:", wallet.__dict__)


if __name__ == "__main__":
    main()
