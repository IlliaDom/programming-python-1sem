import math
import sys
from pathlib import Path
from datetime import date, timedelta

name = "Nikita"
surname = "Krilovets"
group = "IT-31"

print(f"{name} {surname}, {group}")

file_path = Path(__file__).parent / "data" / "expenses.csv"

if not file_path.exists():
    print("error: expenses.csv not found", file=sys.stderr)
    sys.exit(1)

daily_totals = {}

with file_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        if len(parts) != 4 or parts[0].strip().lower() == "date":
            if len(parts) == 4 and parts[0].strip().lower() == "date":
                continue

            print(f"warning: invalid line {line_number}", file=sys.stderr)
            continue

        try:
            expense_date = date.fromisoformat(parts[0].strip())
            amount = float(parts[2].strip())

            if not math.isfinite(amount):
                raise ValueError

        except ValueError:
            print(f"warning: invalid line {line_number}", file=sys.stderr)
            continue

        daily_totals[expense_date] = daily_totals.get(expense_date, 0) + amount

if not daily_totals:
    print("error: no valid expense records", file=sys.stderr)
    sys.exit(1)

first_date = min(daily_totals)
last_date = max(daily_totals)

days_count = (last_date - first_date).days + 1

print(
    f"period: {first_date.strftime('%d.%m.%Y')} "
    f"({first_date.strftime('%A')}) - "
    f"{last_date.strftime('%d.%m.%Y')} "
    f"({last_date.strftime('%A')}), {days_count} days"
)

print()
print("weekday      total")

weekday_totals = [0.0] * 7

for current_date, amount in daily_totals.items():
    weekday_totals[current_date.weekday()] += amount

for i in range(7):
    weekday = date(2026, 1, 5 + i).strftime("%A")
    print(f"{weekday:<12} {weekday_totals[i]:>8.2f}")

total = math.fsum(daily_totals.values())

average = total / days_count

daily_values = [
    daily_totals.get(first_date + timedelta(days=i), 0)
    for i in range(days_count)
]

variance = math.fsum((value - average) ** 2 for value in daily_values) / days_count
std_deviation = math.sqrt(variance)

top_day = max(daily_values)
top_date = first_date + timedelta(days=daily_values.index(top_day))

no_spend_days = sum(1 for value in daily_values if value == 0)

print()
print(f"total:        {total:.2f}")
print(f"per day:      {average:.2f} +- {std_deviation:.2f}")
print(
    f"top day:      {top_date.strftime('%d.%m.%Y')} "
    f"({top_date.strftime('%A')}), {top_day:.2f}"
)
print(f"no-spend days: {no_spend_days}")

if last_date.month == 12:
    next_month = date(last_date.year + 1, 1, 1)
else:
    next_month = date(last_date.year, last_date.month + 1, 1)

first_month_day = date(last_date.year, last_date.month, 1)

days_in_month = (next_month - first_month_day).days
days_left = days_in_month - last_date.day

forecast = average * days_in_month

print(
    f"days in {last_date.strftime('%B')}: "
    f"{days_in_month}, left after {last_date.strftime('%d.%m')}: {days_left}"
)
print(f"month forecast: {forecast:.2f}")