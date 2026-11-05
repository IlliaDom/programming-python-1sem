import sys
import math
from pathlib import Path
from datetime import datetime
import shutil


def human_size(size):
    if size == 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB", "TB"]
    index = min(int(math.log(size, 1024)), len(units) - 1)
    value = size / (1024 ** index)

    return f"{value:.2f} {units[index]}"


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [arg for arg in args if arg != "--dry-run"]

    if len(args) != 1:
        print("Використання: py task3.py [--dry-run] <папка>")
        return 2

    folder = Path(args[0])

    if not folder.is_dir():
        print("Помилка: папку не знайдено.")
        return 1

    files = [p for p in folder.iterdir() if p.is_file()]

    if not files:
        print("Папка порожня.")
        return 0

    plan = []

    for file in files:
        info = file.stat()
        modified = datetime.fromtimestamp(info.st_mtime)
        month = modified.strftime("%Y-%m")
        destination = folder / month / file.name

        plan.append((file, destination, info.st_size, modified))

    plan.sort(key=lambda item: item[3])

    print("Diana Melnyk, група I-23")
    print("\nПлан сортування файлів:")

    for source, destination, size, modified in plan:
        print(
            f"{source.name} | {human_size(size)} | "
            f"{modified:%d.%m.%Y} -> {destination.parent.name}/"
        )

    if dry_run:
        print("\nРежим попереднього перегляду. Файли не переміщено.")
        return 0

    conflicts = [
        destination
        for _, destination, _, _ in plan
        if destination.exists()
    ]

    if conflicts:
        print("\nКонфлікт! Такі файли вже існують:")
        for item in conflicts:
            print(item)
        print("Жоден файл не переміщено.")
        return 1

    for source, destination, _, _ in plan:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(destination))

    report_dir = Path(__file__).parent / "reports"
    report_dir.mkdir(exist_ok=True)

    report_name = datetime.now().strftime("organize_%Y%m%d_%H%M.txt")
    report_path = report_dir / report_name

    with report_path.open("w", encoding="utf-8") as report:
        report.write("Diana Melnyk, група I-23\n")
        report.write("Звіт сортування файлів\n\n")

        for source, destination, size, modified in plan:
            report.write(
                f"{source.name} | {human_size(size)} | "
                f"{modified:%d.%m.%Y} -> {destination}\n"
            )

    print(f"\nПереміщено файлів: {len(plan)}")
    print(f"Звіт збережено: {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())