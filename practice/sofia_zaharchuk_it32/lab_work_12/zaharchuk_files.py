"""Module for working with files."""

import tempfile
from pathlib import Path


def list_files(directory):
    """Return the files of a directory.

    Args: directory - path to the folder.
    Returns: sorted list of file names.
    """
    return sorted(p.name for p in Path(directory).iterdir() if p.is_file())


def find_files(directory, substring):
    """Find files whose name contains a substring.

    Args: directory - path to the folder, substring - text to look for.
    Returns: list of the found file names.
    """
    return [name for name in list_files(directory) if substring.lower() in name.lower()]


def create_file(path, text):
    """Create a file with the given text.

    Args: path - path to the new file, text - text to write.
    Returns: path to the created file.
    """
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    return file_path


def main():
    print("Sofia Zaharchuk, IT-32")
    with tempfile.TemporaryDirectory() as temp_dir:
        create_file(Path(temp_dir) / "report_one.txt", "one")
        create_file(Path(temp_dir) / "report_two.txt", "two")
        create_file(Path(temp_dir) / "notes.txt", "notes")

        print("list_files:", list_files(temp_dir))
        print("find_files 'report':", find_files(temp_dir, "report"))
        print("find_files 'xyz':", find_files(temp_dir, "xyz"))

        created = create_file(Path(temp_dir) / "card.txt", "hello")
        print("create_file:", created.name, "exists:", created.exists())


if __name__ == "__main__":
    main()