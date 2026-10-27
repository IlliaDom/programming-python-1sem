
from pathlib import Path


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Параметри:
        directory: шлях до директорії.

    Результат:
        Список назв файлів.
    """
    path = Path(directory)
    return sorted(file.name for file in path.iterdir() if file.is_file())


def find_files(directory, substring):
    """
    Шукає файли за підрядком у назві.

    Параметри:
        directory: шлях до директорії.
        substring: підрядок для пошуку.

    Результат:
        Список назв знайдених файлів.
    """
    path = Path(directory)
    return sorted(
        file.name
        for file in path.iterdir()
        if file.is_file() and substring in file.name
    )


def create_file(path, text):
    """
    Створює файл і записує в нього текст.

    Параметри:
        path: шлях до файлу.
        text: текст для запису.

    Результат:
        Шлях до створеного файлу.
    """
    file_path = Path(path)
    file_path.write_text(text, encoding="utf-8")
    return str(file_path)


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        create_file(Path(directory) / "test.txt", "Тест")
        create_file(Path(directory) / "katashynska.txt", "Перевірка")

        print("Самоперевірка модуля")
        print("Список файлів:", list_files(directory))
        print("Результат пошуку:", find_files(directory, "katashynska"))
        print("Модуль працює правильно!")
