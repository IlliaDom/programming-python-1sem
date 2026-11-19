import csv
import json
from pathlib import Path

print('Діана Мельник, І-23', flush=True)
base = Path(__file__).resolve().parent
source = base / 'data/expenses.csv'
target = base / 'data/expenses.json'
with source.open(encoding='utf-8-sig', newline='') as f:
    records = [dict(date=r['date'], category=r['category'],
                    amount=float(r['amount']), comment=r.get('comment', r.get('note', '')))
               for r in csv.DictReader(f)]
with target.open('w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, ensure_ascii=False)
print(f'records: {len(records)}')
print(f'saved: data/expenses.json ({target.stat().st_size} bytes)')
