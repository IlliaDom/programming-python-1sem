#Батура Каріна, ІТ-31
import sys
from pathlib import Path

def main():
    print("Karina Batura, IT-31")
    args = sys.argv[1:]
    force = "--force" in args
    if force:
        args.remove("--force")

    if len(args) != 2:
        print("usage: python3 task2.py [--force] <source> <destination>", file=sys.stderr)
        sys.exit(2)

    src = Path(args[0])
    dst = Path(args[1])

    try:
        if not src.exists():
            print(f"error: source {src} not found", file=sys.stderr)
            sys.exit(1)
        if src.is_dir():
            print(f"error: source {src} is a directory, not a file", file=sys.stderr)
            sys.exit(1)
        if not dst.parent.exists():
            print(f"error: destination folder {dst.parent} not found", file=sys.stderr)
            sys.exit(1)
        if dst.is_dir():
            print(f"error: destination {dst} is a directory, not a file", file=sys.stderr)
            sys.exit(1)

        try:
            if src.resolve() == dst.resolve():
                print("error: source and destination are the same file", file=sys.stderr)
                sys.exit(1)
        except OSError:
            pass

        if dst.exists() and not force:
            print(f"error: {dst} already exists, use --force to overwrite", file=sys.stderr)
            sys.exit(1)

        content = src.read_text(encoding="utf-8")
        dst.write_text(content, encoding="utf-8")
        print(f"copied: {src} -> {dst}")
        sys.exit(0)

    except OSError as e:
        print(f"error: {e.strerror} ({type(e).__name__})", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()