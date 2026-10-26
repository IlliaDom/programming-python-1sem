import lab_work_12_filters


directory = "."


files = lab_work_12_filters.list_files(directory)
print("Файли в каталозі:", files)


found = lab_work_12_filters.find_files(directory, "files")
print("Знайдено за підрядком 'files':", found)


path = lab_work_12_filters.create_file("student.txt", "Міщук Назарій, група IT-32")
print("Створено файл:", path)
