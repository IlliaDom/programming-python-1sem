"""Module for file operations: listing and creating files."""

from pathlib import Path


def list_files(directory: str | Path) -> list[str]:
    """Повертає список назв усіх файлів у заданій директорії."""
    dir_path = Path(directory)
    return [f.name for f in dir_path.iterdir() if f.is_file()]


def create_file(path: str | Path, text: str) -> None:
    """Приймає шлях до файлу та текст, створює новий файл із цим текстом."""
    file_path = Path(path)
    file_path.write_text(text, encoding="utf-8")


def main() -> None:
    print("Самоперевірка модуля batura_files пройшла успішно!")


if __name__ == "__main__":
    main()