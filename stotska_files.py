"""Модуль для роботи з файлами: перегляд, пошук і створення."""

import os


def list_files(directory):
    """Повертає список файлів у директорії.

    Параметри:
        directory (str): шлях до директорії.

    Повертає:
        list[str]: відсортований список імен файлів (без підкаталогів).
    """
    names = os.listdir(directory)
    files = [n for n in names if os.path.isfile(os.path.join(directory, n))]
    return sorted(files)


def find_files(directory, substring):
    """Шукає в директорії файли, у назві яких є підрядок.

    Параметри:
        directory (str): шлях до директорії.
        substring (str): підрядок, який шукаємо (регістр не враховується).

    Повертає:
        list[str]: список імен знайдених файлів (порожній, якщо нічого немає).
    """
    needle = substring.lower()
    return [name for name in list_files(directory) if needle in name.lower()]


def create_file(path, text):
    """Створює новий файл із переданим текстом.

    Параметри:
        path (str): шлях до файлу, який потрібно створити.
        text (str): текст, який буде записано у файл.

    Повертає:
        str: абсолютний шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
    return os.path.abspath(path)


if __name__ == "__main__":
    # Самоперевірка: виконується лише при запуску файлу напряму
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        created = create_file(os.path.join(tmp, "report_2026.txt"), "Привіт")
        create_file(os.path.join(tmp, "notes.txt"), "нотатки")
        os.mkdir(os.path.join(tmp, "subdir"))

        print("create_file ->", created)
        print("list_files  ->", list_files(tmp))
        print("find_files('report') ->", find_files(tmp, "report"))

        assert list_files(tmp) == ["notes.txt", "report_2026.txt"]
        assert find_files(tmp, "REPORT") == ["report_2026.txt"]
        assert find_files(tmp, "xyz") == []
        with open(created, encoding="utf-8") as f:
            assert f.read() == "Привіт"

    print("Самоперевірка пройдена")