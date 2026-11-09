import sys
from pathlib import Path
from datetime import datetime, timedelta
import math
from collections import defaultdict

NAME_SURNAME = "Oleksandra Romanich"
GROUP = "IT-32"

def get_month_days(d: datetime.date) -> int:
    if d.month == 12:
        next_month = d.replace(year=d.year + 1, month=1, day=1)
    else:
        next_month = d.replace(month=d.month + 1, day=1)
    current_month = d.replace(day=1)
    return (next_month - current_month).days

def main():
    print(f"{NAME_SURNAME}, {GROUP}")
    
    file_path = Path("data/expenses.csv")
    if not file_path.exists():
        print(f"Error: {file_path} not found", file=sys.stderr)
        sys.exit(1)

    expenses = []
    with file_path.open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            if len(parts) != 4:
                print(f"Warning: line {line_num} is corrupted, skipping", file=sys.stderr)
                continue
            try:
                date_str, category, amount_str, desc = parts
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                amount = float(amount_str)
                expenses.append((date_obj, amount))
            except ValueError:
                print(f"Warning: line {line_num} has invalid data, skipping", file=sys.stderr)

    if not expenses:
        print("No valid data found.", file=sys.stderr)
        sys.exit(1)

    expenses.sort(key=lambda x: x[0])
    first_date, last_date = expenses[0][0], expenses[-1][0]
    period_days = (last_date - first_date).days + 1

    print(f"period: {first_date.strftime('%d.%m.%Y')} ({first_date.strftime('%A')}) - "
          f"{last_date.strftime('%d.%m.%Y')} ({last_date.strftime('%A')}), {period_days} days")
    print()

    weekday_totals = defaultdict(float)
    for d, amt in expenses:
        weekday_totals[d.weekday()] += amt

    print("weekday      total")
    days_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i, name in enumerate(days_names):
        print(f"{name:<12} {weekday_totals[i]:>7.2f}")
    print()

    total_spent = math.fsum(amt for _, amt in expenses)
    daily_averages = []
    current = first_date
    while current <= last_date:
        day_sum = sum(amt for d, amt in expenses if d == current)
        daily_averages.append(day_sum)
        current += timedelta(days=1)

    avg_per_day = total_spent / period_days
    variance = sum((x - avg_per_day) ** 2 for x in daily_averages) / period_days
    std_dev = math.sqrt(variance)

    top_day_date, top_day_amt = max(expenses, key=lambda x: x[1])
    no_spend_days = sum(1 for x in daily_averages if x == 0)

    print(f"total:        {total_spent:.2f}")
    print(f"per day:      {avg_per_day:.2f} +- {std_dev:.2f}")
    print(f"top day:      {top_day_date.strftime('%d.%m.%Y')} ({top_day_date.strftime('%A')}), {top_day_amt:.2f}")
    print(f"no-spend days: {no_spend_days}")

    last_month_days = get_month_days(last_date)
    days_left = last_month_days - last_date.day
    print(f"days in {last_date.strftime('%B')}: {last_month_days}, left after {last_date.strftime('%d.%m')}: {days_left}")
    print(f"month forecast: {avg_per_day * last_month_days:.2f}")

if __name__ == "__main__":
    main()