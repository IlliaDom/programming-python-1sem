class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.owner = owner.strip()
        self.__balance = round(float(balance), 2)

    @property
    def balance(self) -> float:
        return self.__balance

    def __del__(self) -> None:
        owner = getattr(self, "owner", "невідомий власник")
        print(f"wallet of {owner} deleted")


def main() -> None:
    print("1. Видалення єдиного посилання:")
    wallet = Wallet("Діана Мельник", 100)
    del wallet
    print("Після del wallet")

    print("\n2. На гаманець є два посилання:")
    wallet = Wallet("Діана Мельник", 200)
    other = wallet
    del wallet
    print("Після del wallet, об'єкт ще доступний через other:", other.owner)
    del other
    print("Після del other")

    print("\n3. Об'єкт залишено до завершення програми:")
    at_exit = Wallet("Діана Мельник", 300)
    print("Гаманець at_exit існує до завершення програми")


if __name__ == "__main__":
    main()
