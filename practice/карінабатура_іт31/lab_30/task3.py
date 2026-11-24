from datetime import datetime
import math
import sys
from pathlib import Path

print("Батура Каріна Віталіївна, ІТ-31")

args = sys.argv[1:]
dry_run = False

if args and args[0] == "--dry-run":
    dry_run = True
    args = args[1:]

if len(args) != 1:
    print("usage: python3 task3.py [--dry-run] <dir>", file=sys.stderr)
    sys.exit(2)

target_dir = Path(args[0])

if not target_dir.exists() or not target_dir.is_dir():
    print(f"error: {target_dir} is not a directory", file=sys.stderr)
    sys.exit(1)

# Збираємо всі файли
files = [p for p in target_dir.iterdir() if p.is_file()]

if not files:
    print("No files found in the directory.")
    sys.exit(0)


# Функція для зручного вигляду розміру через math.log(size, 1024)
def human_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0.0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 1)
    return f"{s} {units[i]}"


# Готуємо список задач на переміщення: (file_path, mtime_dt, subfolder_name, dest_path)
file_plans = []
for file_path in files:
    mtime_timestamp = file_path.stat().st_mtime
    mtime_dt = datetime.fromtimestamp(mtime_timestamp)
    subfolder_name = mtime_dt.strftime("%Y-%m")
    dest_path = target_dir / subfolder_name / file_path.name
    file_plans.append((file_path, mtime_dt, subfolder_name, dest_path))

# Сортуємо від найстарішого до найновішого за часом зміни
file_plans.sort(key=lambda x: x[1])

# Перевірка конфліктів до переміщення будь-якого файлу
for file_path, mtime_dt, subfolder_name, dest_path in file_plans:
    if dest_path.exists():
        print(
            f"error: {dest_path.relative_to(target_dir.parent)} already exists, nothing was moved",
            file=sys.stderr,
        )
        sys.exit(1)

# Вивід плану
folder_count_set = set()
for file_path, mtime_dt, subfolder_name, dest_path in file_plans:
    sz_str = human_size(file_path.stat().st_size)
    dt_str = mtime_dt.strftime("%d.%m.%Y %H:%M")
    print(
        f"{file_path.name:<20} {sz_str:>8}  {dt_str}  -> {subfolder_name}/"
    )
    folder_count_set.add(subfolder_name)

if dry_run:
    print(f"{len(file_plans)} files, {len(folder_count_set)} folders (dry run, nothing moved)")
    sys.exit(0)

# Виконуємо переміщення
for file_path, mtime_dt, subfolder_name, dest_path in file_plans:
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.rename(dest_path)

# Зберігаємо звіт
reports_dir = Path("reports")
reports_dir.mkdir(exist_ok=True)
report_filename = reports_dir / f"organize_{datetime.now():%Y%m%d_%H%M}.txt"

report_content = f"Organization Report - {datetime.now():%Y-%m-%d %H:%M}\n"
report_content += f"Target directory: {target_dir.resolve()}\n"
report_content += f"Total files moved: {len(file_plans)}\n"
for file_path, mtime_dt, subfolder_name, dest_path in file_plans:
    report_content += f"- {file_path.name} -> {subfolder_name}/\n"

report_filename.write_text(report_content, encoding="utf-8")

print(
    f"{len(file_plans)} files, {len(folder_count_set)} folders\nreport saved to: {report_filename}"
)
sys.exit(0)