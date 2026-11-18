#Батури Каріни ІТ-31 
import sys
from pathlib import Path
from datetime import datetime

DATA_DIR_NAME = "data"
REPORTS_DIR_NAME = "reports"
CSV_FILENAME = "expenses.csv"
REPORT_FILENAME = "expenses_report.txt"

def get_paths():
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir / DATA_DIR_NAME
    reports_dir = script_dir / REPORTS_DIR_NAME
    csv_path = data_dir / CSV_FILENAME
    report_path = reports_dir / REPORT_FILENAME
    return script_dir, data_dir, reports_dir, csv_path, report_path

def print_usage():
    print("usage: python3 task3.py add <date> <category> <amount> <note>")
    print("       python3 task3.py list")
    print("       python3 task3.py report")

def cmd_add(args):
    if len(args) < 4:
        print("error: add needs date, category, amount and note")
        print_usage()
        sys.exit(1)

    date = args[0]
    category = args[1]
    amount_str = args[2]

    try:
        amount = float(amount_str)
    except ValueError:
        print(f"error: invalid amount '{amount_str}', must be a number")
        sys.exit(1)

    note = " ".join(args[3:])

    _, data_dir, _, csv_path, _ = get_paths()
    data_dir.mkdir(exist_ok=True)

    file_exists = csv_path.exists()
    if not file_exists:
        csv_path.write_text("# date;category;amount;note\n", encoding="utf-8")

    with open(csv_path, "a", encoding="utf-8") as f:
        f.write(f"{date};{category};{amount:.2f};{note}\n")

    print(f"added: {date} {category} {amount:.2f} ({note})")

def read_expenses(csv_path: Path):
    if not csv_path.exists():
        return []
    records = []
    lines = csv_path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";", 3)
        if len(parts) == 4:
            date, category, amount_str, note = parts
            try:
                records.append({
                    "date": date,
                    "category": category,
                    "amount": float(amount_str),
                    "note": note
                })
            except ValueError:
                continue
    return records

def cmd_list():
    _, _, _, csv_path, _ = get_paths()
    records = read_expenses(csv_path)

    if not records:
        print("No expenses recorded yet.")
        return

    print(f"{'date':<12} {'category':<15} {'amount':>8}  note")
    total = 0.0
    for r in records:
        print(f"{r['date']:<12} {r['category']:<15} {r['amount']:>8.2f}  {r['note']}")
        total += r['amount']

    print(f"\n{len(records)} records, total {total:.2f}")

def cmd_report():
    _, data_dir, reports_dir, csv_path, report_path = get_paths()
    records = read_expenses(csv_path)

    if not records:
        print("error: no expense records found to generate report.")
        sys.exit(1)

    reports_dir.mkdir(exist_ok=True)

    dates = [r["date"] for r in records]
    min_date = min(dates)
    max_date = max(dates)
    total_records = len(records)

    # Групування по категоріях
    categories_data = {}
    for r in records:
        cat = r["category"]
        if cat not in categories_data:
            categories_data[cat] = {"count": 0, "total": 0.0}
        categories_data[cat]["count"] += 1
        categories_data[cat]["total"] += r["amount"]

    total_sum = sum(item["total"] for item in categories_data.values())

    # Сортування за сумою за спаданням
    sorted_cats = sorted(categories_data.items(), key=lambda x: x[1]["total"], reverse=True)

    # Витрати по днях для пошуку Топ-дня
    days_data = {}
    for r in records:
        d = r["date"]
        days_data[d] = days_data.get(d, 0.0) + r["amount"]
    top_day = max(days_data.items(), key=lambda x: x[1])

    # Найдорожча покупка
    most_expensive = max(records, key=lambda x: x["amount"])

    # Середні витрати на день (по кількості унікальних днів або всього періоду)
    unique_days = len(days_data)
    avg_per_day = total_sum / unique_days if unique_days > 0 else 0.0

    report_lines = []
    report_lines.append("Expenses report for Karina Batura (IT-31)")
    report_lines.append(f"Period: {min_date} .. {max_date}")
    report_lines.append(f"Records: {total_records}")
    report_lines.append("")
    report_lines.append(f"{'category':<12} {'count':>5}   {'total':>8}   {'share':>6}  chart")
    report_lines.append("-" * 52)

    for cat, data in sorted_cats:
        count = data["count"]
        cat_total = data["total"]
        share = (cat_total / total_sum) * 100 if total_sum > 0 else 0.0
        # Гістограма: один символ # на кожні 5%
        num_hashes = int(share // 5)
        chart = "#" * num_hashes
        report_lines.append(f"{cat:<12} {count:>5}   {cat_total:>8.2f}   {share:>5.1f}%  {chart}")

    report_lines.append("-" * 52)
    report_lines.append(f"{'total':<12} {total_records:>5}   {total_sum:>8.2f}   100.0%")
    report_lines.append("")
    report_lines.append(f"Top day: {top_day[0]} ({top_day[1]:.2f})")
    report_lines.append(f"Most expensive: {most_expensive['category']} {most_expensive['amount']:.2f} ({most_expensive['note']})")
    report_lines.append(f"Average per day: {avg_per_day:.2f}")

    report_content = "\n".join(report_lines) + "\n"
    report_path.write_text(report_content, encoding="utf-8")

    # Вивід на екран
    print(report_content, end="")
    print(f"report saved to: reports/{REPORT_FILENAME}")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add":
        cmd_add(args)
    elif command == "list":
        cmd_list()
    elif command == "report":
        cmd_report()
    else:
        print(f"error: unknown command {command}")
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()