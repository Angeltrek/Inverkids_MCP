# Dockerfile para Inverkids MCP Server
FROM python:3.11-slim

# Configurar variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requisitos
COPY requirements.txt pyproject.toml ./

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src/ ./src/
COPY start_mcp.py ./

# Crear usuario no-root para seguridad
RUN useradd -m -u 1000 inverkids && \
    chown -R inverkids:inverkids /app

# Cambiar a usuario no-root
USER inverkids

# Exponer puerto si es necesario (ajustar según tu configuración)
EXPOSE 8000

# Comando por defecto
CMD ["python", "-u", "start_mcp.py"]