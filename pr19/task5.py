class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("--- 1. del wallet (одне посилання) ---")
wallet = Wallet("Nazar Mischuk", 3000)
del wallet
print("after del")

print("\n--- 2. два посилання, видаляємо одне ---")
wallet = Wallet("Nazar Mischuk (2)", 3000)
other = wallet
del wallet
print("after del wallet: object is still alive via 'other'")
print("other.owner =", other.owner)
del other
print("after del other")

print("\n--- 3. наприкінці програми ---")
last = Wallet("Nazar Mischuk (3)", 3000)
print("end of program")
