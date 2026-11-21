import math
import shutil
import sys
from datetime import datetime
from pathlib import Path

NAME = "Kateryna"
SURNAME = "Katashynska"
GROUP = "IT-31"

REPORTS_DIR = Path(__file__).resolve().parent / "reports"
UNITS = ["B", "KB", "MB", "GB"]


def human_size(size):
    if size == 0:
        return "0 B"
    idx = min(int(math.log(size, 1024)), len(UNITS) - 1)
    if idx == 0:
        return f"{size} B"
    value = size / 1024 ** idx
    return f"{value:.1f} {UNITS[idx]}"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if len(args) != 1:
        print("usage: python3 task3.py [--dry-run] <dir>")
        sys.exit(2)

    root = Path(args[0])
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        sys.exit(1)

    start = datetime.now()

    files = []
    for p in root.iterdir():
        if p.is_file():
            st = p.stat()
            files.append((datetime.fromtimestamp(st.st_mtime), p, st.st_size))
    if not files:
        print("no files to organize")
        sys.exit(0)
    files.sort(key=lambda item: item[0])

    plan = []
    for mtime, p, size in files:
        target_dir = root / mtime.strftime("%Y-%m")
        plan.append((p, target_dir, target_dir / p.name, mtime, size))

    lines = []
    for p, target_dir, target, mtime, size in plan:
        lines.append(f"{p.name:<20} {human_size(size):>9}  "
                     f"{mtime:%d.%m.%Y %H:%M}  -> {target_dir.name}/")
    for line in lines:
        print(line)
    folders = {item[1] for item in plan}
    summary = f"{len(plan)} files, {len(folders)} folders"

    if dry_run:
        print(summary + " (dry run, nothing moved)")
        sys.exit(0)

    for p, target_dir, target, mtime, size in plan:
        if target.exists():
            print(f"error: {target} already exists, nothing was moved",
                  file=sys.stderr)
            sys.exit(1)

    for p, target_dir, target, mtime, size in plan:
        target_dir.mkdir(exist_ok=True)
        shutil.move(str(p), str(target))
    print(summary)

    REPORTS_DIR.mkdir(exist_ok=True)
    report = REPORTS_DIR / f"organize_{start:%Y%m%d_%H%M}.txt"
    report.write_text(
        f"{NAME} {SURNAME}, {GROUP}\n"
        f"run: {start:%d.%m.%Y %H:%M}\n"
        f"directory: {root}\n"
        + "\n".join(lines) + "\n" + summary + "\n",
        encoding="utf-8",
    )
    print(f"report saved to: reports/{report.name}")


if __name__ == "__main__":
    main()
