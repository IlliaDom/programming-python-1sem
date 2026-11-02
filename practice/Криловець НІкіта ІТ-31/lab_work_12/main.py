import krilovets_files


directory = "."

print("Список файлів у поточній директорії:")
print(krilovets_files.list_files(directory))

substring = "py"

print(f"\nФайли, у назві яких є '{substring}':")
print(krilovets_files.find_files(directory, substring))

file_path = "student_info.txt"
text = """Ім'я: Нікіта
Прізвище: Криловець
Група: IT-31
"""

print("\nСтворення файлу:")
print(krilovets_files.create_file(file_path, text))
print(f"Файл '{file_path}' успішно створено.")