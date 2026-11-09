import sys
import math
from pathlib import Path
from datetime import datetime

NAME_SURNAME = "Oleksandra Romanich"
GROUP = "IT-32"

def format_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 1)
    return f"{s} {units[i]}"

def main():
    print(f"{NAME_SURNAME}, {GROUP}")

    args = sys.argv[1:]
    dry_run = False
    if "--dry-run" in args:
        dry_run = True
        args.remove("--dry-run")

    if len(args) != 1:
        print("usage: python3 task3.py [--dry-run] <dir>", file=sys.stderr)
        sys.exit(2)

    target_dir = Path(args[0])
    if not target_dir.is_dir():
        print(f"error: {target_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    files = [f for f in target_dir.iterdir() if f.is_file()]
    if not files:
        print("No files found.")
        sys.exit(0)

    file_info = []
    for f in files:
        stat = f.stat()
        mtime = datetime.fromtimestamp(stat.st_mtime)
        folder_name = mtime.strftime("%Y-%m")
        file_info.append((f, stat.st_size, mtime, folder_name))

    file_info.sort(key=lambda x: x[2])

    destinations = {}
    for f, size, mtime, folder_name in file_info:
        dest = target_dir / folder_name / f.name
        if dest.exists():
            print(f"error: {dest} already exists, nothing was moved", file=sys.stderr)
            sys.exit(1)
        destinations[f] = dest

    for f, size, mtime, folder_name in file_info:
        size_str = format_size(size)
        date_str = mtime.strftime("%d.%m.%Y %H:%M")
        print(f"{f.name:<20} {size_str:>8}  {date_str}  -> {folder_name}/")

    folders = set(info[3] for info in file_info)
    
    if dry_run:
        print(f"{len(file_info)} files, {len(folders)} folders (dry run, nothing moved)")
        sys.exit(0)

    for f, dest in destinations.items():
        dest.parent.mkdir(exist_ok=True)
        f.rename(dest)

    reports_dir = Path(__file__).parent / "reports"
    reports_dir.mkdir(exist_ok=True)
    report_name = f"organize_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    report_path = reports_dir / report_name
    
    with report_path.open("w", encoding="utf-8") as r:
        for f, size, mtime, folder_name in file_info:
            r.write(f"{f.name} -> {folder_name}/\n")

    print(f"{len(file_info)} files, {len(folders)} folders")
    print(f"report saved to: {report_path}")

if __name__ == "__main__":
    main()