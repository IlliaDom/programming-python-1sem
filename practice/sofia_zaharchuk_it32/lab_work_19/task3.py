class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner        # викликає сетер owner
        self.balance = balance    # викликає сетер balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not value.strip():
            raise ValueError("owner can not be empty")
        self.__owner = value.strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(value, 2)

    @property
    def is_empty(self):
        return self.balance == 0


if __name__ == "__main__":
    wallet = Wallet("Ваше Імʼя", 1500)
    print(wallet.balance)
    wallet.balance = 1200.555
    print(wallet.balance)

    try:
        wallet.balance = -10
    except ValueError as error:
        print("error:", error)

    try:
        wallet.owner = "   "
    except ValueError as error:
        print("error:", error)

    print(wallet.is_empty)
    try:
        wallet.is_empty = True
    except AttributeError as error:
        print("error:", error)
