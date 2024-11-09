// Variables
const carrito = document.querySelector("#carrito");
const listaProductos = document.querySelector("#lista-productos");
const contenedorCarrito = document.querySelector("#lista-carrito tbody");
const vaciarCarritoBtn = document.querySelector("#vaciar-carrito");
const totalPriceElement = document.getElementById("total-price");
let articulosCarrito = [];

// Cargar Event Listeners
cargarEventListeners();

function cargarEventListeners() {
  listaProductos.addEventListener("click", agregarProducto);
  carrito.addEventListener("click", eliminarProducto);

  document.addEventListener("DOMContentLoaded", () => {
    articulosCarrito = JSON.parse(localStorage.getItem("carrito")) || [];
    carritoHTML();
  });

  vaciarCarritoBtn.addEventListener("click", () => {
    articulosCarrito = [];
    limpiarHTML();
    actualizarCarrito();
  });
}

function agregarProducto(e) {
  e.preventDefault();
  if (e.target.classList.contains("agregar-carrito")) {
    const producto = e.target.parentElement.parentElement;
    leerDatosProducto(producto);
    productoAgregado(producto);
  }
}

function productoAgregado(producto) {
  const alert = document.createElement("H4");
  alert.style.cssText =
    "background-color: red; color: white; text-align: center; padding: 10px";
  alert.style.margin = "5px 20px";
  alert.textContent = "Añadido al carrito";
  producto.appendChild(alert);
  setTimeout(() => {
    alert.remove();
  }, 2000);
}

function eliminarProducto(e) {
  if (e.target.classList.contains("borrar-producto")) {
    const productoId = e.target.getAttribute("data-id");

    articulosCarrito = articulosCarrito.filter(
      (producto) => producto.id !== productoId
    );
    carritoHTML();
    actualizarCarrito();
  }
}

function leerDatosProducto(producto) {
  const infoProducto = {
    imagen: producto.querySelector("img").src,
    titulo: producto.querySelector("h4").textContent,
    precio: producto.querySelector(".precio span").textContent,
    id: producto.querySelector("a").getAttribute("data-id"),
    cantidad: 1,
  };

  const existe = articulosCarrito.some(
    (producto) => producto.id === infoProducto.id
  );

  if (existe) {
    const productos = articulosCarrito.map((producto) => {
      if (producto.id === infoProducto.id) {
        producto.cantidad++;
        return producto;
      } else {
        return producto;
      }
    });
    articulosCarrito = [...productos];
  } else {
    articulosCarrito = [...articulosCarrito, infoProducto];
  }

  carritoHTML();
  actualizarCarrito();
}

function carritoHTML() {
  limpiarHTML();

  articulosCarrito.forEach((producto) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>  
        <img src="${producto.imagen}" width=100>
      </td>
      <td>${producto.titulo}</td>
      <td>${producto.precio}</td>
      <td>${producto.cantidad}</td>
      <td>
        <a href="#" class="borrar-producto" data-id="${producto.id}">X</a>
      </td>
    `;
    contenedorCarrito.appendChild(row);
  });

  sincronizarStorage();
}

function sincronizarStorage() {
  localStorage.setItem("carrito", JSON.stringify(articulosCarrito));
}

function limpiarHTML() {
  while (contenedorCarrito.firstChild) {
    contenedorCarrito.removeChild(contenedorCarrito.firstChild);
  }
}

function actualizarCarrito() {
  const carritoContainer = document.querySelector(".carrito-container");
  carritoContainer.innerHTML = "";
  let total = 0;

  articulosCarrito.forEach((producto, index) => {
    const productoHTML = `
      <div class="carrito-item">
        <h3>${producto.titulo}</h3>
        <p>Precio: $${producto.precio}</p>
        <button class="remove-button" data-index="${index}">Eliminar</button>
      </div>
    `;
    carritoContainer.innerHTML += productoHTML;
    total += parseFloat(producto.precio) * producto.cantidad;
  });

  totalPriceElement.textContent = total.toFixed(2);
}

document.querySelector(".carrito-container").addEventListener("click", (e) => {
  if (e.target.classList.contains("remove-button")) {
    const index = e.target.getAttribute("data-index");
    articulosCarrito.splice(index, 1);
    localStorage.setItem("carrito", JSON.stringify(articulosCarrito));
    actualizarCarrito();
    carritoHTML();
  }
});
