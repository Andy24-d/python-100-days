import os
from pathlib import Path

# Definición de niveles y rangos de días
levels = [
    ("Beginner", range(1, 15)),         # 1–14
    ("Intermediate", range(15, 32)),    # 15–31
    ("Intermediate+", range(32, 59)),   # 32–58
    ("Advanced", range(59, 81)),        # 59–80
    ("Professional", range(81, 101)),   # 81–100
]

root = Path(".").resolve()

# Crea niveles y asegura versionado de carpetas vacías con .gitkeep
for level, days in levels:
    level_dir = root / level
    level_dir.mkdir(exist_ok=True)
    # añade .gitkeep para asegurar que se versiona aunque esté vacío
    (level_dir / ".gitkeep").touch(exist_ok=True)
    for d in days:
        day_dir = level_dir / f"day-{d:02d}"
        day_dir.mkdir(exist_ok=True)
        # archivos iniciales
        (day_dir / "main.py").touch(exist_ok=True)
        (day_dir / "README.md").write_text(
            f"# {level} - Day {d:02d}\n\nQué hice hoy:\n- \n\nNotas:\n- \n"
        )

print("Estructura creada.")