import os
import stotska_files

directory = r"D:\програмування\practice12"

print("Файли в каталозі:", directory)
for name in stotska_files.list_files(directory):
    print(" -", name)

substring = "py"
found = stotska_files.find_files(directory, substring)
print(f"\nФайли, що містять '{substring}':", found)

info = "Ім'я: Софія\nПрізвище: Стоцька\nГрупа: ІТ31"
path = stotska_files.create_file("student_info.txt", info)
print("\nСтворено файл:", path)