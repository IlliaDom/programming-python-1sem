import json
from datetime import date
from pathlib import Path

print('Діана Мельник, І-23', flush=True)
base = Path(__file__).resolve().parent / 'data'
with (base / 'expenses.json').open(encoding='utf-8') as f:
    records = json.load(f)
records.append({'date': date.today().isoformat(), 'category': 'food',
                'amount': 65, 'comment': 'Обід'})
before = len(records)
records = [r for r in records if r['amount'] >= 10]
with (base / 'expenses_updated.json').open('w', encoding='utf-8') as f:
    json.dump(records, f, indent=2, ensure_ascii=False)
print('added: 1')
print(f'removed: {before - len(records)}')
print(f'records: {len(records)}')
