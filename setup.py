import os
import subprocess
import django
from django.conf import settings
from django.core.management import call_command

subprocess.run(['python', '-m', 'venv', 'venv'])
subprocess.run('venv\Scripts\activate', shell=True)

subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veterinaria.settings')
django.setup()

from django.contrib.auth.models import User
from dashboard_admin.models import Producto

call_command('makemigrations')
call_command('migrate')

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')

productos = [
    {
        'nombre': 'Arenero para gatos',
        'descripcion': 'Arenero grande para gatos',
        'precio': 20.00,
        'cantidad_disponible': 100,
        'categoria': 'herramientas',
        'imagen': 'productos/producto1.jfif'
    },
    {
        'nombre': 'Cepillo para gatos',
        'descripcion': 'Cepillo mediano para gatos',
        'precio': 12.00,
        'cantidad_disponible': 100,
        'categoria': 'herramientas',
        'imagen': 'productos/producto2.jfif'
    },
    {
        'nombre': 'Comida para gatos',
        'descripcion': 'Comida para gatos en lata marca Ricocat',
        'precio': 10.00,
        'cantidad_disponible': 100,
        'categoria': 'comida',
        'imagen': 'productos/producto3.jfif'
    },
    {
        'nombre': 'Juguete para gatos',
        'descripcion': 'Juguete pequeño en forma de Ratón',
        'precio': 5.00,
        'cantidad_disponible': 100,
        'categoria': 'juguetes',
        'imagen': 'productos/producto4.jpg'
    },
    {
        'nombre': 'Cepillo para perro',
        'descripcion': 'Cepillo grande para perro',
        'precio': 15.00,
        'cantidad_disponible': 100,
        'categoria': 'herramientas',
        'imagen': 'productos/producto5.jpeg'
    },
    {
        'nombre': 'Comida para perros',
        'descripcion': 'Comida para perros marca pedigree',
        'precio': 12.00,
        'cantidad_disponible': 100,
        'categoria': 'comida',
        'imagen': 'productos/producto6.jfif'
    },
    {
        'nombre': 'Juguete para perros',
        'descripcion': 'Juguete mediano para perros',
        'precio': 17.00,
        'cantidad_disponible': 100,
        'categoria': 'juguetes',
        'imagen': 'productos/producto7.jfif'
    },
    {
        'nombre': 'Shampoo para perros',
        'descripcion': 'Shampoo marca Tankful dogs',
        'precio': 22.00,
        'cantidad_disponible': 100,
        'categoria': 'aseo',
        'imagen': 'productos/producto8.jfif'
    },
]

for producto in productos:
    Producto.objects.create(**producto)

print("Setup completo.")
