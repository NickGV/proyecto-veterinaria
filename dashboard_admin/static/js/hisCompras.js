document.getElementById("compraProveedor").addEventListener("change", function () {
  var proveedorId = this.value;
  console.log(`Proveedor ID seleccionado: ${proveedorId}`);
  var productosSelects = document.querySelectorAll('select[name="producto"]');
  productosSelects.forEach(function (select) {
    select.innerHTML = '<option value="">Seleccione un producto</option>';
  });

  if (proveedorId) {
    fetch(`/dashboard_admin/get_productos_proveedor/${proveedorId}/`)
      .then((response) => response.json())
      .then((data) => {
        console.log("Productos recibidos:", data);
        productosSelects.forEach(function (select) {
          data.forEach(function (producto) {
            var option = document.createElement("option");
            option.value = producto.nombre;
            option.textContent = producto.nombre;
            option.setAttribute("data-precio", producto.precio);
            select.appendChild(option);
          });
        });
      })
      .catch((error) => console.error("Error fetching productos:", error));
  }
});

document.getElementById("add-producto").addEventListener("click", function () {
  var productosContainer = document.getElementById("productos-container");
  var newRow = document.createElement("div");
  newRow.classList.add("row", "mb-2");
  newRow.innerHTML = `
        <div class="col">
            <select class="form-select" name="producto" required>
                <option value="">Seleccione un producto</option>
            </select>
        </div>
        <div class="col">
            <input type="number" class="form-control" name="cantidad" placeholder="Cantidad" required>
        </div>
        <div class="col">
            <input type="text" class="form-control" name="precio" placeholder="Precio" readonly>
        </div>
    `;
  productosContainer.appendChild(newRow);

  // Re-populate the new select with products
  var proveedorId = document.getElementById("compraProveedor").value;
  if (proveedorId) {
    fetch(`/dashboard_admin/get_productos_proveedor/${proveedorId}/`)
      .then((response) => response.json())
      .then((data) => {
        var select = newRow.querySelector('select[name="producto"]');
        data.forEach(function (producto) {
          var option = document.createElement("option");
          option.value = producto.nombre;
          option.textContent = producto.nombre;
          option.setAttribute("data-precio", producto.precio);
          select.appendChild(option);
        });
      })
      .catch((error) => console.error("Error fetching productos:", error));
  }
});

document
  .getElementById("productos-container")
  .addEventListener("change", function (event) {
    if (event.target.name === "producto") {
      var precio = event.target.selectedOptions[0].getAttribute("data-precio");
      event.target.closest(".row").querySelector('input[name="precio"]').value =
        precio;
      calcularTotal();
    } else if (event.target.name === "cantidad") {
      calcularTotal();
    }
  });

function calcularTotal() {
  var total = 0;
  var rows = document.querySelectorAll("#productos-container .row");
  rows.forEach(function (row) {
    var precio = parseFloat(row.querySelector('input[name="precio"]').value);
    var cantidad = parseInt(row.querySelector('input[name="cantidad"]').value);
    if (!isNaN(precio) && !isNaN(cantidad)) {
      total += precio * cantidad;
    }
  });
  document.getElementById("compraTotal").value = total.toFixed(2);
}
