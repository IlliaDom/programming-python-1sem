
import csv
import sys
import math
from pathlib import Path
from datetime import datetime, date, timedelta

name = "Diana"
surname = "Melnyk"
group = "I-23"

print(f"{name} {surname}, група {group}")

file_path = Path(__file__).parent / "data" / "expenses.csv"

if not file_path.exists():
    print(f"Помилка: файл не знайдено: {file_path}", file=sys.stderr)
    sys.exit(1)

expenses = []

with file_path.open("r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    next(reader, None)  # Пропускаємо заголовок

    for line_number, row in enumerate(reader, start=2):
        if not row or all(not value.strip() for value in row):
            continue

        if row[0].strip().startswith("#"):
            continue

        try:
            if len(row) < 3:
                raise ValueError("Недостатньо полів")

            expense_date = datetime.strptime(
                row[0].strip(), "%Y-%m-%d"
            ).date()

            amount = float(row[2].strip())

            if not math.isfinite(amount) or amount < 0:
                raise ValueError("Некоректна сума")

            expenses.append((expense_date, amount))

        except (ValueError, TypeError):
            print(
                f"Попередження: некоректний запис у рядку {line_number}",
                file=sys.stderr
            )

if not expenses:
    print("Немає коректних записів про витрати.", file=sys.stderr)
    sys.exit(1)

first_date = min(item[0] for item in expenses)
last_date = max(item[0] for item in expenses)

period_days = (last_date - first_date).days + 1

print("\n=== ПЕРІОД ВИТРАТ ===")
print(f"Перша дата: {first_date.strftime('%d.%m.%Y')}")
print(f"Остання дата: {last_date.strftime('%d.%m.%Y')}")
print(f"День тижня першої дати: {first_date.strftime('%A')}")
print(f"День тижня останньої дати: {last_date.strftime('%A')}")
print(f"Тривалість періоду: {period_days} днів")

daily_totals = {}

for current_date in (
    first_date + timedelta(days=i)
    for i in range(period_days)
):
    daily_totals[current_date] = math.fsum(
        amount
        for expense_date, amount in expenses
        if expense_date == current_date
    )


total = math.fsum(amount for _, amount in expenses)
average = total / period_days

variance = math.fsum(
    (amount - average) ** 2
    for amount in daily_totals.values()
) / period_days

standard_deviation = math.sqrt(variance)

print("\n=== ЗАГАЛЬНА СТАТИСТИКА ===")
print(f"Загальні витрати: {total:.2f} грн")
print(f"Середні витрати за день: {average:.2f} грн")
print(f"Стандартне відхилення: {standard_deviation:.2f} грн")

weekday_totals = {i: [] for i in range(7)}

for current_date, amount in daily_totals.items():
    weekday_totals[current_date.weekday()].append(amount)

print("\n=== ВИТРАТИ ЗА ДНЯМИ ТИЖНЯ ===")

for weekday in range(7):
    weekday_name = date(2026, 1, 5 + weekday).strftime("%A")
    weekday_sum = math.fsum(weekday_totals[weekday])
    print(f"{weekday_name}: {weekday_sum:.2f} грн")

top_day = max(daily_totals, key=daily_totals.get)
no_spend_days = sum(
    1 for amount in daily_totals.values() if amount == 0
)

print("\n=== ДОДАТКОВА СТАТИСТИКА ===")
print(
    f"Найбільше витрачено: {daily_totals[top_day]:.2f} грн "
    f"({top_day.strftime('%d.%m.%Y')})"
)
print(f"Днів без витрат: {no_spend_days}")

def month_information(current_date):
    first_day = current_date.replace(day=1)

    if current_date.month == 12:
        next_month = date(current_date.year + 1, 1, 1)
    else:
        next_month = date(
            current_date.year,
            current_date.month + 1,
            1
        )

    days_in_month = (next_month - first_day).days
    days_left = days_in_month - current_date.day

    return days_in_month, days_left


days_in_month, days_left = month_information(last_date)

forecast = average * days_in_month

print("\n=== ПРОГНОЗ НА МІСЯЦЬ ===")
print(f"Днів у місяці: {days_in_month}")
print(f"Днів до кінця місяця: {days_left}")
print(f"Прогноз витрат за місяць: {forecast:.2f} грн")

print("\n=== ПЕРЕВІРКА КОНТРОЛЬНИХ ДАТ ===")

for test_date in [
    date(2026, 12, 15),
    date(2028, 2, 10)
]:
    month_days, remaining = month_information(test_date)
    print(
        f"{test_date.strftime('%d.%m.%Y')}: "
        f"{month_days} днів у місяці, "
        f"залишилося {remaining} днів"
    )
