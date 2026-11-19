class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise ValueError("Баланс має бути числом")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.owner = owner.strip()
        self.balance = round(float(balance), 2)


def main() -> None:
    wallet = Wallet("Діана Мельник", 2000.567)
    print(f"Гаманець власниці: {wallet.owner}; баланс: {wallet.balance:.2f} грн")

    try:
        Wallet("   ", 100)
    except ValueError as error:
        print(f"Помилка створення гаманця: {error}")

    try:
        Wallet("Діана Мельник", -50)
    except ValueError as error:
        print(f"Помилка створення гаманця: {error}")


if __name__ == "__main__":
    main()
