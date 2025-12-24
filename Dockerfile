# Dockerfile para Inverkids MCP HTTP Server
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

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
COPY server_http.py ./

# Crear usuario no-root para seguridad
RUN useradd -m -u 1000 inverkids && \
    chown -R inverkids:inverkids /app

USER inverkids

# Exponer puerto HTTP
EXPOSE 8000

# Comando para iniciar el servidor HTTP
CMD ["uvicorn", "server_http:app", "--host", "0.0.0.0", "--port", "8000"]