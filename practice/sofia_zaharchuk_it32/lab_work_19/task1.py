class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("owner can not be empty")
        if balance < 0:
            raise ValueError(f"balance can not be negative: {balance}")
        self.owner = owner.strip()
        self.balance = round(balance, 2)


if __name__ == "__main__":
    for owner, balance in [("Ваше Імʼя", 1500.456), ("", 100), ("Ваше Імʼя", -50)]:
        try:
            wallet = Wallet(owner, balance)
            print("created:", wallet.owner, wallet.balance)
        except ValueError as error:
            print("error:", error)
