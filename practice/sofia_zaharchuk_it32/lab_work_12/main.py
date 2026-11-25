from pathlib import Path

import zaharchuk_files

print("Sofia Zaharchuk, IT-32")

DIRECTORY = Path(__file__).resolve().parent
print(f"directory: {DIRECTORY}")

print("\nFiles in the directory:")
for name in zaharchuk_files.list_files(DIRECTORY):
    print(f"  {name}")

substring = "files"
found = zaharchuk_files.find_files(DIRECTORY, substring)
print(f"\nFiles with '{substring}' in the name: {found}")

card_text = "Name: Sofia\nSurname: Zaharchuk\nGroup: IT-32\n"
created = zaharchuk_files.create_file(DIRECTORY / "zaharchuk_card.txt", card_text)
print(f"\nCreated file: {created.name}")
print("Content:")
print(created.read_text(encoding="utf-8"), end="")

print("\nFiles with 'card' in the name:", zaharchuk_files.find_files(DIRECTORY, "card"))
