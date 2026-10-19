from pathlib import Path
from tarasiuk_files import list_files, find_files, create_file

directory = Path(__file__).parent

print("Список файлів:")
print(list_files(directory))

print("\nФайли з підрядком 'task':")
print(find_files(directory, "task"))

file_path = directory / "tarasiuk_info.txt"
create_file(
    file_path,
    "Ім'я: Nazar\nПрізвище: Tarasiuk\nГрупа: I-23"
)

print("\nСтворено файл:", file_path.name)