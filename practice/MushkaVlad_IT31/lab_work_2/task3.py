print("Mushka Vlad IT31")

from pathlib import Path
from datetime import datetime
import math
import sys

source = Path(__file__).parent / "task3_file"
reports = Path(__file__).parent / "reports"

if not source.is_dir():
    print("Помилка: папку task3_file не знайдено.", file=sys.stderr)
    sys.exit(1)

files = [item for item in source.rglob("*") if item.is_file()]

if len(files) < 15:
    print("Помилка: потрібно щонайменше 15 файлів.", file=sys.stderr)
    sys.exit(1)

categories = {
    "small": [],
    "medium": [],
    "large": []
}

for file in files:
    size = file.stat().st_size

    if size < 1024 * 1024:
        category = "small"
    elif size < 10 * 1024 * 1024:
        category = "medium"
    else:
        category = "large"

    modified = datetime.fromtimestamp(file.stat().st_mtime)
    categories[category].append((file, modified, size))

for category in categories:
    categories[category].sort(key=lambda item: item[1])

print(f"Знайдено файлів: {len(files)}")

for category, items in categories.items():
    print(f"\n{category}: {len(items)}")

    for file, modified, size in items:
        size_unit = math.log(size, 1024) if size > 0 else 0
        print(
            f"{file.name}: {size} байт, "
            f"{modified.strftime('%Y-%m-%d %H:%M')}, "
            f"log2={size_unit:.2f}"
        )

destinations = []

for category, items in categories.items():
    for file, _, _ in items:
        destination = source / category / file.relative_to(source)
        if destination.exists():
            print(f"Конфлікт: {destination}", file=sys.stderr)
            sys.exit(2)
        destinations.append((file, destination))

def organize(dry_run=False):
    for file, destination in destinations:
        if dry_run:
            print(f"[DRY-RUN] {file.relative_to(source)} -> {destination.relative_to(source)}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            file.rename(destination)

organize(dry_run=False)

reports.mkdir(exist_ok=True)
report_file = reports / f"organize_{datetime.now():%Y%m%d_%H%M}.txt"

with report_file.open("w", encoding="utf-8") as report:
    report.write(f"Знайдено файлів: {len(files)}\n")
    for category, items in categories.items():
        report.write(f"\n{category}: {len(items)}\n")
        for file, modified, size in items:
            report.write(
                f"{file.name}; {size}; "
                f"{modified.strftime('%Y-%m-%d %H:%M')}\n"
            )

print(f"\nЗвіт збережено: {report_file}")
