class Wallet():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("wallet was created")

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
    oleksandr = Wallet("Oleksandr", 478)

    try:
        print(f"Balance: {oleksandr.balance}")
        oleksandr.balance = -999
        oleksandr.is_empty = True        
        oleksandr.owner = "   "
    except ValueError as err:
        print("error:", err)
    except AttributeError as err:
        print("error:", err)
        
