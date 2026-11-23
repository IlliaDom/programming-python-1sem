class Wallet():
    def __init__(self, name, balance):
        if not name.strip():
            raise ValueError("name must be filled")
        if balance < 0:
            raise ValueError("balance cannot be negative")

        self.name = name
        self.balance = round(balance, 2)
        print("wallet was created")


if __name__ == "__main__":
    try:
        oleksandr = Wallet("Oleksandr", 478)
    except ValueError as err:
        print("error:", err)