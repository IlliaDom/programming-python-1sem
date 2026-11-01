import sys
import math
from pathlib import Path
from datetime import datetime

# Personal information
print("Sofia Stotska, IT-31")

# Arguments
args = sys.argv[1:]
dry_run = False

if args and args[0] == "--dry-run":
    dry_run = True
    args = args[1:]

if len(args) != 1:
    print("usage: python3 task3.py [--dry-run] <dir>")
    sys.exit(2)

directory = Path(args[0]).expanduser()

if not directory.exists() or not directory.is_dir():
    print(f"error: {directory} is not a directory", file=sys.stderr)
    sys.exit(1)

# Find files
files = [path for path in directory.iterdir() if path.is_file()]

if not files:
    print("No files found")
    sys.exit(0)

# File information
file_data = []

for path in files:
    stat = path.stat()
    modified = datetime.fromtimestamp(stat.st_mtime)
    size = stat.st_size

    if size == 0:
        size_text = "0 B"
    else:
        units = ["B", "KB", "MB", "GB"]
        unit_index = min(math.floor(math.log(size, 1024)), 3)
        size_value = size / (1024 ** unit_index)
        size_text = f"{size_value:.1f} {units[unit_index]}"

    month_folder = modified.strftime("%Y-%m")

    file_data.append({
        "path": path,
        "modified": modified,
        "size": size_text,
        "month": month_folder
    })

# Sort by modification date
file_data.sort(key=lambda item: item["modified"])

# Check all destination files before moving
for item in file_data:
    destination = directory / item["month"] / item["path"].name

    if destination.exists():
        print(
            f"error: {destination} already exists, nothing was moved",
            file=sys.stderr
        )
        sys.exit(1)

# Display plan
for item in file_data:
    print(
        f"{item['path'].name:<20} "
        f"{item['size']:>9}  "
        f"{item['modified'].strftime('%d.%m.%Y %H:%M')}  "
        f"-> {item['month']}/"
    )

folders = len(set(item["month"] for item in file_data))

if dry_run:
    print(f"{len(files)} files, {folders} folders (dry run, nothing moved)")
    sys.exit(0)

# Move files
for item in file_data:
    destination_folder = directory / item["month"]
    destination_folder.mkdir(exist_ok=True)
    item["path"].rename(destination_folder / item["path"].name)

# Create report
script_directory = Path(__file__).parent
reports_directory = script_directory / "reports"
reports_directory.mkdir(exist_ok=True)

now = datetime.now()
report_name = now.strftime("organize_%Y%m%d_%H%M.txt")
report_path = reports_directory / report_name

with report_path.open("w", encoding="utf-8") as report:
    report.write("File organization report\n")
    report.write(f"Date: {now}\n")
    report.write(f"Directory: {directory}\n")
    report.write(f"Files moved: {len(files)}\n\n")

    for item in file_data:
        report.write(
            f"{item['path'].name} -> {item['month']}/\n"
        )

print(f"{len(files)} files, {folders} folders")
print(f"report saved to: reports/{report_name}")

sys.exit(0)