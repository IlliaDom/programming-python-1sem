import math
import sys
from datetime import date, timedelta

name, surname, group = "Yaroslav", "Korolchuk", "IT-31"
print(f"{name} {surname}, {group}")

spent = {}
with open("data/expenses.csv", encoding="utf-8") as f:
    for n, line in enumerate(f, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            d, cat, amount, note = line.split(";", 3)
            d = date.fromisoformat(d)
            amount = float(amount)
        except ValueError:
            print(f"warning: line {n} skipped", file=sys.stderr)
            continue
        spent[d] = spent.get(d, 0) + amount

if not spent:
    print("error: no data", file=sys.stderr)
    sys.exit(1)

first, last = min(spent), max(spent)
days = (last - first).days + 1
print(f"period: {first:%d.%m.%Y} ({first:%A}) - {last:%d.%m.%Y} ({last:%A}), {days} days")

daily = []
by_weekday = [0.0] * 7
for i in range(days):
    d = first + timedelta(days=i)
    s = spent.get(d, 0)
    daily.append(s)
    by_weekday[d.weekday()] += s

names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print()
print("weekday      total")
for nm, s in zip(names, by_weekday):
    print(f"{nm:<12} {s:.2f}")

total = math.fsum(daily)
mean = total / days
std = math.sqrt(math.fsum((x - mean) ** 2 for x in daily) / days)
top = max(spent, key=spent.get)
no_spend = daily.count(0)
print()
print(f"total:        {total:.2f}")
print(f"per day:      {mean:.2f} +- {std:.2f}")
print(f"top day:      {top:%d.%m.%Y} ({top:%A}), {spent[top]:.2f}")
print(f"no-spend days: {no_spend}")

start = last.replace(day=1)
if last.month == 12:
    nxt = date(last.year + 1, 1, 1)
else:
    nxt = date(last.year, last.month + 1, 1)
month_days = (nxt - start).days
left = month_days - last.day
print(f"days in {last:%B}: {month_days}, left after {last:%d.%m}: {left}")
print(f"month forecast: {mean * month_days:.2f}")