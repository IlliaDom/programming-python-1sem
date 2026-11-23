class Wallet():
    def __init__(self, name, balance):
        if not name.strip():
            raise ValueError("name must be filled")
        if balance < 0:
            raise ValueError("balance cannot be negative")

        self.name = name
        self.__balance = round(balance, 2)
        print("wallet was created")

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("wallet does not have enough money")
        self.__balance -= amount


if __name__ == "__main__":
    try:
        oleksandr = Wallet("Oleksandr", 478)
        # oleksandr.withdraw(4444)
        oleksandr.deposit(45)
        print(oleksandr._Wallet__balance)
    except ValueError as err:
        print("error:", err)