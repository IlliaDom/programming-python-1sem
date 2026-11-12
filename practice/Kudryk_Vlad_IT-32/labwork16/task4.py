import json
from datetime import date

print("Vlad Kudryk, IT-32")

data = {"title": "report", "day": date(2026, 11, 12)}

try:
    json.dumps(data)
except TypeError as e:
    print("TypeError:", e)

def date_to_str(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("not supported")

print(json.dumps(data, default=date_to_str))

def dates_to_strings(d):
    result = dict(d)
    result["day"] = d["day"].isoformat()
    return result

def strings_to_dates(d):
    result = dict(d)
    result["day"] = date.fromisoformat(d["day"])
    return result

text = json.dumps(dates_to_strings(data))
restored = strings_to_dates(json.loads(text))

print(restored == data)
print(type(restored["day"]))