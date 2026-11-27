class Wallet:
    def __init__(self, owner):
        self.owner = owner

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("--- 1. del wallet ---")
wallet = Wallet("Ваше Імʼя")
del wallet
print("after del")

print("--- 2. друге посилання ---")
wallet = Wallet("Ваше Імʼя")
other = wallet
del wallet
print("after del wallet (object still alive)")
del other
print("after del other")

print("--- 3. кінець програми ---")
last = Wallet("Кінець програми")
print("program ends")
