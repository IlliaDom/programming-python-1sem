import math
import sys
from datetime import date, timedelta
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

DATA_FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"


def days_in_month(d):
    first = d.replace(day=1)
    if first.month == 12:
        next_first = date(first.year + 1, 1, 1)
    else:
        next_first = date(first.year, first.month + 1, 1)
    return (next_first - first).days


def read_expenses(path):
    """Повертає список (date, amount). Погані рядки — попередження в stderr."""
    rows = []
    with path.open(encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            try:
                if len(parts) < 3:
                    raise ValueError("expected at least 3 fields")
                d = date.fromisoformat(parts[0].strip())
                amount = float(parts[2].strip())
            except ValueError as e:
                print(f"warning: line {number} skipped ({e}): {line}",
                      file=sys.stderr)
                continue
            rows.append((d, amount))
    return rows


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    if not DATA_FILE.is_file():
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)

    rows = read_expenses(DATA_FILE)
    if not rows:
        print("error: no valid expenses", file=sys.stderr)
        sys.exit(1)

    first = min(d for d, _ in rows)
    last = max(d for d, _ in rows)
    period_days = (last - first).days + 1

    by_date = {}
    for d, amount in rows:
        by_date.setdefault(d, []).append(amount)
    day_totals = {}
    for i in range(period_days):
        d = first + timedelta(days=i)
        day_totals[d] = math.fsum(by_date.get(d, []))

    print(f"period: {first:%d.%m.%Y} ({first:%A}) - "
          f"{last:%d.%m.%Y} ({last:%A}), {period_days} days")
    print()

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
    week = {name: [] for name in weekdays}
    for d, total in day_totals.items():
        week[d.strftime("%A")].append(total)
    print(f"{'weekday':<12} total")
    for name in weekdays:
        print(f"{name:<12} {math.fsum(week[name]):>7.2f}")
    print()

    values = list(day_totals.values())
    total = math.fsum(v for _, v in rows)
    mean = total / period_days
    variance = math.fsum((v - mean) ** 2 for v in values) / period_days
    std = math.sqrt(variance)
    print(f"total:        {total:.2f}")
    print(f"per day:      {mean:.2f} +- {std:.2f}")

    top_day = max(day_totals, key=day_totals.get)
    no_spend = sum(1 for v in values if v == 0)
    print(f"top day:      {top_day:%d.%m.%Y} ({top_day:%A}), "
          f"{day_totals[top_day]:.2f}")
    print(f"no-spend days: {no_spend}")

    dim = days_in_month(last)
    left = dim - last.day
    print(f"days in {last:%B}: {dim}, left after {last:%d.%m}: {left}")
    print(f"month forecast: {mean * dim:.2f}")


if __name__ == "__main__":
    main()
