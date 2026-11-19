class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        self.__owner = value.strip()

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("Баланс має бути числом")
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(float(value), 2)

    @property
    def is_empty(self) -> bool:
        return self.balance == 0


def main() -> None:
    wallet = Wallet("Діана Мельник", 1500)
    print(f"Баланс: {wallet.balance:.2f} грн")
    wallet.balance = 1200.555
    print(f"Після зміни: {wallet.balance:.2f} грн")
    print("Гаманець порожній:", wallet.is_empty)

    try:
        wallet.balance = -10
    except ValueError as error:
        print(f"Некоректний баланс: {type(error).__name__}: {error}")

    try:
        wallet.is_empty = True
    except AttributeError as error:
        print(f"Зміна is_empty: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
