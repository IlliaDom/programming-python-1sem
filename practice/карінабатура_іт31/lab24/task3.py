#Батура Каріна, ІТ-31
import sys
from datetime import datetime
from pathlib import Path

def print_header():
    print("Karina Batura, IT-31")

def get_paths():
    script_dir = Path(__file__).resolve().parent
    csv_path = script_dir / "data" / "expenses.csv"
    report_path = script_dir / "reports" / "expenses_report.txt"
    return csv_path, report_path

def parse_record(line_num: int, line: str):
    parts = line.split(";", 3)
    if len(parts) != 4:
        raise ValueError(f"line {line_num}: expected 4 fields, got {len(parts)}")
    
    date_str, category, amount_str, note = [p.strip() for p in parts]
    
    # Перевірка дати
    date_parts = date_str.split("-")
    if len(date_parts) != 3:
        raise ValueError(f"line {line_num}: bad date format '{date_str}'")
    
    try:
        y, m, d = map(int, date_parts)
        if m == 13 and d == 14:  
            raise ValueError(f"line {line_num}: bad date '{date_str}'")
        datetime(y, m, d)
    except ValueError as e:
        if "bad date" in str(e):
            raise
        raise ValueError(f"line {line_num}: bad date '{date_str}'") from e

    try:
        amount = float(amount_str)
    except ValueError as e:
        raise ValueError(f"line {line_num}: bad amount {amount_str!r}") from e

    if amount <= 0:
        raise ValueError(f"line {line_num}: amount must be positive, got {amount:.2f}")

    return {"date": date_str, "category": category, "amount": amount, "note": note}

def read_expenses(csv_path: Path):
    if not csv_path.exists():
        print(f"error: data/expenses.csv not found", file=sys.stderr)
        sys.exit(1)
    if csv_path.is_dir():
        print(f"error: data/expenses.csv is a directory, not a file", file=sys.stderr)
        sys.exit(1)
    
    try:
        text = csv_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"error: expenses.csv is not a valid UTF-8 file", file=sys.stderr)
        sys.exit(1)

    records = []
    skipped = []
    for idx, line in enumerate(text.splitlines(), start=1):
        line_str = line.strip()
        if not line_str or line_str.startswith("#"):
            continue
        try:
            records.append(parse_record(idx, line_str))
        except ValueError as e:
            skipped.append(str(e))
    return records, skipped

def main():
    args = sys.argv[1:]
    if not args:
        print("usage: python3 task3.py add <date> <category> <amount> <note>\n       python3 task3.py list\n       python3 task3.py report", file=sys.stderr)
        sys.exit(2)

    cmd = args[0]
    csv_path, report_path = get_paths()

    if cmd == "add":
        if len(args) < 5:
            print("error: add needs date, category, amount and note", file=sys.stderr)
            sys.exit(1)
        raw_line = f"{args[1]};{args[2]};{args[3]};{' '.join(args[4:])}"
        try:
            parse_record(0, raw_line)
        except ValueError as e:
            err_msg = str(e).split(": ", 1)[1] if ": " in str(e) else str(e)
            print(f"error: {err_msg}", file=sys.stderr)
            print("nothing was added", file=sys.stderr)
            sys.exit(1)

        csv_path.parent.mkdir(exist_ok=True)
        if not csv_path.exists():
            csv_path.write_text("# date;category;amount;note\n", encoding="utf-8")
        with open(csv_path, "a", encoding="utf-8") as f:
            f.write(raw_line + "\n")
        print(f"added: {args[1]} {args[2]} {float(args[3]):.2f} ({' '.join(args[4:])})")
        sys.exit(0)

    elif cmd == "list":
        print_header()
        records, skipped = read_expenses(csv_path)
        if not records and not skipped:
            print("error: nothing to report, no valid records", file=sys.stderr)
            sys.exit(1)

        if records:
            print(f"{'date':<12} {'category':<15} {'amount':>8}  note")
            total = 0.0
            for r in records:
                print(f"{r['date']:<12} {r['category']:<15} {r['amount']:>8.2f}  {r['note']}")
                total += r['amount']
            print(f"{len(records)} records, total {total:.2f}")

        if skipped:
            print(f"skipped {len(skipped)} bad line(s):", file=sys.stderr)
            for err in skipped:
                print(f"  {err}", file=sys.stderr)
        sys.exit(0)

    elif cmd == "report":
        print_header()
        records, skipped = read_expenses(csv_path)
        if not records:
            print("error: nothing to report, no valid records", file=sys.stderr)
            sys.exit(1)

        report_path.parent.mkdir(exist_ok=True)
        min_date = min(r["date"] for r in records)
        max_date = max(r["date"] for r in records)
        
        categories = {}
        for r in records:
            cat = r["category"]
            categories.setdefault(cat, {"count": 0, "total": 0.0})
            categories[cat]["count"] += 1
            categories[cat]["total"] += r["amount"]

        total_sum = sum(v["total"] for v in categories.values())
        sorted_cats = sorted(categories.items(), key=lambda x: x[1]["total"], reverse=True)

        days_data = {}
        for r in records:
            d = r["date"]
            days_data[d] = days_data.get(d, 0.0) + r["amount"]
        top_day = max(days_data.items(), key=lambda x: x[1])
        most_exp = max(records, key=lambda x: x["amount"])
        avg_day = total_sum / len(days_data) if days_data else 0.0

        report_lines = [
            "Expenses report for Karina Batura (IT-31)",
            f"Period: {min_date} .. {max_date}",
            f"Records: {len(records)}",
            "",
            f"{'category':<12} {'count':>5}   {'total':>8}   {'share':>6}  chart",
            "-" * 52
        ]

        for cat, data in sorted_cats:
            share = (data["total"] / total_sum) * 100 if total_sum > 0 else 0.0
            chart = "#" * int(share // 5)
            report_lines.append(f"{cat:<12} {data['count']:>5}   {data['total']:>8.2f}   {share:>5.1f}%  {chart}")

        report_lines.extend([
            "-" * 52,
            f"{'total':<12} {len(records):>5}   {total_sum:>8.2f}   100.0%",
            "",
            f"Top day: {top_day[0]} ({top_day[1]:.2f})",
            f"Most expensive: {most_exp['category']} {most_exp['amount']:.2f} ({most_exp['note']})",
            f"Average per day: {avg_day:.2f}"
        ])

        report_content = "\n".join(report_lines) + "\n"
        report_path.write_text(report_content, encoding="utf-8")

        print(report_content, end="")
        print(f"report saved to: reports/expenses_report.txt")

        if skipped:
            print(f"skipped {len(skipped)} bad line(s):", file=sys.stderr)
            for err in skipped:
                print(f"  {err}", file=sys.stderr)
        sys.exit(0)

    else:
        print(f"error: unknown command {cmd}", file=sys.stderr)
        print("usage: python3 task3.py add <date> <category> <amount> <note>\n       python3 task3.py list\n       python3 task3.py report", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()