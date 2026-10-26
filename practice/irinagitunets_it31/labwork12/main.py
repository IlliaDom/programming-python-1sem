import gitunets_files
import os

directory = os.path.expanduser("~/Desktop")

print("Усі файли:", gitunets_files.list_files(directory))

print("Знайдені файли:", gitunets_files.find_files(directory, "python"))

gitunets_files.create_file(
    "student.txt",
    "Ім'я: Ірина\nПрізвище: Гітунець\nГрупа: IT-31"
)

print("Файл student.txt створено!")