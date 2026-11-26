class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")

        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")

        self.owner = owner
        self.balance = round(balance, 2)


wallet = Wallet("Лещук Ірина", 6000)
print(f"Власник: {wallet.owner}")
print(f"Баланс: {wallet.balance} грн")

try:
    wallet1 = Wallet("", 1000)
except ValueError as error:
    print(f"Помилка: {error}")

try:
    wallet2 = Wallet("Лещук Ірина", -500)
except ValueError as error:
    print(f"Помилка: {error}")