import os
from os import path

def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Параметри:
    directory (str): Шлях до директорії.

    Повертає:
    list: Список імен файлів у директорії.
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def find_files(directory, substring):
    """
    Шукає файли в директорії, у назві яких є переданий підрядок.

    Параметри:
    directory (str): Шлях до директорії.
    substring (str): Підрядок для пошуку у назвах файлів.

    Повертає:
    list: Список знайдених файлів, що містять підрядок.
    """
    return [f for f in os.listdir(directory) if substring in f and os.path.isfile(os.path.join(directory, f))]

def create_file(path, text):
    """
    Створює файл із вказаним текстом.

    Параметри:
    path (str): Шлях до файлу, який потрібно створити.
    text (str): Текст, який буде записаний у файл.

    Повертає:
    str: Шлях до створеного файлу.
    """
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
    return path

if __name__ == "__main__":
    print("Самоперевірка модуля: цей код не повинен виконуватися при імпорті.")
    print("Файли в поточній директорії:", list_files('.'))
    print("Файли, що містять 'test':", find_files('.', 'test'))
    create_file('test.txt', 'Це тестовий файл.')
    print("Створено файл 'test.txt'")
