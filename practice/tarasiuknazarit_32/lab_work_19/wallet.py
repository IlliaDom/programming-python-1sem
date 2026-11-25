"""
Фінальна версія класу Wallet (Завдання 3): власник і баланс -
властивості @property з перевіркою, is_empty - властивість лише
для читання. Деструктор __del__ додано в Завданні 5.
"""


class Wallet:
    def __init__(self, owner: str, balance: float):
        self.owner = owner  # викликає сетер owner
        self.balance = balance  # викликає сетер balance

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, value: str) -> None:
        if not value:
            raise ValueError("owner name can not be empty")
        self.__owner = value

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(value, 2)

    @property
    def is_empty(self) -> bool:
        return self.__balance == 0

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance = self.__balance + amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.balance = self.__balance - amount

    def __del__(self) -> None:
        owner = getattr(self, "_Wallet__owner", "<unknown>")
        print(f"wallet of {owner} deleted")
