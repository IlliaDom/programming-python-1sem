class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not value.strip():
            raise ValueError("Ім'я власника не може бути порожнім")

        self.__owner = value.strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.__balance = round(value, 2)

    @property
    def is_empty(self):
        return self.balance == 0


wallet = Wallet("Ілля Воробей", 1500)

print("Власник:", wallet.owner)
print("Баланс:", wallet.balance)
print("Гаманець порожній:", wallet.is_empty)

wallet.balance = 1200.555
print("Новий баланс:", wallet.balance)

try:
    wallet.balance = -100
except ValueError as error:
    print("Помилка:", error)

try:
    wallet.is_empty = False
except AttributeError as error:
    print("Помилка:", error)