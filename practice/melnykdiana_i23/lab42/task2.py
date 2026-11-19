class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.owner = owner.strip()
        self.__balance = round(float(balance), 2)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за нуль")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за нуль")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance = round(self.__balance - amount, 2)


def main() -> None:
    wallet = Wallet("Діана Мельник", 1500)
    wallet.deposit(100)
    wallet.withdraw(250)
    print(f"Баланс після операцій: {wallet._Wallet__balance:.2f} грн")

    try:
        print(wallet.__balance)
    except AttributeError as error:
        print(f"Прямий доступ wallet.__balance: {type(error).__name__}: {error}")

    print("Доступ через перетворене ім'я:", wallet._Wallet__balance)


if __name__ == "__main__":
    main()
