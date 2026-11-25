"""
Завдання 2. Інкапсуляція.
Баланс зберігається в приватному атрибуті __balance. Методи
deposit() і withdraw() - єдиний офіційний спосіб його змінювати.
"""


class Wallet:
    def __init__(self, owner: str, balance: float):
        if not owner:
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("initial balance can not be negative")

        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance = round(self.__balance - amount, 2)


def main() -> None:
    wallet = Wallet("Назар", 1000)
    wallet.deposit(200)
    wallet.withdraw(500)
    print("баланс через deposit/withdraw:", wallet._Wallet__balance)

    # Спроба прочитати "приватний" атрибут за його іменем
    try:
        print(wallet.__balance)
    except AttributeError as exc:
        print(f"error: {exc}")

    # Насправді атрибут нікуди не зник - Python просто перейменував
    # його на _Wallet__balance (name mangling), щоб уникнути
    # випадкового конфлікту імен із атрибутами підкласів.
    print("через name mangling (_Wallet__balance):", wallet._Wallet__balance)


if __name__ == "__main__":
    main()
