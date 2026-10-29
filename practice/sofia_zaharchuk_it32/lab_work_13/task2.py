import math
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

FILE = Path(__file__).resolve().parent / "data" / "expenses.csv"
WEEKDAYS = [(date(2024, 1, 1) + timedelta(days=i)).strftime("%A") for i in range(7)]  # Mon..Sun


def days_in_month(d: date) -> int:
    first = d.replace(day=1)
    nxt = (first + timedelta(days=32)).replace(day=1)
    return (nxt - first).days


def load(path: Path) -> dict[date, float]:
    by_day: dict[date, float] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        sys.exit(f"error: cannot read {path}: {e}")
    for n, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";")
        try:
            d = datetime.strptime(parts[0].strip(), "%Y-%m-%d").date()
            amount = float(parts[2].replace(",", "."))
        except (ValueError, IndexError):
            print(f"warning: line {n} skipped: {line!r}", file=sys.stderr)
            continue
        by_day[d] = by_day.get(d, 0.0) + amount
    return by_day


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    by_day = load(FILE)
    if not by_day:
        sys.exit("error: no valid expenses")

    first, last = min(by_day), max(by_day)
    span = (last - first).days + 1
    print(f"period: {first:%d.%m.%Y} ({first:%A}) - {last:%d.%m.%Y} ({last:%A}), {span} days")
    print()

    daily = [by_day.get(first + timedelta(days=i), 0.0) for i in range(span)]
    week = [0.0] * 7
    for d, s in by_day.items():
        week[d.weekday()] += s
    print("weekday      total")
    for name, s in zip(WEEKDAYS, week):
        print(f"{name:<11} {s:8.2f}")
    print()

    total = math.fsum(daily)
    mean = total / span
    std = math.sqrt(math.fsum((x - mean) ** 2 for x in daily) / span)
    top = max(by_day, key=by_day.get)
    no_spend = sum(1 for x in daily if x == 0)
    dim = days_in_month(last)
    left = dim - last.day

    print(f"total:        {total:.2f}")
    print(f"per day:      {mean:.2f} +- {std:.2f}")
    print(f"top day:      {top:%d.%m.%Y} ({top:%A}), {by_day[top]:.2f}")
    print(f"no-spend days: {no_spend}")
    print(f"days in {last:%B}: {dim}, left after {last:%d.%m}: {left}")
    print(f"month forecast: {mean * dim:.2f}")

    # перевірка кількості днів у місяці
    print(f"check 2026-12: {days_in_month(date(2026, 12, 15))}, 2028-02: {days_in_month(date(2028, 2, 10))}")


main()
