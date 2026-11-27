import math
import sys
from datetime import datetime
from pathlib import Path

NAME = "Anastasia"
SURNAME = "Zakharchuk"
GROUP = "IT-32"

BASE = Path(__file__).resolve().parent
REPORTS_DIR = BASE / "reports"
USAGE = "usage: python3 task3.py [--dry-run] <dir>"


def format_size(size):
    if size == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB"]
    power = min(int(math.log(size, 1024)), 3)
    return f"{size / 1024 ** power:.1f} {units[power]}"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    args = sys.argv[1:]
    dry_run = False
    if args and args[0] == "--dry-run":
        dry_run = True
        args = args[1:]
    if len(args) != 1:
        print(USAGE, file=sys.stderr)
        sys.exit(2)

    folder = Path(args[0])
    if not folder.is_dir():
        print(f"error: {folder} is not a directory", file=sys.stderr)
        sys.exit(1)

    files = []
    for item in folder.iterdir():
        if item.is_file():
            modified = datetime.fromtimestamp(item.stat().st_mtime)
            files.append((modified, item))
    files.sort()

    if not files:
        print("no files to organize")
        return

    # перевірка конфліктів до переміщення першого файлу
    for modified, item in files:
        target = folder / f"{modified:%Y-%m}" / item.name
        if target.exists():
            print(f"error: {target} already exists, nothing was moved",
                  file=sys.stderr)
            sys.exit(1)

    lines = []
    months = set()
    for modified, item in files:
        month = f"{modified:%Y-%m}"
        months.add(month)
        size_text = format_size(item.stat().st_size)
        lines.append(f"{item.name:<18}{size_text:>10}  "
                     f"{modified:%d.%m.%Y %H:%M}  -> {month}/")

    summary = f"{len(files)} files, {len(months)} folders"

    for line in lines:
        print(line)

    if dry_run:
        print(summary + " (dry run, nothing moved)")
        return

    print(summary)

    for modified, item in files:
        target_dir = folder / f"{modified:%Y-%m}"
        target_dir.mkdir(exist_ok=True)
        item.rename(target_dir / item.name)

    now = datetime.now()
    REPORTS_DIR.mkdir(exist_ok=True)
    report = REPORTS_DIR / f"organize_{now:%Y%m%d_%H%M}.txt"
    report.write_text("\n".join(lines + [summary]) + "\n", encoding="utf-8")
    print("report saved to:", report.relative_to(BASE))


main()