import json
from datetime import date
from pathlib import Path

print('Діана Мельник, І-23', flush=True)
base = Path(__file__).resolve().parent / 'data'
original = {'date': date.today(), 'amount': 65, 'comment': 'Обід'}
try:
    json.dumps(original)
except TypeError as e:
    print(f'TypeError: {e}')

def encode_date(value):
    if isinstance(value, date):
        return value.isoformat()
    raise TypeError(f'Unsupported type: {type(value).__name__}')

encoded = json.dumps(original, default=encode_date, ensure_ascii=False)
restored = json.loads(encoded)
restored['date'] = date.fromisoformat(restored['date'])
print('default:', encoded)
print('equal:', restored == original)

def to_json(value):
    if isinstance(value, date):
        return {'__date__': value.isoformat()}
    if isinstance(value, dict):
        return {k: to_json(v) for k, v in value.items()}
    if isinstance(value, list):
        return [to_json(v) for v in value]
    return value

def from_json(value):
    if isinstance(value, dict):
        if set(value) == {'__date__'}:
            return date.fromisoformat(value['__date__'])
        return {k: from_json(v) for k, v in value.items()}
    if isinstance(value, list):
        return [from_json(v) for v in value]
    return value

path = base / 'date_example.json'
with path.open('w', encoding='utf-8') as f:
    json.dump(to_json(original), f, indent=2, ensure_ascii=False)
with path.open(encoding='utf-8') as f:
    restored = from_json(json.load(f))
print('custom equal:', restored == original)
print('date type:', type(restored['date']).__name__)
