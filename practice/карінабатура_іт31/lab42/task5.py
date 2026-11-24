class Wallet:
    def __init__(self, owner: str, balance: float | int = 0.0):
        self.owner = owner
        self.balance = round(float(balance), 2)

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


if __name__ == "__main__":
    print("1. Видалення об'єкта з одним посиланням:")
    w1 = Wallet("Каріна")
    del w1
    print("Після del w1")

    print("\n2. Видалення одного посилання при наявності другого:")
    w2 = Wallet("Олена")
    other = w2
    del w2
    print("Після del w2 (об'єкт ще живий через other)")
    del other
    print("Після del other")

    print("\n3. Об'єкт залишається до завершення програми:")
    w3 = Wallet("Тарас")
    print("Кінець основного коду програми")