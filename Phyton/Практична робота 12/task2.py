import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import task1


def main():
    directory = os.path.expanduser("~")

    print("Directory:", directory)
    print()

    files = task1.list_files(directory)
    print("Files in directory:", len(files))
    for name in files[:10]:
        print("  ", name)
    print()

    found = task1.find_files(directory, ".txt")
    print("Files containing '.txt':", len(found))
    for name in found[:10]:
        print("  ", name)
    print()

    new_file = os.path.join(directory, "petrenko_info.txt")
    text = "First name: Ivan\nLast name: Petrenko\nGroup: KN-21\n"
    ok = task1.create_file(new_file, text)
    print("Created file:", new_file, "->", ok)


if __name__ == "__main__":
    main()