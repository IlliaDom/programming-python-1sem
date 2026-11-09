"""Main script to test batura_files module."""

import logging
from pathlib import Path
import batura_files

def main() -> int:
    # Налаштування простого виводу
    logging.basicConfig(level=logging.INFO, format="%(levelname)-7s %(message)s")
    
    current_dir = Path(__file__).resolve().parent
    
    print("1. Список файлів у поточній директорії")
    files = batura_files.list_files(current_dir)
    for filename in files:
        print(f" - {filename}")

    print("\n2. Створення файлу з особистими даними")
    new_file_path = current_dir / "student_info.txt"
    content = "Прізвище: Батура\nІм'я: Каріна\nГрупа: ІТ-31\n"
    
    batura_files.create_file(new_file_path, content)
    print(f"Файл успішно створено: {new_file_path.name}")
    print("Вміст створеного файлу:")
    print("-" * 30)
    print(new_file_path.read_text(encoding="utf-8"), end="")
    print("-" * 30)

    return 0


if __name__ == "__main__":
    main()