import sys 
import math
import shutil
from pathlib import Path
from datetime import datetime
from operator import itemgetter

print("Студент: Богдана Цихович, група: ІТ-32")

args = sys.argv[1:]
dry_run = "--dry-run" in args
if dry_run:
    args.remove("--dry-run")

if len(args) != 1:
    print("Використання: python3 task3.py [--dry-run] <dir>")
    sys.exit(2)

dir_path = Path(args[0])

if not dir_path.is_dir():
    print("Вказаний каталог не існує")
    sys.exit(1)

files = [f for f in dir_path.iterdir() if f.is_file()]

if not files:
    print("У вказаному каталозі немає файлів")
    sys.exit(0)

plan = []

try:
    for file in files:
        info = file.stat()
        mtime = datetime.fromtimestamp(info.st_mtime)
        subdir_name = mtime.strftime("%Y-%m")
        target = dir_path / subdir_name / file.name
        plan.append((file, target, info.st_size, mtime))

    plan.sort(key=itemgetter(3))

    for file, target, size, mtime in plan:
        if target.exists():
            print(f"Файл {target} вже існує. Переміщення скасовано.", file=sys.stderr)
            sys.exit(1)

    for file, target, size, mtime in plan:
        size_unit = ["B", "KB", "MB", "GB"]
        size_index = min(int(math.log(size, 1024)), len(size_unit) - 1) if size > 0 else 0
        size_value = size / (1024 ** size_index)
        size_str = f"{size_value:.2f} {size_unit[size_index]}"

        print(f"Файл: {file.name}, Розмір: {size_str}, Змінено: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
        
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(target))

    if not dry_run:
        report_dir = Path("reports")
        report_dir.mkdir(exist_ok=True)
        report_file = report_dir / f"organize_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            for file, target, size, mtime in plan:
                f.write(
                    f"{file.name} -> {target}, "
                    f"розмір: {size} B, "
                    f"змінено: {mtime:%d.%m.%Y %H:%M}\n"
                )

    folders = len(set(target.parent for _, target, _, _ in plan))

    print(f"Кількість файлів: {len(plan)}")
    print(f"Кількість папок: {folders}")

    if dry_run:
        print("Dry run: файли не переміщено")
    else:
        print(f"Звіт збережено: {report_file}")

except Exception as e:
    print(f"Помилка: {e}", file=sys.stderr)
    sys.exit(1) 
