from pathlib import Path
import runpy

folder = Path(__file__).parent
for task in range(1, 6):
    print(f"\n===== Завдання {task} =====")
    runpy.run_path(str(folder / f"task{task}.py"), run_name="__main__")
