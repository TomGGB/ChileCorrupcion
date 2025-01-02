#!/bin/bash
echo "🚀 Building application..."

# Instalar dependencias de Python
python -m pip install -r requirements.txt

# Compilar CSS con Tailwind (si tienes npm instalado)
if command -v npm &> /dev/null; then
    npm run build
fi

# Recolectar archivos estáticos
python manage.py collectstatic --noinput --clear

echo "✅ Build completed!" 