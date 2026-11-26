
import argparse
import math
from pathlib import Path
from datetime import datetime

def format_size(size):
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(size)

    for unit in units:
        if value < 1024 or unit == "TB":
            return f"{value:.2f} {unit}"
        value /= 1024

def organize_files(source, dry_run=False):
    source = Path(source)

    if not source.exists() or not source.is_dir():
        print("Папку не знайдено!")
        return

    files = [p for p in source.iterdir() if p.is_file()]

    if not files:
        print("У папці немає файлів.")
        return

    print("Ira Leshchuk, IT-31")
    print("ОРГАНІЗАЦІЯ ФАЙЛІВ")
    print(f"Знайдено файлів: {len(files)}")

    planned = []
    conflicts = []

    for file in files:
        extension = file.suffix.lower().replace(".", "") or "без_розширення"
        target_folder = source / extension
        destination = target_folder / file.name

        if destination.exists():
            conflicts.append(destination)
        else:
            planned.append((file, target_folder, destination))

        size = file.stat().st_size
        modified = datetime.fromtimestamp(file.stat().st_mtime)

        print(f"\nФайл: {file.name}")
        print(f"Розмір: {format_size(size)}")
        print(f"Дата зміни: {modified:%d.%m.%Y %H:%M}")
        print(f"Розмір у KB: {math.ceil(size / 1024)}")

    if conflicts:
        print("\nВиявлено конфлікти:")
        for item in conflicts:
            print(item)
        print("Переміщення скасовано.")
        return

    if dry_run:
        print("\nТестовий режим. Файли не переміщено.")
        for file, folder, destination in planned:
            print(f"{file.name} -> {folder.name}/")
        return

    report = []

    for file, folder, destination in planned:
        folder.mkdir(exist_ok=True)
        file.rename(destination)
        report.append(f"{file.name} -> {destination}")

    report_path = source / "report.txt"
    report_path.write_text("\n".join(report), encoding="utf-8")

    print("\nПереміщення завершено!")
    print(f"Звіт збережено: {report_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", nargs="?", default="downloads_copy")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    organize_files(args.folder, args.dry_run)
