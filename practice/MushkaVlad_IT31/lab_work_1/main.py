print("Mushka Vlad IT31")

from pathlib import Path
import mushka_files

directory = Path.home() / "Documents" / "python-practice-mushka"

print("Список файлів:")
print([file.name for file in mushka_files.list_files(directory)])

print("\nФайли, у назві яких є 'task':")
print([file.name for file in mushka_files.find_files(directory, "task")])

new_file = directory / "mushka_info.txt"
text = "Ім'я: Влад\nПрізвище: Мушка\nГрупа: IT31"

mushka_files.create_file(new_file, text)
print("\nСтворено файл:", new_file)
