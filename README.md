https://github.com/NickGV/proyecto-veterinaria

# Clínica Veterinaria - Sonrisas y Patitas

Este es un proyecto de gestión para una clínica veterinaria, que permite a los usuarios gestionar sus mascotas, realizar compras y acceder a información sobre productos y servicios.

## Requisitos

- Python 3.x
- MySQL
- pip

## Instalación

1.**Clonar el repositorio:**

```bash
 git clone https://github.com/NickGV/proyecto-veterinaria.git
 cd veterinaria
```

2.**Crear un entorno virtual:**

```bash
  python -m venv venv
```

3.**Activa el entorno virtual:**

```bash
  venv\Scripts\activate
```

4. **Intalar las dependencias:**

```bash
  pip install -r requirements.txt
```

5. **Configurar la base de datos:**
- crea un archivo .env en la raiz del proyecto. Este archivo debe contener las siguientes variables:

```bash
  DB_NAME=nombre_de_la_base_de_datos
  DB_USER=usuario_de_mysql
  DB_PASSWORD=contraseña_de_mysql
  DB_HOST=localhost
  DB_PORT=3306
```

- Remplaza con tus datos

6. **Ejecutar el servidor:**

```bash
  python manage.py runserver
```

Abre tu navegador y ve a http://127.0.0.1:8000 para acceder a la aplicación.