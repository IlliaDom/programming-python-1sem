import json
from datetime import date

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

data = {
    "owner": f"{NAME} {SURNAME}",
    "created": date(2026, 9, 21),
    "items": [
        {"date": date(2026, 9, 21), "amount": 85.5},
        {"date": date(2026, 9, 22), "amount": 14.5},
    ],
}


def date_default(obj):
    if isinstance(obj, date):
        return {"__date__": obj.isoformat()}
    raise TypeError(f"not serializable: {type(obj).__name__}")


def date_hook(obj):
    if "__date__" in obj:
        return date.fromisoformat(obj["__date__"])
    return obj


def dates_to_str(value):
    if isinstance(value, date):
        return {"__date__": value.isoformat()}
    if isinstance(value, dict):
        return {k: dates_to_str(v) for k, v in value.items()}
    if isinstance(value, list):
        return [dates_to_str(v) for v in value]
    return value


def str_to_dates(value):
    if isinstance(value, dict):
        if set(value) == {"__date__"}:
            return date.fromisoformat(value["__date__"])
        return {k: str_to_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [str_to_dates(v) for v in value]
    return value


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    try:
        json.dumps(data)
    except TypeError as e:
        print(f"TypeError: {e}")

    text1 = json.dumps(data, default=date_default, ensure_ascii=False)
    back1 = json.loads(text1, object_hook=date_hook)
    print(f"method 1 (default=): equal={back1 == data}, "
          f"date type={type(back1['created']).__name__}")

    text2 = json.dumps(dates_to_str(data), ensure_ascii=False)
    back2 = str_to_dates(json.loads(text2))
    print(f"method 2 (own funcs): equal={back2 == data}, "
          f"date type={type(back2['created']).__name__}")


if __name__ == "__main__":
    main()
