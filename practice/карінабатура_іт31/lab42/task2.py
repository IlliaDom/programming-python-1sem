class Wallet:
    def __init__(self, owner: str, balance: float | int = 0.0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім.")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним.")

        self.owner = owner.strip()
        self.__balance = round(float(balance), 2)

    def deposit(self, amount: float | int) -> None:
        if amount <= 0:
            raise ValueError("Сума поповнення має бути додатною.")
        self.__balance = round(self.__balance + float(amount), 2)

    def withdraw(self, amount: float | int) -> None:
        if amount <= 0:
            raise ValueError("Сума зняття має бути додатною.")
        if float(amount) > self.__balance:
            raise ValueError("Недостатньо коштів на балансі.")
        self.__balance = round(self.__balance - float(amount), 2)

    def get_balance(self) -> float:
        return self.__balance


if __name__ == "__main__":
    wallet = Wallet("Каріна Батура", 1500)
    wallet.deposit(350.256)
    wallet.withdraw(200)
    print("Баланс через метод get_balance():", wallet.get_balance())

    # 1. Спроба прочитати __balance напряму
    try:
        print(wallet.__balance)
    except AttributeError as err:
        print("Помилка при зверненні до wallet.__balance:", err)

    # 2. Доступ через перетворення імені (name mangling)
    print("Значення через wallet._Wallet__balance:", wallet._Wallet__balance)