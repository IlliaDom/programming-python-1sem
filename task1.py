class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")

        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")

        self.owner = owner.strip()
        self.balance = round(balance, 2)


wallet = Wallet("Ілля Воробей", 5000)
print("Гаманець створено:", wallet.owner, wallet.balance, "грн")

try:
    wallet2 = Wallet("", 1000)
except ValueError as error:
    print("Помилка:", error)

try:
    wallet3 = Wallet("Ілля Воробей", -500)
except ValueError as error:
    print("Помилка:", error)