from pathlib import Path

import romaniuk_files
from romaniuk_files import find_files
from romaniuk_files import create_file as create

files_list = romaniuk_files.list_files(Path("../../../../ISO").resolve())

print("Files in directory:")

for item in files_list:
    print(item)

found_files = find_files(Path("../../../../Blender").resolve(), "d.blend")

print("\nd.blend files in directory:")

for item in found_files:
    print(item)

create(Path("../text.txt").resolve(), "Oleksandr Romaniuk IT-31")

print("\nCreated file")