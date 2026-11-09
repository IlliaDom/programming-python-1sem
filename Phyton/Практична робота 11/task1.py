import sys
import os
NAME = "Sasha"
SURNAME = "Romanitch"
GROUP = "IT-32"
def inspect(path):
    if os.path.isdir(path):
        raise IsADirectoryError("is a directory")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text:
        raise ValueError("file is empty")
    lines = text.splitlines()
    return len(lines), lines[0]
def main(paths):
    print(f"{NAME} {SURNAME}, {GROUP}")
    if not paths:
        print("usage: python3 task1.py <path> [<path> ...]", file=sys.stderr)
        return 2
    failed = 0
    for path in paths:
        try:
            count, first = inspect(path)
        except FileNotFoundError as e:
            reason, name = "file not found", type(e).__name__
        except IsADirectoryError as e:
            reason, name = "is a directory", type(e).__name__
        except PermissionError as e:
            reason, name = "permission denied", type(e).__name__
        except UnicodeDecodeError as e:
            reason, name = "not a UTF-8 text file", type(e).__name__
        except ValueError as e:
            reason, name = str(e), type(e).__name__
        except OSError as e:
            reason, name = e.strerror or "cannot read file", type(e).__name__
        else:
            print(f"ok:    {path}: {count} lines, first: {first}")
            continue
        failed += 1
        print(f"error: {path}: {reason} ({name})", file=sys.stderr)

    print(f"checked {len(paths)}, failed {failed}")
    return 1 if failed else 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
    