from pathlib import Path

def list_files(directory) -> None:
    """Returns all files in directory"""
    dir_files = []

    for file in sorted(directory.iterdir()):
        if file.is_file():
            dir_files.append(file.name)

    return dir_files


def find_files(directory, substring) -> None:
    """Returns files in directory which include substring"""
    found_files = []

    for file in sorted(directory.iterdir()):
        if file.is_file():
          if substring in file.name:
              found_files.append(file.name)

    return found_files


def create_file(path, text) -> None:
    """Creates new file with text or adds text to the existing ones"""
    created = open(path, "a", encoding="utf-8")
    created.write(text)
    created.close()

    return created


if __name__ ==  "__main__":
    list_files(Path("../../../../ISO").resolve())
    find_files(Path("../../../../Blender").resolve(), "d.blend")
    create_file(Path("../text.txt").resolve(), "Oleksandr Romaniuk IT-31")