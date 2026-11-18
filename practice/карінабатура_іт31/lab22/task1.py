#Батури Каріни ІТ-31 
from pathlib import Path

def main():
    # 1. Шляхи
    current_dir = Path.cwd()
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent
    home_dir = Path.home()

    print(f"cwd:         {current_dir}")
    print(f"script:      {script_path}")
    print(f"script dir:  {script_dir}")
    print(f"home:        {home_dir}\n")

    # 2. Створення каталогів 
    data_dir = script_dir / "data"
    reports_dir = script_dir / "reports"
    backups_dir = script_dir / "backups"

    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)
    backups_dir.mkdir(exist_ok=True)

    # 3. Запис профілю у data/profile.txt
    profile_path = data_dir / "profile.txt"
    profile_content = (
        "name: Karina\n"
        "surname: Batura\n"
        "group: IT-31\n"
        "year: 2007\n"
        "language: Python\n"
    )
    profile_path.write_text(profile_content, encoding="utf-8")

    # 4. 
    print(f"profile path: {profile_path}")
    print(f"relative:    {profile_path.relative_to(script_dir)}")
    print(f"name:        {profile_path.name}")
    print(f"stem:        {profile_path.stem}")
    print(f"suffix:      {profile_path.suffix}")
    print(f"parent:      {profile_path.parent.name}")
    print(f"size:        {profile_path.stat().st_size} bytes\n")

    # 5. Виведення дерева проєкту
    print("project tree:")
    for item in sorted(script_dir.iterdir()):
        if item.is_dir():
            print(f"  {item.name}/")
            for subitem in sorted(item.iterdir()):
                print(f"    {subitem.name}")

if __name__ == "__main__":
    main()