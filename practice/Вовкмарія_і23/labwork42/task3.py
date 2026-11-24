class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not str(value).strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        self.__owner = str(value).strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(float(value), 2)

    @property
    def is_empty(self):
        return self.__balance == 0


wallet = Wallet("Марія Вовк", 1500)
print(f"Власник: {wallet.owner}")
print(f"Баланс: {wallet.balance:.2f} грн")
wallet.balance = 1200.555
print(f"Округлений баланс: {wallet.balance:.2f} грн")
print(f"Гаманець порожній: {wallet.is_empty}")

try:
    wallet.balance = -50
except ValueError as error:
    print(f"Помилка зміни балансу: {error}")

try:
    wallet.is_empty = True
except AttributeError as error:
    print(f"Помилка зміни is_empty: {error}")
