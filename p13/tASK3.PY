import math
import sys
from datetime import datetime
from pathlib import Path

name, surname, group = "Yaroslav", "Korolchuk", "IT-31"
print(f"{name} {surname}, {group}")

args = sys.argv[1:]
dry = "--dry-run" in args
rest = [a for a in args if a != "--dry-run"]
if len(rest) != 1 or rest[0].startswith("--"):
    print("usage: python3 task3.py [--dry-run] <dir>")
    sys.exit(2)

folder = Path(rest[0])
if not folder.is_dir():
    print(f"error: {folder} is not a directory", file=sys.stderr)
    sys.exit(1)

files = [p for p in folder.iterdir() if p.is_file()]
if not files:
    print("no files")
    sys.exit(0)
files.sort(key=lambda p: p.stat().st_mtime)


def human(size):
    if size == 0:
        return "0 B"
    i = min(int(math.log(size, 1024)), 3)
    unit = ["B", "KB", "MB", "GB"][i]
    return f"{size / 1024 ** i:.1f} {unit}"


plan = []
lines = []
months = set()
for p in files:
    dt = datetime.fromtimestamp(p.stat().st_mtime)
    month = dt.strftime("%Y-%m")
    months.add(month)
    plan.append((p, folder / month / p.name))
    lines.append(f"{p.name:<20} {human(p.stat().st_size):>9}  {dt:%d.%m.%Y %H:%M}  -> {month}/")

for line in lines:
    print(line)

if dry:
    print(f"{len(files)} files, {len(months)} folders (dry run, nothing moved)")
    sys.exit(0)

for src, dst in plan:
    if dst.exists():
        print(f"error: {dst} already exists, nothing was moved", file=sys.stderr)
        sys.exit(1)

for src, dst in plan:
    dst.parent.mkdir(exist_ok=True)
    src.rename(dst)

print(f"{len(files)} files, {len(months)} folders")

now = datetime.now()
reports = Path(__file__).parent / "reports"
reports.mkdir(exist_ok=True)
report = reports / f"organize_{now:%Y%m%d_%H%M}.txt"
report.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"report saved to: reports/{report.name}")