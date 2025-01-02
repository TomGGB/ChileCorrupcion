FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto del código
COPY . .

# Recolectar archivos estáticos
RUN python manage.py collectstatic --noinput

# Configurar variables de entorno
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ChileCorrupcion.settings

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "ChileCorrupcion.wsgi:application", "--bind", "0.0.0.0:8000"] 