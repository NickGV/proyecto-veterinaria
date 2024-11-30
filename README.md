# Proyecto Tienda Veterinaria

Este proyecto es una tienda en línea para una tienda de mascotas. Permite a los usuarios navegar por los productos, agregar productos al carrito, realizar compras y ver el historial de compras.

## Requisitos

- Python 3.8+
- Django 3.2+
- MongoDB 4.4+

## Configuración del entorno

1. **Clona el repositorio:**

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. **Configurar la base de datos:**
- crea un archivo .env en la raiz del proyecto. Este archivo debe contener las siguientes variables:

```bash
  DB_NAME=nombre_de_la_base_de_datos
  DB_USER=usuario_de_mysql
  DB_PASSWORD=contraseña_de_mysql
  DB_HOST=localhost
  DB_PORT=3306

  MONGO_DB_NAME=tiendaveterinaria
  MONGO_DB_USER=tu_usuario
  MONGO_DB_PASSWORD=tu_contraseña
  MONGO_DB_HOST=localhost
  MONGO_DB_PORT=27017
```

- Remplaza con tus datos

3.**Inicia el proyecto el proyecto:**

```bash
  python setup.py
```

4. **configuracion de mongo ejecuta en la consola de MongoDB:**

```bash
  use tiendaveterinaria
  db.createCollection("catalogos")
  db.createCollection("historial_compras")
  db.createCollection("historial_ventas")
  db.createCollection("carrito")
```

5. **inicia el servidor de desarrollo:**

```bash 
    python manage.py runserver
```

Abre tu navegador y ve a http://127.0.0.1:8000 para acceder a la aplicación.