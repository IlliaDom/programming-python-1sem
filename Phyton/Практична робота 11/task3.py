import math
import sys
from datetime import datetime
NAME = "Sasha"          
SURNAME = "Romanitch"   
GROUP = "IT-32"        
DATA_FILE = "data/expenses.csv"   
USAGE = (
    "usage: python3 task3.py add <date> <category> <amount> <note>\n"
    "       python3 task3.py list\n"
    "       python3 task3.py report"
)
def validate(fields):
    if len(fields) != 4:
        raise ValueError(f"expected 4 fields, got {len(fields)}")
    date, category, amount_text, note = (x.strip() for x in fields)
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"bad date '{date}'") from None
    if not category:
        raise ValueError("empty category")
    try:
        amount = float(amount_text)
    except ValueError:
        raise ValueError(f"bad amount '{amount_text}'") from None
    if not math.isfinite(amount):
        raise ValueError(f"bad amount '{amount_text}'")
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount:.2f}")
    return date, category, amount, note
def read_text():
    with open(DATA_FILE, encoding="utf-8") as f:
        return f.read()
def parse(text):
    records, skipped = [], []
    for number, line in enumerate(text.splitlines(), start=1):
        if number == 1:       
            continue
        if not line.strip():  
            continue
        try:
            records.append(validate(line.split(";")))
        except ValueError as e:
            skipped.append((number, str(e)))
    return records, skipped
def print_skipped(skipped):
    if skipped:
        print(f"skipped {len(skipped)} bad line(s):", file=sys.stderr)
        for number, reason in skipped:
            print(f"  line {number}: {reason}", file=sys.stderr)
def cmd_add(args):
    date, category, amount, note = args[0], args[1], args[2], " ".join(args[3:])
    try:
        record = validate([date, category, amount, note])
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        print("nothing was added", file=sys.stderr)
        return 1
    if ";" in note or "\n" in note:
        print("error: note must not contain ';' or line breaks", file=sys.stderr)
        print("nothing was added", file=sys.stderr)
        return 1
    text = read_text()
    prefix = "" if (not text or text.endswith("\n")) else "\n"
    d, c, a, n = record
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{prefix}{d};{c};{a:.2f};{n}\n")
    print(f"added: {d} {c} {a:.2f} {n}")
    return 0
def cmd_list():
    records, skipped = parse(read_text())
    print(f"{'date':<12}{'category':<12}{'amount':>10}  note")
    total = 0.0
    for date, category, amount, note in records:
        print(f"{date:<12}{category:<12}{amount:>10.2f}  {note}")
        total += amount
    print(f"{len(records)} records, total {total:.2f}")
    print_skipped(skipped)
    return 0
def cmd_report():
    records, skipped = parse(read_text())
    if not records:
        print("error: nothing to report, no valid records", file=sys.stderr)
        print_skipped(skipped)
        return 1
    by_category = {}
    for _, category, amount, _ in records:
        by_category[category] = by_category.get(category, 0.0) + amount
    total = sum(by_category.values())
    print(f"{'category':<14}{'sum':>10}{'share':>8}")
    for category, s in sorted(by_category.items(), key=lambda kv: -kv[1]):
        print(f"{category:<14}{s:>10.2f}{s / total * 100:>7.1f}%")
    biggest = max(records, key=lambda r: r[2])
    print(f"{len(records)} records, total {total:.2f}, average {total / len(records):.2f}")
    print(f"largest: {biggest[2]:.2f} ({biggest[1]}, {biggest[0]})")
    print_skipped(skipped)
    return 0
def main(argv):
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not argv:
        print(USAGE, file=sys.stderr)
        return 2
    command, args = argv[0], argv[1:]
    if command == "add":
        if len(args) < 4:
            print("error: add needs <date> <category> <amount> <note>", file=sys.stderr)
            print(USAGE, file=sys.stderr)
            return 2
    elif command in ("list", "report"):
        if args:
            print(f"error: {command} takes no arguments", file=sys.stderr)
            print(USAGE, file=sys.stderr)
            return 2
    else:
        print(f"error: unknown command {command}", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 2
    try:
        if command == "add":
            return cmd_add(args)
        if command == "list":
            return cmd_list()
        return cmd_report()
    except FileNotFoundError:
        print(f"error: {DATA_FILE} not found", file=sys.stderr)
    except IsADirectoryError:
        print(f"error: {DATA_FILE} is a directory, not a file", file=sys.stderr)
    except UnicodeDecodeError:
        print(f"error: {DATA_FILE} is not a UTF-8 text file", file=sys.stderr)
    except PermissionError:
        print(f"error: no permission to access {DATA_FILE}", file=sys.stderr)
    except OSError as e:
        print(f"error: cannot work with {DATA_FILE}: {e.strerror or e}", file=sys.stderr)
    return 1
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
 