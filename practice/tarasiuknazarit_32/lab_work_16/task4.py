import json
from datetime import date

print("Nazar Tarasiuk, I-23")

today = date.today()

data = {
    'name': 'Nazar',
    'date': today
}

try:
    json_text = json.dumps(data)
except TypeError as error:
    print('TypeError:', error)

def date_to_string(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f'Type {type(obj)} is not JSON serializable')


json_text = json.dumps(data, default=date_to_string, ensure_ascii=False)
print('Method 1:', json_text)


data_for_json = {
    'name': data['name'],
    'date': data['date'].isoformat()
}

json_text = json.dumps(data_for_json, ensure_ascii=False)

restored_data = json.loads(json_text)
restored_data['date'] = date.fromisoformat(restored_data['date'])

print('Method 2:', restored_data)
print('Restored date type:', type(restored_data['date']))
print('Data equals original:', restored_data == data)