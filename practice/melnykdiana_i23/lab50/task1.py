"""Завдання 1. Перевірка абстрактного контракту Exporter."""

from exporters import Exporter


def main():
    try:
        Exporter()
    except TypeError as error:
        print(f"error: {error}")


if __name__ == "__main__":
    main()
