
import csv
import math
from datetime import date, datetime, timedelta
from pathlib import Path

print("Ira Leshchuk, IT-31")
print("АНАЛІЗ ВИТРАТ")

file_path = Path("data/expenses.csv")

expenses = []

with file_path.open("r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        if len(row) == 4:
            day, category, amount, description = row
            expenses.append({
                "date": datetime.strptime(day, "%Y-%m-%d").date(),
                "category": category,
                "amount": float(amount),
                "description": description
            })

if not expenses:
    print("Файл не містить витрат.")
    raise SystemExit

total = math.fsum(item["amount"] for item in expenses)
average = total / len(expenses)

print(f"\nКількість записів: {len(expenses)}")
print(f"Загальна сума: {total:.2f} грн")
print(f"Середня витрата: {average:.2f} грн")

daily = {}

for item in expenses:
    day = item["date"]
    daily[day] = daily.get(day, 0) + item["amount"]

first_day = min(daily)
last_day = max(daily)

print("\nВитрати за днями:")

current = first_day
while current <= last_day:
    print(f"{current}: {daily.get(current, 0):.2f} грн")
    current += timedelta(days=1)

top_day = max(daily, key=daily.get)
print(f"\nНайбільше витрачено: {top_day} — {daily[top_day]:.2f} грн")

category_totals = {}

for item in expenses:
    category = item["category"]
    category_totals[category] = category_totals.get(category, 0) + item["amount"]

print("\nВитрати за категоріями:")
for category, amount in category_totals.items():
    print(f"{category}: {amount:.2f} грн")

print("\nПеревірка math:")
print(f"Корінь із загальної суми: {math.sqrt(total):.2f}")
print(f"Чи сума більша за нуль: {math.isclose(total, 0)}")

print("\nАналіз дат:")
print(f"Перший день: {first_day.strftime('%d.%m.%Y')}")
print(f"Останній день: {last_day.strftime('%d.%m.%Y')}")
print(f"Проміжок: {(last_day - first_day).days} днів")

print("\nАналіз завершено.")
