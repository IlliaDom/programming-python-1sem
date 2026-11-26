class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("1. Видалення об'єкта:")
wallet = Wallet("Лещук Ірина", 6000)
del wallet

print("\n2. Видалення одного посилання:")
wallet = Wallet("Лещук Ірина", 6000)
other = wallet
del wallet
print("Об'єкт ще існує через друге посилання")

del other

print("\n3. Наприкінці програми:")
wallet = Wallet("Лещук Ірина", 6000)
print("Програма завершується")