class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатною")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів")
        self.__balance -= amount


wallet = Wallet("Лещук Ірина", 6000)

wallet.deposit(500)
print("Після поповнення:", wallet._Wallet__balance)

wallet.withdraw(1000)
print("Після зняття:", wallet._Wallet__balance)

try:
    print(wallet.__balance)
except AttributeError as error:
    print("Помилка доступу:", error)

print("Доступ через name mangling:", wallet._Wallet__balance)