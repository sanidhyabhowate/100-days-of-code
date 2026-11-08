from pathlib import Path

base = Path(__file__).resolve().parent

folder = base / "python_records"

folder.mkdir(exist_ok=True)

file = folder / "progress.txt"

file.write_text("Python modules and packages completed", encoding="utf-8")

print(file.read_text(encoding="utf-8"))

print(file.exists())