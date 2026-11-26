class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я не може бути порожнім")

        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.owner = owner.strip()
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути додатною")

        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття повинна бути додатною")

        if amount > self.__balance:
            raise ValueError("Недостатньо коштів")

        self.__balance = round(self.__balance - amount, 2)


wallet = Wallet("Ілля Воробей", 1000)

wallet.deposit(500)
wallet.withdraw(200)

print("Власник:", wallet.owner)

try:
    print(wallet.__balance)
except AttributeError as error:
    print("Помилка:", error)

print("Баланс через name mangling:", wallet._Wallet__balance)