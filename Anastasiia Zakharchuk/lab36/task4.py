import json
from datetime import date

print("Anastasia Zakharchuk, IT-32")

data = {"title": "expenses", "start": date(2026, 9, 21), "items": [{"day": date(2026, 9, 22), "amount": 85.5}]}

try:
    json.dumps(data)
except TypeError as e:
    print("TypeError:", e)


def date_default(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"{type(obj).__name__} is not serializable")


text1 = json.dumps(data, default=date_default)
print("method 1:", text1)
back1 = json.loads(text1)
print("method 1 start type:", type(back1["start"]).__name__)


def encode_dates(obj):
    if isinstance(obj, date):
        return {"__date__": obj.isoformat()}
    if isinstance(obj, dict):
        return {k: encode_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [encode_dates(x) for x in obj]
    return obj


def decode_dates(obj):
    if isinstance(obj, dict):
        if list(obj.keys()) == ["__date__"]:
            return date.fromisoformat(obj["__date__"])
        return {k: decode_dates(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [decode_dates(x) for x in obj]
    return obj


text2 = json.dumps(encode_dates(data))
print("method 2:", text2)
back2 = decode_dates(json.loads(text2))
print("method 2 equal:", back2 == data)
print("start is date:", isinstance(back2["start"], date))
print("day is date:", isinstance(back2["items"][0]["day"], date))
