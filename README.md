# Task:

### 2.2. Módulo de Compras

4. **Orden de Compra**:
    
    - [ ] Crear un formulario para generar órdenes de compra, seleccionando productos y especificando cantidades.
    - [ ] Implementar una vista que maneje la creación de órdenes de compra y actualice el inventario al recibir mercancía.

5. **Historial de Compras**:
    
    - [ ] Crear una vista para mostrar el historial de compras con filtros por fecha y proveedor.
    - [ ] Implementar la lógica para registrar y mostrar el estado de las órdenes de compra.

### 2.3. Módulo de Ventas por Catálogo

8. **Carrito de Compras**:
    
    - [ ] Mejorar la funcionalidad del carrito para permitir agregar productos, modificar cantidades y proceder al pago.
    - [ ] Implementar la lógica para almacenar el carrito en `localStorage` o en la sesión del usuario.
9. **Proceso de Pago**:
    
    - [ ] Investigar e integrar una plataforma de pago (como PayPal o Stripe) para gestionar transacciones.
    - [ ] Implementar la lógica para redirigir a los usuarios a la plataforma de pago y manejar la respuesta de la transacción.
10. **Historial de Ventas**:
    
    - [ ] Crear una vista para que los clientes revisen su historial de compras.
    - [ ] Implementar una vista para que la administración consulte las ventas realizadas.

### 2.4. Módulo Administrativo

13. **Reportes**:
    
    - [ ] Desarrollar una funcionalidad que permita generar reportes sobre inventario, ventas y compras.
    - [ ] Investigar bibliotecas como ReportLab o pandas para generar PDFs o archivos de Excel.

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

2. **Configurar la base de datos:**
- crea un archivo .env en la raiz del proyecto. Este archivo debe contener las siguientes variables:

```bash
  DB_NAME=nombre_de_la_base_de_datos
  DB_USER=usuario_de_mysql
  DB_PASSWORD=contraseña_de_mysql
  DB_HOST=localhost
  DB_PORT=3306
  
  MONGO_DB_NAME=nombre_de_tu_base_de_datos
  MONGO_DB_USER=tu_usuario
  MONGO_DB_PASSWORD=tu_contraseña
  MONGO_DB_HOST=localhost
  MONGO_DB_PORT=27017
```

- Remplaza con tus datos


3.**Inicia el proyecto el proyecto:**

```bash
  python -m venv venv
```

4. **Ejecutar el servidor:**

```bash
  python manage.py runserver
```

Abre tu navegador y ve a http://127.0.0.1:8000 para acceder a la aplicación.