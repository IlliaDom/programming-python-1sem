import json
import sys

print("Nazar Tarasiuk, I-23")

settings_file = 'settings.json'

default_settings = {
    'monthly_limit': 2000,
    'currency': 'UAH',
    'language': 'uk'
}

try:
    with open(settings_file, 'r', encoding='utf-8') as file:
        settings = json.load(file)

    print('Settings loaded:')
    print(settings)

except FileNotFoundError:
    settings = default_settings

    with open(settings_file, 'w', encoding='utf-8') as file:
        json.dump(settings, file, indent=2, ensure_ascii=False)

    print('Settings file created:')
    print(settings)

except json.JSONDecodeError as error:
    print(f'JSON error on line {error.lineno}', file=sys.stderr)
    sys.exit(1)

with open('data/expenses.json', 'r', encoding='utf-8') as file:
    expenses = json.load(file)

total = sum(record['amount'] for record in expenses)

print(f'Total expenses: {total:.2f}')
print(f'Monthly limit: {settings["monthly_limit"]}')

if total > settings['monthly_limit']:
    print('Warning: monthly limit exceeded!')
else:
    print('Monthly limit is not exceeded.')