
import leshchuk_files


directory = "."

print("Список файлів у директорії:")
print(leshchuk_files.list_files(directory))

print("\nПошук файлів зі словом 'main':")
print(leshchuk_files.find_files(directory, "main"))

text = "Лещук Ірина, група IT-31"

leshchuk_files.create_file("student_info.txt", text)

print("\nФайл student_info.txt успішно створено!")
