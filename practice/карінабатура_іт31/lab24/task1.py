#Батура Каріна, ІТ-31
import sys
from pathlib import Path

def main():
    print("Karina Batura, IT-31")
    paths = sys.argv[1:]
    if not paths:
        print("usage: python3 task1.py <path> [<path> ...]", file=sys.stderr)
        sys.exit(2)

    checked = 0
    failed = 0

    for path_str in paths:
        checked += 1
        path = Path(path_str)
        try:
            if not path.exists():
                raise FileNotFoundError(f"{path_str}: file not found")
            if path.is_dir():
                raise IsADirectoryError(f"{path_str}: is a directory")
            
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError as e:
                raise UnicodeDecodeError(e.encoding, e.object, e.start, e.end, f"{path_str}: not a UTF-8 text file") from e

            if not content.strip():
                raise ValueError(f"{path_str}: file is empty")

            lines = content.splitlines()
            print(f"ok:    {path_str}: {len(lines)} lines, first: {lines[0] if lines else ''}")

        except (FileNotFoundError, IsADirectoryError, UnicodeDecodeError, ValueError) as e:
            failed += 1
            print(f"error: {e} ({type(e).__name__})", file=sys.stderr)
        except OSError as e:
            failed += 1
            print(f"error: {path_str}: {e.strerror} ({type(e).__name__})", file=sys.stderr)

    print(f"checked {checked}, failed {failed}")
    sys.exit(1 if failed > 0 else 0)

if __name__ == "__main__":
    main()