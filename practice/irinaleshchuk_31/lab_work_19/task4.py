import csv


class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я не може бути порожнім")
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.owner = owner
        self.__balance = round(balance, 2)

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів")
        self.__balance = round(self.__balance - amount, 2)


wallet = Wallet("Лещук Ірина", 6000)

print("Власник:", wallet.owner)
print("Початковий бюджет:", wallet.balance, "грн")

with open("data/expenses.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        date, category, amount, description = row
        amount = float(amount)

        try:
            wallet.withdraw(amount)
            print(f"{date} | {category} | -{amount:.2f} грн | Залишок: {wallet.balance:.2f} грн")
        except ValueError as error:
            print(f"Недостатньо коштів на витраті: {description}")
            print(error)
            break

print("Кінцевий залишок:", wallet.balance, "грн")