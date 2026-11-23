class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("1) del wallet (єдине посилання)")
wallet = Wallet("Vlad Kudryk", 1000)
del wallet
print("   після del\n")

print("2) два посилання, видаляємо одне")
wallet = Wallet("Karina Pikul", 500)
other = wallet
del wallet
print("   після del wallet — обʼєкт ще живий:", other.owner)
del other
print("   після del other\n")

print("3) наприкінці програми")
last = Wallet("Nazariiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiy", 300)
print("   кінець програми")
