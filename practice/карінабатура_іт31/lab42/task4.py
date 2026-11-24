import csv
from pathlib import Path
from task3 import Wallet


def resolve_expenses_path() -> Path:
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / "data" / "expenses.csv",
        Path("lab42/data/expenses.csv"),
        Path("data/expenses.csv"),
    ]
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError("Не знайдено файл data/expenses.csv")


if __name__ == "__main__":
    monthly_budget = 2000.00 
    wallet = Wallet("Каріна Батура", monthly_budget)

    csv_path = resolve_expenses_path()
    with csv_path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader, start=1):
            category = row["category"].strip()
            amount = float(row["amount_uah"].strip())

            if amount > wallet.balance:
                print(
                    f"Недостатньо коштів на витраті #{idx} ('{category}', {amount:.2f} грн). "
                    f"Поточний залишок: {wallet.balance:.2f} грн."
                )
                break

            wallet.balance = wallet.balance - amount
            print(f"Списано '{category}' (-{amount:.2f} грн) -> залишок: {wallet.balance:.2f} грн")

    print(f"Підсумковий баланс: {wallet.balance:.2f} грн")