import os


def list_files(directory):
    """Повертає список файлів у вказаній директорії.

    Args:
        directory (str): Шлях до директорії.

    Returns:
        list: Список назв файлів.
    """
    return [
        name for name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, name))
    ]


def find_files(directory, substring):
    """Знаходить файли, у назві яких є заданий підрядок.

    Args:
        directory (str): Шлях до директорії.
        substring (str): Підрядок для пошуку.

    Returns:
        list: Список назв знайдених файлів.
    """
    return [
        name for name in list_files(directory)
        if substring in name
    ]


def create_file(path, text):
    """Створює файл із заданим текстом.

    Args:
        path (str): Шлях до нового файлу.
        text (str): Текст для запису.

    Returns:
        str: Шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
    return path


if __name__ == "__main__":
    test_directory = "."
    print("Список файлів:", list_files(test_directory))
    print("Пошук файлів із 'melnyk':", find_files(test_directory, "melnyk"))
    create_file("test_file.txt", "Тест модуля melnyk_files")
    print("Тестовий файл створено.")
