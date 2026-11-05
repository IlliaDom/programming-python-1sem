import os
import melnyk_files


directory = os.path.expanduser("~/Desktop")

print("Файли на робочому столі:")
print(melnyk_files.list_files(directory))

print("\nФайли, у назві яких є 'Практична':")
print(melnyk_files.find_files(directory, "Практична"))

file_path = "diana_melnyk.txt"
text = "Ім'я: Діана\nПрізвище: Мельник\nГрупа: І-23"

melnyk_files.create_file(file_path, text)
print(f"\nСтворено файл: {file_path}")
