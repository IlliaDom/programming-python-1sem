from pathlib import Path

import zakharchuk_files

FOLDER = Path("/home/nastyazach/Drupal/3")
SUBSTRING = "entityreference"

files = zakharchuk_files.list_files(FOLDER)
print(f"files in {FOLDER}:")
for name in files:
    print("  " + name)

found = zakharchuk_files.find_files(FOLDER, SUBSTRING)
print(f"files with '{SUBSTRING}': {len(found)}")
for name in found:
    print("  " + name)

text = "Anastasia Zakharchuk, IT-32"
created = zakharchuk_files.create_file(Path(__file__).resolve().parent / "about_me.txt", text)
print("created:", created.name)
print("text:", created.read_text(encoding="utf-8"))