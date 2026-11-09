from pathlib import Path
import os

PERSON = {
    "name": "Sasha",
    "surname": "Romanitch",
    "group": "IT-32",
    "year": "2009",
    "language": "Python",
}


def show_paths():
    cwd = Path.cwd()
    script = Path(__file__).resolve()
    script_dir = script.parent
    home = Path.home()

    print(f"cwd:         {cwd}")
    print(f"script:      {script}")
    print(f"script dir:  {script_dir}")
    print(f"home:        {home}")
    print()
    return script_dir


def make_dirs(script_dir: Path):
    for name in ("data", "reports", "backups"):
        (script_dir / name).mkdir(exist_ok=True)


def write_profile(script_dir: Path) -> Path:
    profile = script_dir / "data" / "profile.txt"
    lines = [
        f"name: {PERSON['name']}",
        f"surname: {PERSON['surname']}",
        f"group: {PERSON['group']}",
        f"year: {PERSON['year']}",
        f"language: {PERSON['language']}",
    ]
    profile.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return profile


def show_file_info(profile: Path, script_dir: Path):
    print(f"profile path: {profile.resolve()}")
    print(f"relative:    {profile.relative_to(script_dir)}")
    print(f"name:        {profile.name}")
    print(f"stem:        {profile.stem}")
    print(f"suffix:      {profile.suffix}")
    print(f"parent:      {profile.parent.name}")
    print(f"size:        {profile.stat().st_size} bytes")
    print()


def show_tree(root: Path):
    print("project tree:")
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        depth = len(rel.parts) - 1
        indent = "  " * (depth + 1)
        if path.is_dir():
            print(f"{indent}{path.name}/")
        else:
            print(f"{indent}{path.name}")


def main():
    script_dir = show_paths()
    make_dirs(script_dir)
    profile = write_profile(script_dir)
    show_file_info(profile, script_dir)
    show_tree(script_dir)


if __name__ == "__main__":
    main()