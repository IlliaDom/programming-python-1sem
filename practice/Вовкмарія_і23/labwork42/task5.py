class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __del__(self):
        owner = getattr(self, "owner", "невідомий власник")
        print(f"wallet of {owner} deleted")


print("Випадок 1")
wallet = Wallet("Марія Вовк", 2000)
del wallet
print("Посилання wallet видалено")

print("\nВипадок 2")
wallet = Wallet("Марія Вовк", 2000)
other = wallet
del wallet
print("Видалено лише wallet, але посилання other залишилося")
del other
print("Видалено останнє посилання")

print("\nВипадок 3")
wallet = Wallet("Марія Вовк", 2000)
print("Деструктор буде викликано після завершення програми")
