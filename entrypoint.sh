#!/bin/sh

# Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Recopilar archivos estáticos (si es necesario)
echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# Iniciar servidor
echo "Iniciando servidor..."
exec gunicorn wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3