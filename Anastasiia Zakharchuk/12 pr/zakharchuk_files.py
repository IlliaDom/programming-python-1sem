"""Module for working with files: list, search and create."""

from pathlib import Path


def list_files(directory):
    """Return a list of file names in a directory.

    Parameters:
        directory: path to the directory (str or Path).
    Returns:
        sorted list of file names (folders are not included).
    """
    folder = Path(directory)
    names = []
    for entry in folder.iterdir():
        if entry.is_file():
            names.append(entry.name)
    return sorted(names)


def find_files(directory, substring):
    """Find files whose name contains a substring.

    Parameters:
        directory: path to the directory (str or Path).
        substring: text to look for in file names.
    Returns:
        sorted list of matching file names.
    """
    found = []
    for name in list_files(directory):
        if substring in name:
            found.append(name)
    return found


def create_file(path, text):
    """Create a new file with the given text.

    Parameters:
        path: path to the new file (str or Path).
        text: text to write into the file.
    Returns:
        Path of the created file.
    """
    file_path = Path(path)
    file_path.write_text(text, encoding="utf-8")
    return file_path


def main():
    folder = Path(__file__).resolve().parent
    print("files:", list_files(folder))
    print("found 'files':", find_files(folder, "files"))
    created = create_file(folder / "selfcheck.txt", "self-check ok\n")
    print("created:", created.name)
    print("text:", created.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    main()