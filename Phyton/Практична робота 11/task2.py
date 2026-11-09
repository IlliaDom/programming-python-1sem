import os
import sys
NAME = "Sasha"        
SURNAME = "Romanitch"   
GROUP = "IT-32"        
USAGE = "usage: python3 task2.py [--force] <source> <destination>"
def copy_file(src, dst, force):
    if not os.path.exists(src):
        raise FileNotFoundError(f"source {src} not found")
    if os.path.isdir(src):
        raise IsADirectoryError(f"source {src} is a directory, not a file")
    if os.path.isdir(dst):
        raise IsADirectoryError(f"destination {dst} is a directory, not a file")
 
    folder = os.path.dirname(dst) or "."
    if not os.path.isdir(folder):
        raise FileNotFoundError(f"destination folder {folder} not found")
 
    if os.path.exists(dst) and os.path.samefile(src, dst):
        raise ValueError("source and destination are the same file")
 
    with open(src, encoding="utf-8", newline="") as f:
        text = f.read()
 
    mode = "w" if force else "x"
    try:
        with open(dst, mode, encoding="utf-8", newline="") as f:
            f.write(text)
    except FileExistsError:
        raise FileExistsError(f"{dst} already exists, use --force to overwrite") from None
def main(argv):
    print(f"{NAME} {SURNAME}, {GROUP}")
    force = False
    args = []
    for a in argv:
        if a == "--force":
            force = True
        elif a.startswith("--"):
            print(USAGE, file=sys.stderr)
            return 2
        else:
            args.append(a)
    if len(args) != 2:
        print(USAGE, file=sys.stderr)
        return 2
    src, dst = args
    try:
        copy_file(src, dst, force)
    except UnicodeDecodeError:
        print(f"error: source {src} is not a UTF-8 text file", file=sys.stderr)
        return 1
    except (FileNotFoundError, IsADirectoryError, FileExistsError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    except PermissionError as e:
        print(f"error: permission denied: {e.filename}", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"error: {e.strerror or e}", file=sys.stderr)
        return 1
    else:
        print(f"copied: {src} -> {dst}")
        return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
 