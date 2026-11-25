"""
Завдання 3. Властивість @property.
Перевіряємо сетери balance і owner та властивість лише для читання
is_empty.
"""
from wallet import Wallet


def main() -> None:
    wallet = Wallet("Назар", 1500)
    print(wallet.balance)
    wallet.balance = 1200.555
    print(wallet.balance)

    # Сетер owner не дозволяє порожнє імʼя
    try:
        wallet.owner = ""
    except ValueError as exc:
        print(f"error: {exc}")

    # Сетер balance не дозволяє від'ємне значення
    try:
        wallet.balance = -50
    except ValueError as exc:
        print(f"error: {exc}")

    print("is_empty:", wallet.is_empty)

    # is_empty - лише для читання, сетера немає
    try:
        wallet.is_empty = True
    except AttributeError as exc:
        print(f"error: {exc}")


if __name__ == "__main__":
    main()
