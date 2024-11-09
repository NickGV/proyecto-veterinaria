console.log("El archivo carrito.js se está ejecutando"); // Prueba de carga

document.addEventListener("DOMContentLoaded", () => {
  const carritoContainer = document.querySelector(".carrito-container");
  const totalPriceElement = document.getElementById("total-price");

  let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

  // Datos de prueba
  if (carrito.length === 0) {
    carrito = [
      { titulo: "Producto 1", precio: 20 },
      { titulo: "Producto 2", precio: 15 },
    ];
    localStorage.setItem("carrito", JSON.stringify(carrito));
  }

  console.log(carrito);
  actualizarCarrito();

  function actualizarCarrito() {
    carritoContainer.innerHTML = "";
    let total = 0;

    carrito.forEach((producto, index) => {
      const titulo = producto.titulo || "Producto sin título";
      const precio = producto.precio || 0;

      const productoHTML = `
          <div class="carrito-item">
            <h3>${titulo}</h3>
            <p>Precio: $${precio}</p>
            <button class="remove-button" data-index="${index}">Eliminar</button>
          </div>
        `;
      carritoContainer.innerHTML += productoHTML;
      total += parseFloat(precio);
    });

    totalPriceElement.textContent = total.toFixed(2);
  }

  carritoContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("remove-button")) {
      const index = e.target.getAttribute("data-index");
      carrito.splice(index, 1);
      localStorage.setItem("carrito", JSON.stringify(carrito));
      actualizarCarrito();
    }
  });
});
