import json
from datetime import date
from pathlib import Path

print("Maria Vovk, І-23")

BASE_DIR = Path(__file__).parent
sample = {"owner": "Maria Vovk", "created": date(2026, 11, 12)}

# Початкова спроба: стандартний JSON не підтримує date.
try:
    json.dumps(sample, ensure_ascii=False)
except TypeError as error:
    print(f"TypeError: {error}")

# Спосіб 1 — параметр default.
json_text = json.dumps(
    sample,
    default=lambda value: value.isoformat() if isinstance(value, date) else str(value),
    ensure_ascii=False
)
restored = json.loads(json_text)
print(f"default result: {restored}")

# Спосіб 2 — власне перетворення перед записом і після читання.
def encode_dates(value):
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: encode_dates(item) for key, item in value.items()}
    if isinstance(value, list):
        return [encode_dates(item) for item in value]
    return value

def decode_dates(value):
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if key == "created" and isinstance(item, str):
                result[key] = date.fromisoformat(item)
            else:
                result[key] = decode_dates(item)
        return result
    if isinstance(value, list):
        return [decode_dates(item) for item in value]
    return value

path = BASE_DIR / "date_example.json"
with path.open("w", encoding="utf-8") as file:
    json.dump(encode_dates(sample), file, indent=2, ensure_ascii=False)

with path.open("r", encoding="utf-8") as file:
    loaded = decode_dates(json.load(file))

print(f"round trip equal: {loaded == sample}")
print(f"date type after reading: {type(loaded['created']).__name__}")
