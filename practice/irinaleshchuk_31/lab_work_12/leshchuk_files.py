
import os


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    :param directory: шлях до директорії
    :return: список назв файлів
    """
    return [
        file for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file))
    ]


def find_files(directory, substring):
    """
    Шукає файли, у назві яких є заданий підрядок.

    :param directory: шлях до директорії
    :param substring: підрядок для пошуку
    :return: список знайдених файлів
    """
    return [
        file for file in list_files(directory)
        if substring in file
    ]


def create_file(path, text):
    """
    Створює файл із переданим текстом.

    :param path: шлях до нового файлу
    :param text: текст для запису
    :return: шлях до створеного файлу
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
    return path


if __name__ == "__main__":
    print("Самоперевірка модуля")

    directory = "."
    print("Список файлів:", list_files(directory))
    print("Пошук файлів:", find_files(directory, "main"))

    create_file("test_file.txt", "Тест роботи модуля")
    print("Тестовий файл успішно створено!")
