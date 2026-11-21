import sys
from pathlib import Path

import requests

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

BASE = Path(__file__).resolve().parent
DATA_FILE = BASE / "data" / "expenses.csv"

# Р”Р»СЏ Р·Р°РІРґР°РЅРЅСЏ 4 Р·РјС–РЅСЋР№С‚Рµ С†С– РєРѕРЅСЃС‚Р°РЅС‚Рё:
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
TIMEOUT = 10          # РґР»СЏ РїРµСЂРµРІС–СЂРєРё С‚Р°Р№РјР°СѓС‚Сѓ РїРѕСЃС‚Р°РІС‚Рµ 0.001


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def fetch_rate(code):
    """РџРѕРІРµСЂС‚Р°С” (РєСѓСЂСЃ, РґР°С‚Р°) РІР°Р»СЋС‚Рё Р·Р° РєРѕРґРѕРј С‡РµСЂРµР· РїР°СЂР°РјРµС‚СЂ valcode."""
    try:
        response = requests.get(URL, params={"valcode": code, "json": ""},
                                timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
    except requests.Timeout:
        fail(f"request for {code} timed out (timeout={TIMEOUT} s)")
    except requests.ConnectionError:
        fail("no connection to the server, check your internet")
    except requests.HTTPError as e:
        fail(f"server returned HTTP {e.response.status_code} for {code}")
    except requests.RequestException as e:
        fail(f"request failed: {e}")
    except ValueError:
        fail("response is not valid JSON")
    if not data:
        fail(f"no rate returned for {code}")
    return data[0]["rate"], data[0]["exchangedate"]


def read_total(path):
    total = 0.0
    with path.open(encoding="utf-8-sig") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                total += float(line.split(";")[2])
            except (IndexError, ValueError):
                print(f"warning: line {number} skipped: {line}",
                      file=sys.stderr)
    return total


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not DATA_FILE.is_file():
        fail(f"{DATA_FILE} not found")

    total = read_total(DATA_FILE)
    usd, rate_date = fetch_rate("USD")
    eur, _ = fetch_rate("EUR")

    print(f"rate date: {rate_date}")
    print(f"total: {total:.2f} UAH = {total / usd:.2f} USD "
          f"= {total / eur:.2f} EUR")


if __name__ == "__main__":
    main()
