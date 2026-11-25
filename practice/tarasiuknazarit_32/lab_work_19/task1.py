"""
Завдання 1. Конструктор з перевіркою.
Клас Wallet, що не дозволяє створити обʼєкт з порожнім імʼям
власника або з від'ємним початковим балансом.
"""


class Wallet:
    def __init__(self, owner: str, balance: float):
        if not owner:
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("initial balance can not be negative")

        self.owner = owner
        self.balance = round(balance, 2)


def main() -> None:
    # Коректний гаманець
    wallet = Wallet("Назар", 1500)
    print(f"ok: wallet of {wallet.owner}, balance {wallet.balance}")

    # Спроба 1: порожнє імʼя
    try:
        Wallet("", 500)
    except ValueError as exc:
        print(f"error: {exc}")

    # Спроба 2: від'ємний баланс
    try:
        Wallet("Іван", -100)
    except ValueError as exc:
        print(f"error: {exc}")


if __name__ == "__main__":
    main()
