class Wallet:
    def __init__(self, owner, balance):
        if not str(owner).strip():
            raise ValueError("Власник гаманця не може бути порожнім")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.owner = owner.strip()
        self.balance = round(float(balance), 2)


wallet = Wallet("Марія Вовк", 2000)
print(f"Гаманець власника {wallet.owner}: {wallet.balance:.2f} грн")

try:
    Wallet("", 500)
except ValueError as error:
    print(f"Помилка створення гаманця: {error}")

try:
    Wallet("Марія Вовк", -100)
except ValueError as error:
    print(f"Помилка створення гаманця: {error}")
