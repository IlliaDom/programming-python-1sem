import math
import sys
from pathlib import Path
from datetime import date, timedelta

# Personal information
print("Sofia Stotska, IT-31")

# File path
file_path = Path(__file__).parent / "data" / "expenses.csv"

if not file_path.exists():
    print("Error: expenses.csv not found", file=sys.stderr)
    sys.exit(1)

# Read expenses
expenses = {}

with file_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        if len(parts) != 4:
            print(f"Warning: invalid line {line_number}", file=sys.stderr)
            continue

        try:
            expense_date = date.fromisoformat(parts[0])
            amount = float(parts[2])

            if not math.isfinite(amount) or amount < 0:
                raise ValueError

        except ValueError:
            print(f"Warning: invalid line {line_number}", file=sys.stderr)
            continue

        expenses.setdefault(expense_date, []).append(amount)

if not expenses:
    print("No valid expenses found", file=sys.stderr)
    sys.exit(1)

# Period
first_date = min(expenses)
last_date = max(expenses)

period_days = (last_date - first_date).days + 1

print(
    f"period: {first_date.strftime('%d.%m.%Y')} "
    f"({first_date.strftime('%A')}) - "
    f"{last_date.strftime('%d.%m.%Y')} "
    f"({last_date.strftime('%A')}), {period_days} days"
)

# Daily expenses
daily_totals = {}

current_date = first_date

while current_date <= last_date:
    daily_totals[current_date] = math.fsum(
        expenses.get(current_date, [])
    )
    current_date += timedelta(days=1)

# Weekday totals
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print("\nweekday      total")

for weekday_number, weekday_name in enumerate(weekdays):
    total = math.fsum(
        amount
        for day, amount in daily_totals.items()
        if day.weekday() == weekday_number
    )

    print(f"{weekday_name:<12} {total:8.2f}")

# Statistics
total = math.fsum(daily_totals.values())
average = total / period_days

variance = math.fsum(
    (amount - average) ** 2
    for amount in daily_totals.values()
) / period_days

standard_deviation = math.sqrt(variance)

top_day = max(daily_totals, key=daily_totals.get)
no_spend_days = sum(
    1 for amount in daily_totals.values() if amount == 0
)

print(f"\ntotal:        {total:.2f}")
print(f"per day:      {average:.2f} +- {standard_deviation:.2f}")

print(
    f"top day:      {top_day.strftime('%d.%m.%Y')} "
    f"({top_day.strftime('%A')}), {daily_totals[top_day]:.2f}"
)

print(f"no-spend days: {no_spend_days}")

# Month calculation
month_start = date(last_date.year, last_date.month, 1)

if last_date.month == 12:
    next_month = date(last_date.year + 1, 1, 1)
else:
    next_month = date(last_date.year, last_date.month + 1, 1)

days_in_month = (next_month - month_start).days
days_left = (next_month - last_date).days

month_forecast = average * days_in_month

print(
    f"days in {last_date.strftime('%B')}: "
    f"{days_in_month}, left after {last_date.strftime('%d.%m')}: {days_left}"
)

print(f"month forecast: {month_forecast:.2f}")