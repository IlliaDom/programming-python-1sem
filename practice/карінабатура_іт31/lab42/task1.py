class Wallet:
    def __init__(self, owner: str, balance: float | int = 0.0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім.")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним.")

        self.owner = owner.strip()
        self.balance = round(float(balance), 2)


if __name__ == "__main__":
    # Коректний гаманець
    wallet = Wallet("Каріна Батура", 2500.456)
    print(f"Створено гаманець: {wallet.owner}, баланс: {wallet.balance}")

    # Некоректне ім'я власника
    try:
        invalid_owner = Wallet("   ", 1000)
    except ValueError as err:
        print("Помилка (ім'я власника):", err)

    # Некоректний початковий баланс
    try:
        invalid_balance = Wallet("Каріна Батура", -100)
    except ValueError as err:
        print("Помилка (баланс):", err)