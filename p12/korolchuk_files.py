import os


def list_files(directory):
    """Повертає список файлів у директорії.

    directory - шлях до директорії.
    Результат - список імен файлів.
    """
    result = []
    for name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, name)):
            result.append(name)
    return result


def find_files(directory, substring):
    """Шукає файли, у назві яких є підрядок.

    directory - шлях до директорії.
    substring - підрядок для пошуку.
    Результат - список знайдених імен файлів.
    """
    result = []
    for name in list_files(directory):
        if substring in name:
            result.append(name)
    return result


def create_file(path, text):
    """Створює новий файл із текстом.

    path - шлях до файлу.
    text - текст для запису.
    Результат - шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


if __name__ == "__main__":
    print(list_files("."))
    print(find_files(".", "files"))
    print(create_file("test.txt", "test"))
