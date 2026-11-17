# Imagen base: Python 3.10 liviana
FROM python:3.10-slim

# Evita archivos .pyc y fuerza salida sin buffer (logs en tiempo real)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Dependencias de sistema: build-essential para compilar librerías de IA, git y curl
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo (relativo al contenedor, nunca rutas del host)
WORKDIR /workspace

# Instalar dependencias de Python primero para aprovechar la caché de capas
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["bash"]
