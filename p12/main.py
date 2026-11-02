import korolchuk_files

directory = "."

print(korolchuk_files.list_files(directory))
print(korolchuk_files.find_files(directory, "files"))
print(korolchuk_files.create_file("info.txt", "Ярослав Корольчук, IT-31"))
