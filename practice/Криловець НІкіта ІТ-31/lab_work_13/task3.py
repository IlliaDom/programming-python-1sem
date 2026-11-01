import math
import sys
from pathlib import Path
from datetime import datetime

name = "Nikita"
surname = "Krilovets"
group = "IT-31"

print(f"{name} {surname}, {group}")

if len(sys.argv) == 2:
    dry_run = False
    directory = Path(sys.argv[1]).expanduser()

elif len(sys.argv) == 3 and sys.argv[1] == "--dry-run":
    dry_run = True
    directory = Path(sys.argv[2]).expanduser()

else:
    print("usage: python task3.py [--dry-run] <dir>", file=sys.stderr)
    sys.exit(2)

if not directory.exists() or not directory.is_dir():
    print(f"error: {directory} is not a directory", file=sys.stderr)
    sys.exit(1)

files = [file for file in directory.iterdir() if file.is_file()]

if not files:
    print("no files found")
    sys.exit(0)

file_data = []

for file in files:
    stat = file.stat()
    modified = datetime.fromtimestamp(stat.st_mtime)
    size = stat.st_size

    if size == 0:
        size_text = "0.0 B"
    else:
        units = ["B", "KB", "MB", "GB"]
        unit_index = min(int(math.log(size, 1024)), 3)
        size_value = size / (1024 ** unit_index)
        size_text = f"{size_value:.1f} {units[unit_index]}"

    month = modified.strftime("%Y-%m")
    destination = directory / month / file.name

    file_data.append((modified, file, destination, size_text))

file_data.sort(key=lambda item: item[0])

for modified, file, destination, size_text in file_data:
    print(
        f"{file.name:<20} {size_text:>9}  "
        f"{modified.strftime('%d.%m.%Y %H:%M')}  -> "
        f"{destination.parent.name}/"
    )

for modified, file, destination, size_text in file_data:
    if destination.exists():
        print(
            f"error: {destination} already exists, nothing was moved",
            file=sys.stderr
        )
        sys.exit(1)

folder_count = len(set(item[2].parent for item in file_data))

if dry_run:
    print(f"{len(files)} files, {folder_count} folders (dry run, nothing moved)")
    sys.exit(0)

try:
    for modified, file, destination, size_text in file_data:
        destination.parent.mkdir(parents=True, exist_ok=True)
        file.rename(destination)

    reports_dir = Path(__file__).parent / "reports"
    reports_dir.mkdir(exist_ok=True)

    now = datetime.now()
    report_path = reports_dir / f"organize_{now.strftime('%Y%m%d_%H%M')}.txt"

    report_lines = [
        f"{name} {surname}, {group}",
        f"Date: {now.strftime('%d.%m.%Y %H:%M')}",
        ""
    ]

    for modified, file, destination, size_text in file_data:
        report_lines.append(
            f"{file.name} -> {destination.parent.name}/"
        )

    report_lines.append(
        f"\n{len(files)} files, {folder_count} folders"
    )

    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"{len(files)} files, {folder_count} folders")
    print(f"report saved to: {report_path.relative_to(Path(__file__).parent)}")

except OSError as error:
    print(f"error: {error}", file=sys.stderr)
    sys.exit(1)