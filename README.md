# Task:
### 2.1. Módulo de Inventario

1. **Gestión de Productos**:
    
    - [ ] Crear un modelo de Producto en `models.py` con campos: nombre, descripción, precio, cantidad disponible, categoría e imágenes.
    - [ ] Crear un formulario para registrar productos en `forms.py`.
    - [ ] Implementar una vista para registrar productos (POST) y mostrar el formulario (GET).
    - [ ] Crear una vista para listar productos con opciones de búsqueda y filtrado.
    - [ ] Implementar funcionalidad para actualizar productos (editar) con su respectivo formulario.
    - [ ] Implementar funcionalidad para eliminar productos con confirmación.
    - [ ] Crear una vista para mostrar los detalles de un producto específico.
2. **Alertas de Stock**:
    
    - [ ] Implementar una función que verifique los niveles de stock y envíe notificaciones cuando un producto esté bajo.
    - [ ] Crear una lógica para generar automáticamente órdenes de compra a proveedores cuando los niveles de stock sean bajos.

### 2.2. Módulo de Compras

3. **Gestión de Proveedores**:
    
    - [ ] Asegurarte de que el módulo para gestionar proveedores esté completo (registro, actualización, eliminación y consulta).
    - [ ] Crear un modelo de Proveedor si no existe, con campos necesarios.
4. **Orden de Compra**:
    
    - [ ] Crear un formulario para generar órdenes de compra, seleccionando productos y especificando cantidades.
    - [ ] Implementar una vista que maneje la creación de órdenes de compra y actualice el inventario al recibir mercancía.
5. **Historial de Compras**:
    
    - [ ] Crear una vista para mostrar el historial de compras con filtros por fecha y proveedor.
    - [ ] Implementar la lógica para registrar y mostrar el estado de las órdenes de compra.

### 2.3. Módulo de Ventas por Catálogo

6. **Gestión de Clientes**:
    
    - [ ] Crear un modelo de Cliente en `models.py` con campos: nombre, contacto, historial de compras.
    - [ ] Crear un formulario para registrar clientes en `forms.py`.
    - [ ] Implementar una vista para listar y editar información de clientes.
7. **Catálogo de Productos**:
    
    - [ ] Asegurarte de que el catálogo de productos esté bien implementado, con opciones de búsqueda y filtrado.
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

11. **Dashboard Administrativo**:
    
    - [ ] Crear un panel de control que muestre indicadores clave sobre inventario, ventas y compras.
    - [ ] Implementar gráficos y tablas que resuman la información más relevante.
12. **Gestión de Usuarios**:
    
    - [ ] Implementar un sistema para gestionar roles y permisos de usuarios.
    - [ ] Asegurarte de que solo los usuarios autorizados tengan acceso a ciertas funciones.
13. **Reportes**:
    
    - [ ] Desarrollar una funcionalidad que permita generar reportes sobre inventario, ventas y compras.
    - [ ] Investigar bibliotecas como ReportLab o pandas para generar PDFs o archivos de Excel.

### 2.5. Módulo para Clientes

14. **Vista del Catálogo**:
    
    - [ ] Asegurarte de que los clientes puedan explorar el catálogo de productos, agregar productos al carrito y proceder a la compra.
15. **Perfil de Cliente**:
    
    - [ ] Implementar una sección donde los clientes puedan gestionar su información personal y consultar su historial de compras.

### Acciones Generales

16. **Integración y Pruebas**:
    
    - [ ] Realizar pruebas exhaustivas de cada funcionalidad implementada para asegurar que todo funcione correctamente.
    - [ ] Probar la experiencia del usuario para asegurar que sea fluida y sin errores.
17. **Documentación**:
    
    - [ ] Mantener una buena documentación de cada módulo y funcionalidad implementada para facilitar el mantenimiento y futuras mejoras.
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