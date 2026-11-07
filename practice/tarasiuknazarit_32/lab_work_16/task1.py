import csv
import json
import os

print("Nazar Tarasiuk, I-23")

records = []

with open('data/expenses.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')

    for row in reader:
        records.append({
            'date': row[0],
            'category': row[1],
            'amount': float(row[2]),
            'comment': row[3]
        })

with open('data/expenses.json', 'w', encoding='utf-8') as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

size = os.path.getsize('data/expenses.json')

print(f'records: {len(records)}')
print(f'saved: data/expenses.json ({size} bytes)')