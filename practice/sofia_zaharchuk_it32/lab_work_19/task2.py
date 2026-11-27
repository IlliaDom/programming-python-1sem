class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("owner can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.owner = owner.strip()
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.__balance:
            raise ValueError(f"not enough money: {self.__balance:.2f} < {amount:.2f}")
        self.__balance = round(self.__balance - amount, 2)


if __name__ == "__main__":
    wallet = Wallet("Ваше Імʼя", 1500)
    wallet.deposit(200)
    try:
        wallet.withdraw(5000)
    except ValueError as error:
        print("error:", error)

    try:
        print(wallet.__balance)
    except AttributeError as error:
        print("error:", error)

    print(vars(wallet))
    print(wallet._Wallet__balance)
