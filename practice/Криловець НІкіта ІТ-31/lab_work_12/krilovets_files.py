import os


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Параметри:
        directory (str): шлях до директорії.

    Результат:
        list: список назв файлів у директорії.
    """
    return [
        name
        for name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, name))
    ]


def find_files(directory, substring):
    """
    Шукає файли, у назві яких міститься заданий підрядок.

    Параметри:
        directory (str): шлях до директорії.
        substring (str): підрядок для пошуку в назві файлу.

    Результат:
        list: список назв знайдених файлів.
    """
    return [
        name
        for name in list_files(directory)
        if substring in name
    ]


def create_file(path, text):
    """
    Створює файл із заданим текстом.

    Параметри:
        path (str): шлях до нового файлу.
        text (str): текст, який буде записано у файл.

    Результат:
        str: шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

    return path


if __name__ == "__main__":
    test_directory = "."

    print("Самоперевірка модуля")
    print("Файли в поточній директорії:")
    print(list_files(test_directory))

    print("\nФайли, що містять 'file':")
    print(find_files(test_directory, "file"))

    test_file = "test_module_file.txt"
    create_file(test_file, "Тест роботи модуля.")
    print(f"\nСтворено файл: {test_file}")