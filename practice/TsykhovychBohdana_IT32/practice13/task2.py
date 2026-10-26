import csv
import math
from datetime import datetime, timedelta
from collections import defaultdict

print("Студент: Богдана Цихович, група: ІТ-32")

expenses = defaultdict(float)

with open('data/expenses.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:
        day = datetime.strptime(row['date'], '%Y-%m-%d').date()
        expenses[day] += float(row['amount'])

start = min(expenses.keys())
end = max(expenses.keys())

days = [start + timedelta(days=i) for i in range((end - start).days + 1)]

values = [expenses[day] for day in days]

total = math.fsum(values)
average = total / len(days)
std = math.sqrt(math.fsum((x - average) ** 2 for x in values) / len(days))

top_day = max(days, key=expenses.get)
no_spend = values.count(0)

month_start = end.replace(day=1)
if end.month == 12:
    next_month_start = end.replace(year=end.year + 1, month=1, day=1)
else:
    next_month_start = end.replace(month=end.month + 1, day=1)

month_days = (next_month_start - month_start).days
left = (next_month_start - end).days - 1
forecast = average * month_days

print(f"Період: {start.strftime('%d.%m.%Y')} ({start.strftime('%A')}) - {end.strftime('%d.%m.%Y')} ({end.strftime('%A')}), тривалість: {((end - start).days + 1)} днів")
print(f"Сума витрат за кожним днем ​​тижня:")
for i, day in enumerate(days):
    print(f"  {day.strftime('%A')}: {expenses[day]:.2f} грн")
print(f"Загальна сума: {total:.2f} грн")
print(f"Середні витрати на день: {average:.2f} грн")
print(f"Стандартне відхилення: {std:.2f} грн")
print(f"День з найбільшими витратами: {top_day.strftime('%d.%m.%Y')} ({expenses[top_day]:.2f} грн)")
print(f"Кількість днів без витрат: {no_spend}")

print(f"Кількість днів у місяць: {month_days}")
print(f"Кількість днів до кінця місяця: {left}")
print(f"Прогноз витрат на весь місяць: {forecast:.2f} грн")
