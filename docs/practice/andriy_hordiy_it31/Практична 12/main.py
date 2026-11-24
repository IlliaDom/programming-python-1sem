import hordiy_files
from pathlib import Path
print(hordiy_files.list_files(Path("/Users/admin/Desktop")))

print(hordiy_files.find_files(Path("/Users/admin/Desktop"),"d"))

hordiy_files.create_file("/Users/admin/Desktop/practic12_task3.txt","Файл успішно створено")