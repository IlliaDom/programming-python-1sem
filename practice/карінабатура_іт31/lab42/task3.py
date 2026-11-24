class Wallet:
    def __init__(self, owner: str, balance: float | int = 0.0):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Ім'я власника не може бути порожнім.")
        self.__owner = value.strip()

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float | int) -> None:
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(float(value), 2)

    @property
    def is_empty(self) -> bool:
        return self.__balance == 0.0


if __name__ == "__main__":
    wallet = Wallet("Каріна Батура", 1500)
    print("Баланс:", wallet.balance, "| Порожній:", wallet.is_empty)

    wallet.balance = 1200.555
    print("Після оновлення балансу:", wallet.balance)

    # Від'ємний баланс -> ValueError
    try:
        wallet.balance = -25
    except ValueError as err:
        print("Помилка при присвоєнні від'ємного балансу:", err)

    # Запис у read-only властивість is_empty -> AttributeError
    try:
        wallet.is_empty = True
    except AttributeError as err:
        print("Помилка при спробі змінити is_empty:", err)