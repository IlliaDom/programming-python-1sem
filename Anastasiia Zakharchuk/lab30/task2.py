import math
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

NAME = "Anastasia"
SURNAME = "Zakharchuk"
GROUP = "IT-32"

BASE = Path(__file__).resolve().parent
EXPENSES = BASE / "data" / "expenses.csv"

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]


def parse_line(line):
    parts = line.split(";")
    if len(parts) != 4:
        raise ValueError(f"expected 4 fields, got {len(parts)}")
    day = datetime.strptime(parts[0], "%Y-%m-%d").date()
    amount = float(parts[2])
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount:.2f}")
    return day, amount


def read_expenses(path):
    records = []
    with open(path, encoding="utf-8") as f:
        for number, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            try:
                records.append(parse_line(line))
            except ValueError as e:
                print(f"warning: line {number} skipped: {e}",
                      file=sys.stderr)
    return records


def days_in_month(day):
    first = date(day.year, day.month, 1)
    if day.month == 12:
        next_first = date(day.year + 1, 1, 1)
    else:
        next_first = date(day.year, day.month + 1, 1)
    return (next_first - first).days


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    try:
        records = read_expenses(EXPENSES)
    except FileNotFoundError:
        print(f"error: {EXPENSES.name} not found", file=sys.stderr)
        sys.exit(1)

    if not records:
        print("error: no valid records", file=sys.stderr)
        sys.exit(1)

    by_date = {}
    for day, amount in records:
        by_date[day] = by_date.get(day, 0.0) + amount

    first = min(by_date)
    last = max(by_date)
    n_days = (last - first).days + 1

    print(f"period: {first:%d.%m.%Y} ({first:%A}) - "
          f"{last:%d.%m.%Y} ({last:%A}), {n_days} days")

    # суми за днями тижня (0 = понеділок)
    by_weekday = [0.0] * 7
    for day, day_total in by_date.items():
        by_weekday[day.weekday()] += day_total

    print()
    print(f"{'weekday':<12}{'total':>8}")
    for i in range(7):
        print(f"{DAYS[i]:<12}{by_weekday[i]:>8.2f}")

    daily = []
    for i in range(n_days):
        daily.append(by_date.get(first + timedelta(days=i), 0.0))

    total = math.fsum(daily)
    mean = total / n_days
    std = math.sqrt(math.fsum((x - mean) ** 2 for x in daily) / n_days)

    top_day = max(by_date, key=by_date.get)
    no_spend = n_days - len(by_date)

    print()
    print(f"total:        {total:.2f}")
    print(f"per day:      {mean:.2f} +- {std:.2f}")
    print(f"top day:      {top_day:%d.%m.%Y} ({top_day:%A}), "
          f"{by_date[top_day]:.2f}")
    print(f"no-spend days: {no_spend}")

    month_days = days_in_month(last)
    left = month_days - last.day
    forecast = mean * month_days
    print(f"days in {last:%B}: {month_days}, left after {last:%d.%m}: {left}")
    print(f"month forecast: {forecast:.2f}")


if __name__ == "__main__":
    main()