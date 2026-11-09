import os


def list_files(directory):
    
    if not os.path.isdir(directory):
        return []
    result = []
    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)
        if os.path.isfile(full_path):
            result.append(name)
    return result


def find_files(directory, substring):
   
    if not os.path.isdir(directory) or substring is None:
        return []
    substring_lower = substring.lower()
    result = []
    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)
        if os.path.isfile(full_path) and substring_lower in name.lower():
            result.append(name)
    return result


def create_file(path, text):
    
    try:
        parent = os.path.dirname(os.path.abspath(path))
        if parent and not os.path.isdir(parent):
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    except (OSError, ValueError):
        return False

if __name__ == "__main__":
    import tempfile

    print("=== Self-check: task1 ===")

    with tempfile.TemporaryDirectory() as tmp:
        assert list_files(tmp) == [], "Empty directory must return []"
        print("list_files (empty):", list_files(tmp))

        ok1 = create_file(os.path.join(tmp, "report.txt"), "hello")
        ok2 = create_file(os.path.join(tmp, "notes.txt"), "world")
        ok3 = create_file(os.path.join(tmp, "image.png"), "binary")
        assert ok1 and ok2 and ok3, "create_file must return True"
        print("create_file: OK")

        files = sorted(list_files(tmp))
        print("list_files:", files)
        assert files == ["image.png", "notes.txt", "report.txt"]

        found = sorted(find_files(tmp, ".txt"))
        print("find_files('.txt'):", found)
        assert found == ["notes.txt", "report.txt"]

        found2 = sorted(find_files(tmp, "REP"))
        print("find_files('REP'):", found2)
        assert found2 == ["report.txt"]

        assert list_files(os.path.join(tmp, "nope")) == []
        assert find_files(os.path.join(tmp, "nope"), "x") == []
        print("Non-existent directory: OK")
