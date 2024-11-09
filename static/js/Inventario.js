// Array para almacenar los productos
let productos = [];

// Registrar Producto
document.getElementById("form-productos").addEventListener("submit", function(event) {
    event.preventDefault();
    
    // Obtener datos del formulario
    const nombre = document.getElementById("nombre").value;
    const descripcion = document.getElementById("descripcion").value;
    const precio = parseFloat(document.getElementById("precio").value);
    const cantidad = parseInt(document.getElementById("cantidad").value);
    const categoria = document.getElementById("categoria").value;
    const imagen = document.getElementById("imagen").files[0] ? URL.createObjectURL(document.getElementById("imagen").files[0]) : "";

    // Crear objeto producto y agregarlo al array
    const producto = { nombre, descripcion, precio, cantidad, categoria, imagen };
    productos.push(producto);

    // Actualizar tabla de productos
    actualizarTablaProductos();

    // Resetear el formulario
    this.reset();
});

// Actualizar tabla de productos
function actualizarTablaProductos() {
    const tabla = document.getElementById("lista-productos");
    tabla.innerHTML = "";  // Limpiar tabla

    productos.forEach((prod, index) => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <td>${prod.nombre}</td>
            <td>${prod.descripcion}</td>
            <td>${prod.precio.toFixed(2)}</td>
            <td>${prod.cantidad}</td>
            <td>${prod.categoria}</td>
            <td><img src="${prod.imagen}" alt="Imagen del producto"></td>
            <td>
                <button onclick="editarProducto(${index})">Editar</button>
                <button onclick="eliminarProducto(${index})">Eliminar</button>
            </td>
        `;
        tabla.appendChild(fila);

        // Verificar si se necesita alerta de stock
        if (prod.cantidad < 10) {
            alert(`El producto "${prod.nombre}" está bajo en stock. Considera hacer un nuevo pedido.`);
        }
    });
}

// Editar Producto
function editarProducto(index) {
    const producto = productos[index];
    document.getElementById("nombre").value = producto.nombre;
    document.getElementById("descripcion").value = producto.descripcion;
    document.getElementById("precio").value = producto.precio;
    document.getElementById("cantidad").value = producto.cantidad;
    document.getElementById("categoria").value = producto.categoria;

    // Eliminar producto del array temporalmente para actualizar después
    productos.splice(index, 1);
    actualizarTablaProductos();
}

// Eliminar Producto
function eliminarProducto(index) {
    if (confirm("¿Estás seguro de que deseas eliminar este producto?")) {
        productos.splice(index, 1);  // Eliminar producto
        actualizarTablaProductos();  // Actualizar tabla
    }
}

// Función para redirigir al menú administrativo
function volverAlMenu() {
    // Aquí puedes cambiar la ruta a la que debe redirigir el botón
    window.location.href = "../templates/modAdmin.html";
}

