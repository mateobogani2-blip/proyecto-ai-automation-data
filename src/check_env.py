"""Script de verificación del entorno (Checkpoint 1).

Comprueba:
  1. Versión de Python instalada.
  2. Que el script corre dentro de un contenedor Docker.
  3. Que las variables de entorno definidas en .env son accesibles.
Todas las rutas son relativas a la raíz del proyecto.
"""
import os
import platform
import sys
from pathlib import Path

from dotenv import load_dotenv

# Raíz del proyecto calculada a partir de la ubicación de este archivo (sin rutas absolutas)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
REQUIRED_VARS = ["OPENAI_API_KEY", "MLFLOW_TRACKING_URI", "DATABASE_URL"]


def running_in_docker() -> bool:
    if Path("/.dockerenv").exists():
        return True
    try:
        return "docker" in Path("/proc/1/cgroup").read_text()
    except OSError:
        return False


def main() -> int:
    print("=" * 55)
    print(" VERIFICACIÓN DEL ENTORNO - AI AUTOMATION")
    print("=" * 55)

    # 1. Python
    print(f"[OK] Python {platform.python_version()} ({sys.executable})")
    if sys.version_info < (3, 10):
        print("[ERROR] Se requiere Python 3.10 o superior")
        return 1

    # 2. Docker
    in_docker = running_in_docker()
    print(f"[{'OK' if in_docker else 'WARN'}] Ejecutando dentro de Docker: {in_docker}")
    print(f"     Hostname del contenedor: {platform.node()}")

    # 3. Variables de entorno
    loaded = load_dotenv(ENV_FILE)
    print(f"[{'OK' if loaded else 'WARN'}] Archivo .env cargado: {ENV_FILE.relative_to(PROJECT_ROOT)}")
    missing = []
    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value:
            shown = value if var == "MLFLOW_TRACKING_URI" else value[:4] + "****"
            print(f"[OK] {var} = {shown}")
        else:
            print(f"[ERROR] {var} no está definida")
            missing.append(var)

    print("-" * 55)
    if missing or not in_docker:
        print("Resultado: entorno INCOMPLETO")
        return 1
    print("Resultado: entorno configurado correctamente ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
