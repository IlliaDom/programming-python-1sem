#Батури Каріни ІТ-31 
from pathlib import Path
from datetime import datetime

def count_runs(path: Path) -> int:
    if not path.exists():
        return 0
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return len(lines)

def add_run(path: Path, number: int) -> None:
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"{number};{stamp};Karina Batura\n"
    with open(path, "a", encoding="utf-8") as f:
        f.write(record)

def show_history(path: Path, last: int = 3) -> None:
    if not path.exists():
        print("runs so far: 0")
        return

    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    total_runs = len(lines)
    print(f"runs so far: {total_runs}")

    if total_runs == 0:
        return

    print("last runs:")
    recent_lines = lines[-last:]
    for line in recent_lines:
        parts = line.split(";")
        if len(parts) == 3:
            num, dt, name = parts
            print(f"  # {num:<2}  {dt}  {name}")

    # Час найпершого запуску
    first_parts = lines[0].split(";")
    if len(first_parts) >= 2:
        print(f"first run was at {first_parts[1]}")

def main():
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir / "data"
    data_dir.mkdir(exist_ok=True)
    log_path = data_dir / "runs.log"

    previous_count = count_runs(log_path)
    current_run_number = previous_count + 1

    is_first_run = (previous_count == 0)

    add_run(log_path, current_run_number)

    if is_first_run:
        print("[Увага] Файл runs.log щойно створено вперше!")

    print("Hello, Karina Batura!")
    print(f"This is run number {current_run_number}.")

    show_history(log_path, last=3)

if __name__ == "__main__":
    main()