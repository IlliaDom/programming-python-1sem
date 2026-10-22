print("Mushka Vlad IT31")

from pathlib import Path
from tempfile import TemporaryDirectory


def list_files(directory):
    """Повертає список файлів у вказаній директорії.

    Args:
        directory: Шлях до директорії.

    Returns:
        Список шляхів до файлів.
    """
    path = Path(directory)
    return [item for item in path.iterdir() if item.is_file()]


def find_files(directory, substring):
    """Знаходить файли, у назві яких є заданий підрядок.

    Args:
        directory: Шлях до директорії.
        substring: Текст для пошуку в назві файлу.

    Returns:
        Список знайдених файлів.
    """
    return [
        file for file in list_files(directory)
        if substring in file.name
    ]


def create_file(path, text):
    """Створює файл і записує в нього текст.

    Args:
        path: Шлях до нового файлу.
        text: Текст, який потрібно записати.

    Returns:
        Шлях до створеного файлу.
    """
    file = Path(path)
    file.write_text(text, encoding="utf-8")
    return file


if __name__ == "__main__":
    # Самоперевірка: тестові файли створюються в тимчасовій папці.
    with TemporaryDirectory() as directory:
        create_file(Path(directory) / "test.txt", "Тест")
        create_file(Path(directory) / "notes.txt", "Нотатки")

        print("Усі файли:", [f.name for f in list_files(directory)])
        print("Пошук test:", [f.name for f in find_files(directory, "test")])

    print("Самоперевірка завершена.")
