document.addEventListener("DOMContentLoaded", () => {
  const carrito = JSON.parse(localStorage.getItem("carrito")) || [];
  const botones = document.querySelectorAll(".add-to-cart");
  const categoriaSelect = document.getElementById("categoria-select");

  botones.forEach((boton) => {
    boton.addEventListener("click", () => {
      const producto = {
        id: boton.getAttribute("data-id"),
        nombre: boton.getAttribute("data-name"),
        precio: boton.getAttribute("data-price"),
      };

      carrito.push(producto);
      localStorage.setItem("carrito", JSON.stringify(carrito));
      alert(`${producto.nombre} añadido al carrito`);
    });
  });

  // Filter products by category
  categoriaSelect.addEventListener("change", (event) => {
    const categoriaSeleccionada = event.target.value;
    const productos = document.querySelectorAll(".card");

    productos.forEach((producto) => {
      if (
        categoriaSeleccionada === "todas" ||
        producto.getAttribute("data-categoria") === categoriaSeleccionada
      ) {
        producto.style.display = "block";
      } else {
        producto.style.display = "none";
      }
    });
  });
});

const carrito = document.querySelector("#carrito");
const listaProductos = document.querySelector("#lista-productos");
const contenedorCarrito = document.querySelector("#lista-carrito tbody");
const vaciarCarritoBtn = document.querySelector("#vaciar-carrito");
const totalPriceElement = document.querySelector("#total-price");
let articulosCarrito = [];

// Event listeners setup
cargarEventListeners();

function cargarEventListeners() {
  listaProductos.addEventListener("click", agregarProducto);
  carrito.addEventListener("click", eliminarProducto);

  document.addEventListener("DOMContentLoaded", () => {
    articulosCarrito = JSON.parse(localStorage.getItem("carrito")) || [];
    carritoHTML();
  });

  vaciarCarritoBtn.addEventListener("click", vaciarCarrito);
}

function agregarProducto(e) {
  e.preventDefault();
  if (e.target.classList.contains("agregar-carrito")) {
    const producto = e.target.closest(".card");
    leerDatosProducto(producto);
    mostrarMensajeProductoAgregado(producto);
  }
}

function mostrarMensajeProductoAgregado(producto) {
  if (!producto.querySelector(".alert")) {
    const alert = document.createElement("h4");
    alert.classList.add("alert");
    alert.style.cssText =
      "background-color: red; color: white; text-align: center; padding: 10px";
    alert.textContent = "Añadido al carrito";
    producto.appendChild(alert);
    setTimeout(() => alert.remove(), 2000);
  }
}

function eliminarProducto(e) {
  if (e.target.classList.contains("borrar-producto")) {
    const productoId = e.target.dataset.id;
    articulosCarrito = articulosCarrito.filter(
      (producto) => producto.id !== productoId
    );
    carritoHTML();
  }
}

function leerDatosProducto(producto) {
  const infoProducto = {
    imagen: producto.querySelector("img").src,
    titulo: producto.querySelector("h4").textContent,
    precio: parseFloat(
      producto.querySelector(".precio").textContent.replace("$", "")
    ),
    id: producto.querySelector("a").dataset.id,
    cantidad: 1,
  };

  const existe = articulosCarrito.some((prod) => prod.id === infoProducto.id);

  if (existe) {
    articulosCarrito = articulosCarrito.map((prod) => {
      if (prod.id === infoProducto.id) {
        prod.cantidad++;
      }
      return prod;
    });
  } else {
    articulosCarrito.push(infoProducto);
  }

  carritoHTML();
}

function carritoHTML() {
  limpiarHTML();

  articulosCarrito.forEach((producto) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td><img src="${producto.imagen}" width="100"></td>
      <td>${producto.titulo}</td>
      <td>$${producto.precio}</td>
      <td>${producto.cantidad}</td>
      <td><a href="#" class="borrar-producto" data-id="${producto.id}">X</a></td>
    `;
    contenedorCarrito.appendChild(row);
  });

  sincronizarStorage();
}

function vaciarCarrito() {
  articulosCarrito = [];
  limpiarHTML();
  sincronizarStorage();
}

function sincronizarStorage() {
  localStorage.setItem("carrito", JSON.stringify(articulosCarrito));
}

function limpiarHTML() {
  contenedorCarrito.innerHTML = "";
}
