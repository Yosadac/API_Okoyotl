FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar estructura completa
COPY . .

# Específicamente asegurar la copia de tu app
COPY Okoyotl/ ./Okoyotl/

ENV PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=settings

RUN chmod +x entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]