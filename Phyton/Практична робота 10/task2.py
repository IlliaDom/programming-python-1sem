from pathlib import Path
from datetime import datetime

PERSON = {
    "name": "Sasha",
    "surname": "Romanitch",
    "group": "IT-32",
}

SCRIPT_DIR = Path(__file__).resolve().parent
LOG_PATH = SCRIPT_DIR / "data" / "runs.log"


def count_runs(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open("r", encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())


def add_run(path: Path, number: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    who = f"{PERSON['name']} {PERSON['surname']}"
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{number};{stamp};{who}\n")


def show_history(path: Path, last: int = 3) -> None:
    total = count_runs(path)
    print(f"runs so far: {total}")

    if total == 0:
        return

    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    tail = lines[-last:]

    print("last runs:")
    for line in tail:
        num, stamp, who = line.split(";", 2)
        print(f"  # {num:<3} {stamp}  {who}")

    first = lines[0].split(";", 2)
    print(f"first run was at {first[1]}")


def main():
    created = not LOG_PATH.exists()

    number = count_runs(LOG_PATH) + 1
    add_run(LOG_PATH, number)

    who = f"{PERSON['name']} {PERSON['surname']}"
    print(f"Hello, {who}! This is run number {number}.")

    if created:
        print("(log file was just created)")

    show_history(LOG_PATH, last=3)


if __name__ == "__main__":
    main()