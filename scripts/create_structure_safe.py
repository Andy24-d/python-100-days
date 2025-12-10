#!/usr/bin/env python3
"""
Script seguro para crear la estructura de carpetas por día (day-01 a day-100)
con archivos mínimos (main.py, README.md) organizados por niveles.

Por defecto ejecuta en modo dry-run (simulación). Para aplicar cambios,
usa: python scripts/create_structure_safe.py --apply
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple


# Mapeo de días a niveles según la estructura del curso
LEVEL_MAPPING = {
    "Beginner": (1, 14),
    "Intermediate": (15, 31),
    "Intermediate+": (32, 58),
    "Advanced": (59, 80),
    "Professional": (81, 100),
}


def get_repo_root() -> Path:
    """
    Obtiene la ruta raíz del repositorio verificando la existencia de .git/
    """
    current = Path.cwd()
    while current != current.parent:
        if (current / ".git").exists():
            return current
        current = current.parent
    raise RuntimeError(
        "No se encontró el directorio .git/. "
        "Asegúrate de ejecutar este script desde dentro del repositorio."
    )


def get_level_for_day(day: int) -> str:
    """
    Devuelve el nivel correspondiente al día dado.
    """
    for level, (start, end) in LEVEL_MAPPING.items():
        if start <= day <= end:
            return level
    raise ValueError(f"Día {day} fuera de rango (1-100)")


def generate_day_folders(repo_root: Path, dry_run: bool = True) -> List[Tuple[Path, str]]:
    """
    Genera carpetas day-01 a day-100 en sus respectivos niveles.
    
    Args:
        repo_root: Ruta raíz del repositorio
        dry_run: Si es True, solo simula (no crea nada)
    
    Returns:
        Lista de tuplas (ruta, acción) indicando qué se creó o crearía
    """
    actions = []
    template_path = repo_root / "templates" / "day_readme_template.md"
    
    # Verificar que existe el template
    if not template_path.exists():
        print(f"⚠️  Advertencia: No se encontró {template_path}")
        template_content = "# Día XX\n\nDocumentación pendiente.\n"
    else:
        with open(template_path, "r", encoding="utf-8") as f:
            template_content = f.read()
    
    for day in range(1, 101):
        level = get_level_for_day(day)
        day_folder = repo_root / level / f"day-{day:02d}"
        
        # Crear carpeta del día
        if not day_folder.exists():
            if not dry_run:
                day_folder.mkdir(parents=True, exist_ok=True)
            actions.append((day_folder, "Crear carpeta"))
        else:
            actions.append((day_folder, "Ya existe"))
        
        # Crear main.py
        main_py = day_folder / "main.py"
        if not main_py.exists():
            if not dry_run:
                main_content = f'''"""Día {day:02d} - 100 Days of Python"""

def main():
    print("Día {day:02d}")


if __name__ == "__main__":
    main()
'''
                main_py.write_text(main_content, encoding="utf-8")
            actions.append((main_py, "Crear main.py"))
        else:
            actions.append((main_py, "Ya existe"))
        
        # Crear README.md desde template
        readme_md = day_folder / "README.md"
        if not readme_md.exists():
            if not dry_run:
                readme_content = template_content.replace("XX", f"{day:02d}")
                readme_md.write_text(readme_content, encoding="utf-8")
            actions.append((readme_md, "Crear README.md"))
        else:
            actions.append((readme_md, "Ya existe"))
    
    return actions


def confirm_apply() -> bool:
    """
    Solicita confirmación textual del usuario para aplicar cambios.
    """
    print("\n" + "=" * 70)
    print("⚠️  ADVERTENCIA: Estás a punto de crear ~300 archivos (100 días)")
    print("=" * 70)
    print("\nEsto generará:")
    print("  • 100 carpetas (day-01 a day-100) distribuidas en 5 niveles")
    print("  • 100 archivos main.py")
    print("  • 100 archivos README.md")
    print("\n¿Estás seguro de que deseas continuar?")
    print("Escribe 'SI, CREAR TODO' (sin comillas) para confirmar, o cualquier otra cosa para cancelar:")
    
    response = input("> ").strip()
    return response == "SI, CREAR TODO"


def main():
    """
    Punto de entrada principal del script.
    """
    # Verificar que estamos en el repositorio
    try:
        repo_root = get_repo_root()
    except RuntimeError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    print(f"📁 Repositorio detectado en: {repo_root}")
    
    # Verificar si se pasó --apply
    apply = "--apply" in sys.argv
    
    if apply:
        print("\n🔧 Modo: APLICAR CAMBIOS (--apply detectado)")
        if not confirm_apply():
            print("❌ Operación cancelada por el usuario.")
            sys.exit(0)
        print("\n✅ Confirmado. Creando estructura...\n")
    else:
        print("\n🔍 Modo: DRY-RUN (simulación)")
        print("Para aplicar cambios, ejecuta: python scripts/create_structure_safe.py --apply\n")
    
    # Generar estructura
    actions = generate_day_folders(repo_root, dry_run=not apply)
    
    # Resumen
    created = sum(1 for _, action in actions if action.startswith("Crear"))
    existing = sum(1 for _, action in actions if action == "Ya existe")
    
    print("\n" + "=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    print(f"Total de operaciones: {len(actions)}")
    print(f"  • Archivos/carpetas a crear: {created}")
    print(f"  • Ya existentes (sin cambios): {existing}")
    
    if not apply and created > 0:
        print("\n💡 Este fue un dry-run. Ningún archivo fue creado.")
        print("   Para aplicar cambios, ejecuta:")
        print("   python scripts/create_structure_safe.py --apply")
    elif apply and created > 0:
        print(f"\n✅ ¡Estructura creada exitosamente!")
        print(f"   Se crearon {created} archivos/carpetas en {repo_root}")
    else:
        print("\n✅ Todos los archivos ya existen. No hay nada que hacer.")
    
    print("=" * 70)


if __name__ == "__main__":
    main()
