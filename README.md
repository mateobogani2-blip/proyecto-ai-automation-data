# Proyecto AI Automation — Checkpoint 1

Entorno de desarrollo reproducible con Docker + Dev Containers.

## Estructura
```
.devcontainer/devcontainer.json   # Config del Dev Container para VS Code
config/settings.yaml              # Configuración YAML del proyecto
data/                             # Datos locales (no versionados)
notebooks/                        # Experimentación
src/check_env.py                  # Script de verificación
Dockerfile                        # Imagen de desarrollo (python:3.10-slim)
.dockerignore / .gitignore
.env.example                      # Plantilla de credenciales
requirements.txt
```

## Uso
1. Abrir la carpeta en VS Code (con Docker Desktop corriendo).
2. `F1` → **Dev Containers: Reopen in Container**.
3. En la terminal del contenedor: `python src/check_env.py`
