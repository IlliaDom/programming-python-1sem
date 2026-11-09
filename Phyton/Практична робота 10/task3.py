import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime
PERSON = {
    "name": "Sasha",
    "surname": "Romanitch",
    "group": "IT-32",
}
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
REPORTS_DIR = SCRIPT_DIR / "reports"
CSV_PATH = DATA_DIR / "expenses.csv"
REPORT_PATH = REPORTS_DIR / "expenses_report.txt"
HEADER = "# date;category;amount;note"
USAGE = (
    "usage: python3 task3.py add <date> <category> <amount> <note>\n"
    "       python3 task3.py list\n"
    "       python3 task3.py report"
)

def ensure_file() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not CSV_PATH.exists():
        CSV_PATH.write_text(HEADER + "\n", encoding="utf-8")
def read_expenses() -> list[dict]:
    ensure_file()
    rows = []
    with CSV_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(";")
            if len(parts) < 4:
                continue
            date, category, amount, note = parts[0], parts[1], parts[2], ";".join(parts[3:])
            try:
                amount = float(amount)
            except ValueError:
                continue
            rows.append({
                "date": date,
                "category": category,
                "amount": amount,
                "note": note,
            })
    return rows
def cmd_add(args: list[str]) -> None:
    if len(args) < 4:
        print("error: add needs date, category, amount and note")
        print(USAGE)
        return
    date, category, amount_raw = args[0], args[1], args[2]
    note = " ".join(args[3:])
    try:
        amount = float(amount_raw)
    except ValueError:
        print(f"error: amount must be a number, got {amount_raw!r}")
        print(USAGE)
        return
    ensure_file()
    with CSV_PATH.open("a", encoding="utf-8") as f:
        f.write(f"{date};{category};{amount:.2f};{note}\n")
    print(f"added: {date} {category} {amount:.2f} ({note})")
def cmd_list(_args: list[str]) -> None:
    rows = read_expenses()
    if not rows:
        print("(no expenses yet)")
        return
    print(f"{'date':<12}{'category':<14}{'amount':>8}  note")
    total = 0.0
    for r in rows:
        print(f"{r['date']:<12}{r['category']:<14}{r['amount']:>8.2f}  {r['note']}")
        total += r["amount"]
    print(f"{len(rows)} records, total {total:.2f}")
def cmd_report(_args: list[str]) -> None:
    rows = read_expenses()
    if not rows:
        print("error: no data to build report")
        return
    dates = sorted(r["date"] for r in rows)
    first_date, last_date = dates[0], dates[-1]
    total = sum(r["amount"] for r in rows)
    by_cat = defaultdict(lambda: [0, 0.0])  
    for r in rows:
        by_cat[r["category"]][0] += 1
        by_cat[r["category"]][1] += r["amount"]
    categories = sorted(by_cat.items(), key=lambda kv: kv[1][1], reverse=True)
    by_day = defaultdict(float)
    for r in rows:
        by_day[r["date"]] += r["amount"]
    top_day, top_day_sum = max(by_day.items(), key=lambda kv: kv[1])

    most = max(rows, key=lambda r: r["amount"])
    days_count = len(by_day)
    avg_per_day = total / days_count if days_count else 0.0
    who = f"{PERSON['name']} {PERSON['surname']} ({PERSON['group']})"
    lines = []
    lines.append(f"Expenses report for {who}")
    lines.append(f"Period: {first_date} .. {last_date}")
    lines.append(f"Records: {len(rows)}")
    lines.append("")
    lines.append(f"{'category':<12}{'count':>6}{'total':>11}{'share':>9}  chart")
    lines.append("-" * 52)

    for cat, (cnt, sm) in categories:
        share = sm / total * 100 if total else 0
        bars = "#" * int(share / 5)
        lines.append(
            f"{cat:<12}{cnt:>6}{sm:>11.2f}{share:>8.1f}%  {bars}"
        )
    lines.append("-" * 52)
    lines.append(f"{'total':<12}{len(rows):>6}{total:>11.2f}{100.0:>8.1f}%")
    lines.append("")
    lines.append(f"Top day: {top_day} ({top_day_sum:.2f})")
    lines.append(f"Most expensive: {most['category']} {most['amount']:.2f} ({most['note']})")
    lines.append(f"Average per day: {avg_per_day:.2f}")

    report_text = "\n".join(lines)
    print(report_text)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text + "\n", encoding="utf-8")
    print()
    print(f"report saved to: {REPORT_PATH.relative_to(SCRIPT_DIR)}")

def main(argv: list[str]) -> None:
    if not argv:
        print(USAGE)
        return

    command, *rest = argv
    if command == "add":
        cmd_add(rest)
    elif command == "list":
        cmd_list(rest)
    elif command == "report":
        cmd_report(rest)
    else:
        print(f"error: unknown command {command}")
        print(USAGE)


if __name__ == "__main__":
    main(sys.argv[1:])