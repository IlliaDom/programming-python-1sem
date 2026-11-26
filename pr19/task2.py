class Wallet:
    """Гаманець з приватним балансом __balance."""

    def __init__(self, owner, balance):
        if not owner or not owner.strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
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

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    wallet = Wallet("Nazar Mischuk", 3000)
    wallet.deposit(500)
    wallet.withdraw(200)
    print("balance:", wallet.get_balance())

    try:
        wallet.withdraw(10_000)
    except ValueError as e:
        print("Error:", e)

    # Спроба прочитати за іменем
    try:
        print(wallet.__balance)
    except AttributeError as e:
        print("AttributeError:", e)

    # Name mangling: Python перейменовує __balance у _Wallet__balance
    print("via _Wallet__balance:", wallet._Wallet__balance)
    print("__dict__:", wallet.__dict__)
