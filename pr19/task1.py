class Wallet:
    """Гаманець з перевіркою даних у конструкторі."""

    def __init__(self, owner, balance):
        if not owner or not owner.strip():
            raise ValueError("owner name can not be empty")
        if balance < 0:
            raise ValueError("balance can not be negative")
        self.owner = owner
        self.balance = round(balance, 2)


if __name__ == "__main__":
  
    wallet = Wallet("Nazar Mischuk", 3000.456)
    print(f"OK: {wallet.owner}, balance = {wallet.balance}")

   
    try:
        bad1 = Wallet("", 100)
    except ValueError as e:
        print("Error:", e)

    
    try:
        bad2 = Wallet("Nazar Mischuk", -50)
    except ValueError as e:
        print("Error:", e)
