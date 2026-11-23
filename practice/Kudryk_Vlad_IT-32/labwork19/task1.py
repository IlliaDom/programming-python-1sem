class Wallet:
    def __init__(self, owner, balance):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("owner name must not be empty")
        if balance < 0:
            raise ValueError("initial balance must not be negative")
        self.owner = owner
        self.balance = round(balance, 2)

w = Wallet("Vlad Kudryk", 1500.456)
print(f"OK: {w.owner}, баланс {w.balance}")

# некоректні спроби
for args in [("", 100), ("Vlad Kudryk", -50)]:
    try:
        Wallet(*args)
    except ValueError as e:
        print(f"Помилка при Wallet{args}: {e}")
