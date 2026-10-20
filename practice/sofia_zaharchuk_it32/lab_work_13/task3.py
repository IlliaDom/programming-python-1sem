import math
import sys
from datetime import datetime
from pathlib import Path

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"
UNITS = ["B", "KB", "MB", "GB"]


def human(size: int) -> str:
    i = min(int(math.log(size, 1024)), len(UNITS) - 1) if size > 0 else 0
    if i == 0:
        return f"{size} B"
    return f"{size / 1024 ** i:.1f} {UNITS[i]}"


def main() -> None:
    print(f"{NAME} {SURNAME}, {GROUP}")
    args = sys.argv[1:]
    dry = "--dry-run" in args
    rest = [a for a in args if a != "--dry-run"]
    if len(rest) != 1 or len(args) - len(rest) > 1:
        print("usage: python3 task3.py [--dry-run] <dir>", file=sys.stderr)
        sys.exit(2)

    root = Path(rest[0])
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        sys.exit(1)

    items = []
    for p in root.iterdir():
        if p.is_file():
            st = p.stat()
            items.append((datetime.fromtimestamp(st.st_mtime), st.st_size, p))
    if not items:
        print("no files to organize")
        return
    items.sort(key=lambda x: x[0])

    plan = []
    lines = []
    for mtime, size, p in items:
        folder = mtime.strftime("%Y-%m")
        plan.append((p, root / folder / p.name))
        lines.append(f"{p.name:<20}{human(size):>9}  {mtime:%d.%m.%Y %H:%M}  -> {folder}/")
    for line in lines:
        print(line)
    folders = {dst.parent for _, dst in plan}
    summary = f"{len(plan)} files, {len(folders)} folders"

    if dry:
        print(summary + " (dry run, nothing moved)")
        return

    for _, dst in plan:  # спершу перевірка всіх
        if dst.exists():
            print(f"error: {dst} already exists, nothing was moved", file=sys.stderr)
            sys.exit(1)

    for src, dst in plan:
        dst.parent.mkdir(exist_ok=True)
        src.rename(dst)
    print(summary)

    now = datetime.now()
    rep_dir = Path(__file__).resolve().parent / "reports"
    rep_dir.mkdir(exist_ok=True)
    rep = rep_dir / f"organize_{now:%Y%m%d_%H%M}.txt"
    rep.write_text("\n".join(lines) + f"\n{summary}\n", encoding="utf-8")
    print(f"report saved to: reports/{rep.name}")


main()
