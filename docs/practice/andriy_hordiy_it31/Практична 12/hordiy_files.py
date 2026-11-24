import unicodedata
def list_files(directory):
    # Повертає список назв файлів у вказаній директорії
    files = []
    for path in directory.iterdir():
        if path.is_file():
            files.append(path.name)
    return files

def find_files(directory, substring):
    # Шукає та повертає файли за підрядком у назві
    founded_files = []
    for path in directory.iterdir():
        if path.is_file():
            if unicodedata.normalize("NFC", substring) in unicodedata.normalize("NFC", path.name):
                founded_files.append(path.name)
    return founded_files
def create_file(path, text):
    # створює файл у вказаному шляху та записує вказаний текст у цей файл
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
