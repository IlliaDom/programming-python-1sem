
from pathlib import Path
import katashynska_files as files


# Каталог із файлами програми
directory = Path(__file__).parent

print("Список файлів у каталозі:")
print(files.list_files(directory))

print("\nПошук файлів за підрядком 'katashynska':")
print(files.find_files(directory, "katashynska"))

# Створення файлу з особистими даними
file_path = directory / "Kateryna_Katashynska_IT-31.txt"

text = (
    "Ім'я: Kateryna\n"
    "Прізвище: Katashynska\n"
    "Група: IT-31\n"
)

files.create_file(file_path, text)

print("\nСтворено файл:", file_path.name)
print("Вміст створеного файлу:")
print(file_path.read_text(encoding="utf-8"))
