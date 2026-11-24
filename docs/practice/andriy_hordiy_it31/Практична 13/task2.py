from datetime import date, datetime, timedelta
import sys
from pathlib import Path
import math
reader = []
path = Path("../Практична 10/data/expenses.csv").resolve()
with open(path, "r", encoding="utf-8") as expenses:
    for expense in expenses.readlines()[1:]:
        reader.append(expense)
dates = []
for expense in reader:
    dates.append((datetime.strptime((expense.split("|")[0]),"%d.%m.%Y").date()))

print(f"Hordiy Andriy IT-31\nPeriod: {dates[0].strftime('%d.%m.%Y')} ({dates[0].strftime('%A')}) - {dates[-1].strftime('%d.%m.%Y')} ({dates[-1].strftime('%A')}), {(dates[-1]-dates[0]).days} days.")


week = {
    "Monday" : 0,
    "Tuesday" : 0,
    "Wednesday" : 0,
    "Thursday" : 0,
    "Friday" : 0,
    "Saturday" : 0,
    "Sunday" : 0
}
cost = 0
def week_expense(day):
    for days in week:
        if days == day:
            week[days] += cost
full_cost = []
daily_cost ={}
for expense in reader:
    day = datetime.strptime(expense.split("|")[0], "%d.%m.%Y").strftime("%A")
    dni = datetime.strptime(expense.split("|")[0], "%d.%m.%Y").date()
    cost = float(expense.split("|")[2])
    if dni not in daily_cost:
        daily_cost[dni] = 0
    daily_cost[dni] += cost
    week_expense(day)
    full_cost.append(cost)
for days in week:
    print(f"{days}: {week[days]} UAH")
avg = math.fsum(daily_cost.values()) / len(daily_cost)

deviation = math.sqrt(
    math.fsum((x - avg) ** 2 for x in daily_cost.values()) / len(daily_cost)
)
maxday = max(daily_cost, key=daily_cost.get)
print(f"\ntotal: {math.fsum(full_cost):.2f} UAH")
print(f"per day: {avg:.2f} UAH +- {deviation:.2f}")
print(f"top day: {maxday} - {daily_cost[maxday]} UAH")
all_days = [
    min(dates) + timedelta(days=i)
    for i in range((max(dates) - min(dates)).days + 1)
]
no_expense = sum(1 for day in all_days if day not in daily_cost)
print(f"no-spend days: {no_expense}")
