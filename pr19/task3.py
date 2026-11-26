class Wallet:
    """Гаманець з властивостями balance, owner та is_empty."""

    def __init__(self, owner, balance):
        self.owner = owner        # викликає сетер owner
        self.balance = balance    # викликає сетер balance

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

    @property
    def is_empty(self):  # лише для читання (немає сетера)
        return self.__balance == 0


if __name__ == "__main__":
    wallet = Wallet("Nazar Mischuk", 1500)
    print(wallet.balance)
    wallet.balance = 1200.555
    print(wallet.balance)

    try:
        wallet.balance = -10
    except ValueError as e:
        print("ValueError:", e)

    try:
        wallet.owner = "  "
    except ValueError as e:
        print("ValueError:", e)

    print("is_empty:", wallet.is_empty)
    wallet.balance = 0
    print("is_empty after balance = 0:", wallet.is_empty)

    try:
        wallet.is_empty = False
    except AttributeError as e:
        print("AttributeError:", e)
