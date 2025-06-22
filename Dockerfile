FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY . .

# Puerto expuesto
EXPOSE 8000

# Comando de producción
CMD ["gunicorn", "tu_proyecto.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]