from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
import requests

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
STUDENT = "Мельник Діана, І-23"
CACHE = Path(__file__).with_name("cache") / "rates.json"
MAX_AGE = 60 * 60


def load_rates() -> tuple[list[dict], str]:
    try:
        cached = json.loads(CACHE.read_text(encoding="utf-8"))
        age = time.time() - float(cached["fetched_at"])
        if 0 <= age < MAX_AGE:
            return cached["rates"], f"cache (age {int(age)} s)"
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        pass

    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    rates = response.json()
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(
        json.dumps({"fetched_at": datetime.now(timezone.utc).timestamp(), "rates": rates},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return rates, "api (cache saved)"


def main() -> int:
    try:
        rates, source = load_rates()
    except requests.RequestException as exc:
        print(f"Помилка запиту НБУ: {exc}", file=sys.stderr)
        return 1
    except (OSError, ValueError, TypeError) as exc:
        print(f"Не вдалося прочитати або зберегти кеш: {exc}", file=sys.stderr)
        return 1
    print(STUDENT)
    print("source:", source)
    print("currencies:", len(rates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
