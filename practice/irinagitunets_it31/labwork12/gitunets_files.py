import os


def list_files(directory):
    return [
        file for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file))
    ]


def find_files(directory, substring):
    return [
        file for file in list_files(directory)
        if substring in file
    ]


def create_file(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

    return path


if __name__ == "__main__":
    print("Усі файли:", list_files("."))
    print("Файли зі словом main:", find_files(".", "main"))