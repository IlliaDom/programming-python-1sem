import json
import sys
from pathlib import Path

print('Діана Мельник, І-23', flush=True)
base = Path(__file__).resolve().parent
path = base / 'settings.json'
if not path.exists():
    settings = {'owner': 'Діана Мельник', 'group': 'І-23',
                'currency': 'UAH', 'monthly_limit': 6000,
                'categories': ['food', 'transport', 'coffee', 'books', 'internet']}
    with path.open('w', encoding='utf-8') as f:
        json.dump(settings, f, indent=2, ensure_ascii=False)
    print('settings.json not found, default created')
else:
    try:
        with path.open(encoding='utf-8') as f:
            settings = json.load(f)
    except json.JSONDecodeError as e:
        print(f'JSON error at line {e.lineno}: {e.msg}', file=sys.stderr)
        sys.exit(1)
    with (base / 'data/expenses.json').open(encoding='utf-8') as f:
        records = json.load(f)
    spent = sum(r['amount'] for r in records)
    limit = settings['monthly_limit']
    currency = settings['currency']
    print(json.dumps(settings, ensure_ascii=False))
    print(f'limit: {limit:.2f} {currency}, spent: {spent:.2f} {currency}, left: {limit-spent:.2f} {currency}')
