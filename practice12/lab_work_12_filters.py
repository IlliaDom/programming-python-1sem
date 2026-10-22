"""Модуль для роботи з файлами: перегляд, пошук і створення."""

import os


def list_files(directory):
    """Повертає список файлів у директорії.

    Параметри:
        directory (str): шлях до директорії.

    Результат:
        list[str]: імена файлів (без підкаталогів).
    """
    return [
        name for name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, name))
    ]


def find_files(directory, substring):
    """Шукає в директорії файли, у назві яких є підрядок.

    Параметри:
        directory (str): шлях до директорії.
        substring (str): підрядок, який має бути в назві файлу.

    Результат:
        list[str]: імена знайдених файлів.
    """
    return [name for name in list_files(directory) if substring in name]


def create_file(path, text):
    """Створює новий файл із переданим текстом.

    Параметри:
        path (str): шлях до файлу, який потрібно створити.
        text (str): текст, що буде записаний у файл.

    Результат:
        str: шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


if __name__ == "__main__":
    # Самоперевірка модуля
    print("Файли в поточній папці:", list_files("."))
    print("Файли зі словом 'files':", find_files(".", "files"))
    print("Створено:", create_file("selftest.txt", "Тестовий текст"))
