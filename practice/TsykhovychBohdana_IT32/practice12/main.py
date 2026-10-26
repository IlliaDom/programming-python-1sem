import tsykhovych_files as files

directory = "."

print("Список файлів:")
print(files.list_files(directory))

print("Пошук файлів .py:")
print(files.find_files(directory, ".py"))

print("Створення файлу:")
files.create_file(
    "Bohdana_Tsykhovych_IT-23.txt",
    "Богдана Цихович, група ІТ-23"
)
print("Файл створено!")