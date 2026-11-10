from pathlib import Path
from datetime import date
import math
import sys

print("Mushka Vlad IT31")

file_path = Path(__file__).parent / "data" / "expenses.csv"

expenses = {}

try:
    lines = file_path.read_text(encoding="utf-8").splitlines()
except OSError as error:
    print(f"Помилка: {error}", file=sys.stderr)
    sys.exit(1)

for line in lines:
    line = line.strip()

    if not line or line.startswith("#"):
        continue

    try:
        date_text, category, amount_text, note = line.split(";")
        day = date.fromisoformat(date_text)
        amount = float(amount_text)

        expenses.setdefault(day, []).append(amount)

    except ValueError:
        print(f"Некоректний рядок: {line}", file=sys.stderr)

if not expenses:
    print("Немає даних для аналізу.")
    sys.exit(0)

first_day = min(expenses)
last_day = max(expenses)

days_count = (last_day - first_day).days + 1

all_days = [
    date.fromordinal(first_day.toordinal() + i)
    for i in range(days_count)
]

daily_totals = {
    day: math.fsum(expenses.get(day, []))
    for day in all_days
}

weekday_names = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

print("Mushka Vlad IT31")
print(f"period: {first_day:%d.%m.%Y} ({first_day:%A}) - "
      f"{last_day:%d.%m.%Y} ({last_day:%A}), {days_count} days")

print()
print("weekday      total")

for weekday in range(7):
    total = math.fsum(
        value for day, value in daily_totals.items()
        if day.weekday() == weekday
    )
    print(f"{weekday_names[weekday]:<12}{total:>7.2f}")

total = math.fsum(daily_totals.values())
average = total / days_count

std_dev = math.sqrt(
    math.fsum((value - average) ** 2 for value in daily_totals.values())
    / days_count
)

top_day = max(daily_totals, key=daily_totals.get)
no_spend_days = sum(value == 0 for value in daily_totals.values())

month_start = last_day.replace(day=1)

if last_day.month == 12:
    next_month = date(last_day.year + 1, 1, 1)
else:
    next_month = date(last_day.year, last_day.month + 1, 1)

days_in_month = (next_month - month_start).days
days_left = days_in_month - last_day.day

forecast = average * days_in_month

print()
print(f"total:        {total:.2f}")
print(f"per day:      {average:.2f} +- {std_dev:.2f}")
print(f"top day:      {top_day:%d.%m.%Y} ({top_day:%A}), "
      f"{daily_totals[top_day]:.2f}")
print(f"no-spend days: {no_spend_days}")
print(f"days in {last_day:%B}: {days_in_month}, "
      f"left after {last_day:%d.%m}: {days_left}")
print(f"month forecast: {forecast:.2f}")