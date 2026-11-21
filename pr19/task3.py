NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
START_BALANCE = 1500.0


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

    @property
    def is_empty(self):
        return self.__balance == 0


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    wallet = Wallet(f"{NAME} {SURNAME}", START_BALANCE)
    print(wallet.balance)
    wallet.balance = 1200.555
    print(wallet.balance)
    print("is_empty:", wallet.is_empty)

    for action, func in [
        ("balance = -1", lambda: setattr(wallet, "balance", -1)),
        ("owner = ''", lambda: setattr(wallet, "owner", "")),
        ("is_empty = True", lambda: setattr(wallet, "is_empty", True)),
    ]:
        try:
            func()
        except (ValueError, AttributeError) as e:
            print(f"{action}: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
