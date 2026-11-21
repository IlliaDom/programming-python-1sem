NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
START_BALANCE = 1500.0


class Wallet:
    def __init__(self, owner, balance):
        if not owner or not owner.strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("start balance can not be negative")
        self.owner = owner
        self.balance = round(balance, 2)


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    wallet = Wallet(f"{NAME} {SURNAME}", START_BALANCE)
    print(f"created: {wallet.owner}, {wallet.balance:.2f}")

    for owner, balance in [("", 100), (f"{NAME} {SURNAME}", -50)]:
        try:
            Wallet(owner, balance)
        except ValueError as e:
            print(f"error: {e}")


if __name__ == "__main__":
    main()
