// Array para almacenar los proveedores
let proveedores = [];

// Registrar Proveedor
document.getElementById("form-proveedores").addEventListener("submit", function(event) {
    event.preventDefault();
    
    // Obtener datos del formulario
    const nombre = document.getElementById("nombre").value;
    const contacto = document.getElementById("contacto").value;
    const direccion = document.getElementById("direccion").value;
    const catalogo = document.getElementById("catalogo").value;

    // Crear objeto proveedor y agregarlo al array
    const proveedor = { nombre, contacto, direccion, catalogo };
    proveedores.push(proveedor);

    // Actualizar tabla de proveedores
    actualizarTablaProveedores();

    // Resetear el formulario
    this.reset();
});

// Actualizar tabla de proveedores
function actualizarTablaProveedores() {
    const tabla = document.getElementById("tabla-proveedores").querySelector("tbody");
    tabla.innerHTML = "";  // Limpiar tabla

    proveedores.forEach((prov, index) => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
            <td>${prov.nombre}</td>
            <td>${prov.contacto}</td>
            <td>${prov.direccion}</td>
            <td>${prov.catalogo}</td>
            <td>
                <button class="btn-detalles" onclick="mostrarDetallesProveedor(${index})">Detalles</button>
                <button class="btn-editar" onclick="editarProveedor(${index})">Editar</button>
                <button class="btn-eliminar" onclick="eliminarProveedor(${index})">Eliminar</button>
            </td>
        `;
        tabla.appendChild(fila);
    });
}

// Mostrar detalles de proveedor
function mostrarDetallesProveedor(index) {
    const proveedor = proveedores[index];
    const detallesSection = document.getElementById("detalles-proveedor");

    // Mostrar detalles en el apartado
    detallesSection.innerHTML = `
        <h3>Detalles del Proveedor</h3>
        <p><strong>Nombre:</strong> ${proveedor.nombre}</p>
        <p><strong>Contacto:</strong> ${proveedor.contacto}</p>
        <p><strong>Dirección:</strong> ${proveedor.direccion}</p>
        <p><strong>Catálogo:</strong> ${proveedor.catalogo}</p>
    `;
    detallesSection.style.display = "block";  // Mostrar sección
}

// Editar Proveedor
function editarProveedor(index) {
    const proveedor = proveedores[index];
    document.getElementById("nombre").value = proveedor.nombre;
    document.getElementById("contacto").value = proveedor.contacto;
    document.getElementById("direccion").value = proveedor.direccion;
    document.getElementById("catalogo").value = proveedor.catalogo;

    // Eliminar proveedor del array temporalmente para actualizar después
    proveedores.splice(index, 1);
    actualizarTablaProveedores();
}

// Eliminar Proveedor
function eliminarProveedor(index) {
    if (confirm("¿Estás seguro de que deseas eliminar este proveedor?")) {
        proveedores.splice(index, 1);  // Eliminar proveedor
        actualizarTablaProveedores();  // Actualizar tabla
    }
}

// Crear Orden de Compra
document.getElementById("form-orden-compra").addEventListener("submit", function(event) {
    event.preventDefault();
    const proveedor = document.getElementById("proveedor").value;
    const producto = document.getElementById("producto").value;
    const cantidad = document.getElementById("cantidad").value;
    const fecha = document.getElementById("fecha").value;

    alert(`Orden de Compra creada:
Proveedor: ${proveedor}
Producto: ${producto}
Cantidad: ${cantidad}
Fecha de Recepción: ${fecha}`);

    document.getElementById("orden-proveedor").textContent = proveedor;
    document.getElementById("orden-producto").textContent = producto;
    document.getElementById("orden-cantidad").textContent = cantidad;
    document.getElementById("orden-fecha").textContent = fecha;

    // Hacer visible la sección de detalles de la orden
    document.getElementById("orden-info").style.display = "block";

    // Resetear el formulario de orden de compra
    this.reset();
});
