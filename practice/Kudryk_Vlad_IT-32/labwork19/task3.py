class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner    
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("owner name must not be empty")
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
        return self.__balance == 0


wallet = Wallet("Vlad Kudryk", 1500)
print(wallet.balance)
wallet.balance = 1200.555
print(wallet.balance)

try:
    wallet.balance = -10
except ValueError as e:
    print("ValueError:", e)

try:
    wallet.owner = "   "
except ValueError as e:
    print("ValueError:", e)

print("is_empty:", wallet.is_empty)
wallet.balance = 0
print("is_empty після обнулення:", wallet.is_empty)

try:
    wallet.is_empty = False
except AttributeError as e:
    print("AttributeError:", e)
