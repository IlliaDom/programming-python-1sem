NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"
START_BALANCE = 1500.0


class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = round(balance, 2)

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    owner = f"{NAME} {SURNAME}"

    print("--- case 1: del wallet")
    wallet = Wallet(owner, START_BALANCE)
    del wallet
    print("after del")

    print("--- case 2: two references, delete one")
    wallet = Wallet(owner, START_BALANCE)
    other = wallet
    del wallet
    print("after del wallet (other still refers to the object)")
    del other
    print("after del other")

    print("--- case 3: end of program")
    last = Wallet(owner, START_BALANCE)
    print("end of program")


main()
