import mischuk_files

# Каталог, з яким працюємо (поточна папка; можна вказати інший шлях)
directory = "."

# 1. Список файлів
files = mischuk_files.list_files(directory)
print("Файли в каталозі:", files)

# 2. Пошук файлів за підрядком
found = mischuk_files.find_files(directory, "files")
print("Знайдено за підрядком 'files':", found)

# 3. Створення файлу з моїми даними
path = mischuk_files.create_file("student.txt", "Міщук Назарій, група IT-32")
print("Створено файл:", path)
