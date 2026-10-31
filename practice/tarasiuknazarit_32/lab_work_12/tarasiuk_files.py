from pathlib import Path
import tempfile


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Args:
        directory: Шлях до директорії.

    Returns:
        Список назв файлів.
    """
    path = Path(directory)
    return [file.name for file in path.iterdir() if file.is_file()]


def find_files(directory, substring):
    """
    Шукає файли, у назві яких є заданий підрядок.

    Args:
        directory: Шлях до директорії.
        substring: Підрядок для пошуку.

    Returns:
        Список назв знайдених файлів.
    """
    files = list_files(directory)
    return [file for file in files if substring in file]


def create_file(path, text):
    """
    Створює файл і записує в нього текст.

    Args:
        path: Шлях до файлу.
        text: Текст для запису.

    Returns:
        Шлях до створеного файлу.
    """
    file_path = Path(path)
    file_path.write_text(text, encoding="utf-8")
    return file_path


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as directory:
        create_file(Path(directory) / "example.txt", "Hello!")
        create_file(Path(directory) / "test.txt", "Python")

        print("Усі файли:", list_files(directory))
        print("Знайдені файли:", find_files(directory, "test"))

        create_file(Path(directory) / "result.txt", "Перевірка модуля")
        print("Файл створено: result.txt")