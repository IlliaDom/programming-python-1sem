class Wallet:
    def __init__(self, owner, balance):
        if not str(owner).strip():
            raise ValueError("Власник гаманця не може бути порожнім")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.owner = owner.strip()
        self.__balance = round(float(balance), 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за нуль")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за нуль")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance = round(self.__balance - amount, 2)


wallet = Wallet("Марія Вовк", 2000)
wallet.deposit(250)
wallet.withdraw(100)
print(f"Баланс після операцій: {wallet._Wallet__balance:.2f} грн")

try:
    print(wallet.__balance)
except AttributeError as error:
    print(f"Помилка доступу: {error}")

print(f"Доступ через перетворення імені: {wallet._Wallet__balance:.2f} грн")

try:
    wallet.withdraw(5000)
except ValueError as error:
    print(f"Помилка зняття: {error}")
