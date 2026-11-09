from datetime import date, datetime, timedelta
import math
from pathlib import Path
import sys

print("Батура Каріна Віталіївна, ІТ-31")

expenses_path = Path("data") / "expenses.csv"
if not expenses_path.exists():
    sys.exit(f"error: file {expenses_path} not found")

records = []
line_num = 0

with open(expenses_path, "r", encoding="utf-8") as f:
    for line in f:
        line_num += 1
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";")
        if len(parts) < 3:
            print(
                f"warning: malformed line {line_num}: {line}",
                file=sys.stderr,
            )
            continue
        try:
            d_str, category, amount_str = parts[0].strip(
            ), parts[1].strip(), parts[2].strip()
            dt = datetime.strptime(d_str, "%Y-%m-%d").date()
            amount = float(amount_str)
            records.append((dt, amount))
        except ValueError as e:
            print(
                f"warning: error parsing line {line_num} ({e}): {line}",
                file=sys.stderr,
            )

if not records:
    sys.exit("error: no valid expense records found")

records.sort(key=lambda x: x[0])
first_date = records[0][0]
last_date = records[-1][0]
period_days = (last_date - first_date).days + 1

print(
    f"period: {first_date:%d.%m.%Y} ({first_date:%A}) - {last_date:%d.%m.%Y} ({last_date:%A}), {period_days} days\n"
)

# Витрати за днями тижня (0 - Понеділок, 6 - Неділя)
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
wd_totals = {wd: 0.0 for wd in weekdays}

# Заповнюємо всі дні у періоді (навіть з 0 витратами)
current = first_date
all_daily_totals = {}
while current <= last_date:
    all_daily_totals[current] = 0.0
    current += timedelta(days=1)

for dt, amount in records:
    all_daily_totals[dt] += amount

for dt, amount in all_daily_totals.items():
    wd_name = dt.strftime("%A")
    wd_totals[wd_name] += amount

print(f"{'weekday':<12} {'total':<10}")
for wd in weekdays:
    print(f"{wd:<12} {wd_totals[wd]:.2f}")

all_amounts = [amount for _, amount in records]
total_sum = math.fsum(all_amounts)

# Дні без витрат усередині періоду рахуються як 0
daily_values = list(all_daily_totals.values())
mean_day = sum(daily_values) / len(daily_values)
variance = sum((v - mean_day) ** 2 for v in daily_values) / len(daily_values)
std_dev = math.sqrt(variance)

top_day_dt = max(all_daily_totals, key=all_daily_totals.get)
top_day_sum = all_daily_totals[top_day_dt]
no_spend_days = sum(1 for v in daily_values if v == 0.0)

# Дні в місяці останньої дати через різницю дат 
if last_date.month == 12:
    next_month_first = date(last_date.year + 1, 1, 1)
else:
    next_month_first = date(last_date.year, last_date.month + 1, 1)
current_month_first = date(last_date.year, last_date.month, 1)
days_in_month = (next_month_first - current_month_first).days
days_left = (next_month_first - last_date).days - 1
month_forecast = mean_day * days_in_month

print(f"\ntotal:        {total_sum:.2f}")
print(f"per day:      {mean_day:.2f} +- {std_dev:.2f}")
print(
    f"top day:      {top_day_dt:%d.%m.%Y} ({top_day_dt:%A}), {top_day_sum:.2f}"
)
print(f"no-spend days: {no_spend_days}")
print(
    f"days in {last_date:%B}: {days_in_month}, left after {last_date:%d.%m.%Y}: {days_left}"
)
print(f"month forecast: {month_forecast:.2f}")