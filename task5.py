class Wallet:
    def __init__(self, owner):
        self.owner = owner
        print(f"Гаманець {self.owner} створено")

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("Створення першого гаманця")
wallet = Wallet("Ілля Воробей")

print("Видалення гаманця")
del wallet

print("\nПеревірка другого посилання")
wallet = Wallet("Ілля Воробей")
other = wallet

del wallet
print("Перше посилання видалено, але об'єкт ще існує")

del other
print("Друге посилання видалено")

print("\nКінець програми")