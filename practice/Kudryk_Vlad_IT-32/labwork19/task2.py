class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("owner name must not be empty")
        if balance < 0:
            raise ValueError("initial balance must not be negative")
        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance = round(self.__balance - amount, 2)

    def show(self):
        return self.__balance


w = Wallet("Vlad Kudryk", 1000)
w.deposit(250)
w.withdraw(100.5)
print("Баланс через метод:", w.show())

try:
    w.withdraw(10_000)
except ValueError as e:
    print("Помилка зняття:", e)

try:
    print(w.__balance)
except AttributeError as e:
    print("AttributeError:", e)

print("Через _Wallet__balance:", w._Wallet__balance)
print("Атрибути обʼєкта:", [a for a in vars(w)])
