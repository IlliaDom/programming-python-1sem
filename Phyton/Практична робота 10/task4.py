from pathlib import Path
from datetime import datetime
import shutil
SCRIPT_DIR = Path(__file__).resolve().parent
BACKUPS = SCRIPT_DIR / "backups"
SOURCES = [
    SCRIPT_DIR / "data" / "profile.txt",
    SCRIPT_DIR / "data" / "runs.log",
    SCRIPT_DIR / "data" / "expenses.csv",
]
def copy_binary(src: Path, dst: Path) -> int:
    with src.open("rb") as fin, dst.open("wb") as fout:
        data = fin.read()
        fout.write(data)
    return len(data)
def backup(src: Path, stamp: str) -> Path | None:
    if not src.exists():
        print(f"skip (no file): {src.relative_to(SCRIPT_DIR)}")
        return None
    target_dir = BACKUPS / stamp
    target_dir.mkdir(parents=True, exist_ok=True)
    dst = target_dir / src.name

    size = copy_binary(src, dst)
    print(f"copied {src.relative_to(SCRIPT_DIR)} -> "
          f"{dst.relative_to(SCRIPT_DIR)} ({size} bytes)")
    return dst
def main():
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    BACKUPS.mkdir(exist_ok=True)

    print(f"backup folder: {stamp}")
    for src in SOURCES:
        backup(src, stamp)
    print()
    print("backup tree:")
    for path in sorted((BACKUPS / stamp).iterdir()):
        print(f"  {path.name}  ({path.stat().st_size} bytes)")
if __name__ == "__main__":
    main()