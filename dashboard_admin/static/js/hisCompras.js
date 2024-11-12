// Función para filtrar la tabla según los filtros aplicados
function filterTable() {
    const clientFilter = document.getElementById("search-client").value.toLowerCase();
    const productFilter = document.getElementById("search-product").value.toLowerCase();
    const dateFilter = document.getElementById("search-date").value;
    const categoryFilter = document.getElementById("search-category").value.toLowerCase();
    
    const rows = document.querySelectorAll("#purchase-history tbody tr");

    rows.forEach(row => {
        const date = row.cells[0].textContent;
        const orderNumber = row.cells[1].textContent;
        const product = row.cells[2].textContent.toLowerCase();
        const category = row.getAttribute("data-category");
        
        // Verificamos si el filtro está presente en la celda correspondiente
        const matchesClient = clientFilter === "" || orderNumber.toLowerCase().includes(clientFilter);
        const matchesProduct = product.includes(productFilter);
        const matchesDate = date.includes(dateFilter);
        const matchesCategory = categoryFilter === "" || category.includes(categoryFilter);
        
        if (matchesClient && matchesProduct && matchesDate && matchesCategory) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}

// Función para limpiar los filtros
function clearFilters() {
    document.getElementById("search-client").value = "";
    document.getElementById("search-product").value = "";
    document.getElementById("search-date").value = "";
    document.getElementById("search-category").value = "";
    filterTable();
}

// Funciones para acciones de la tabla (ver detalles, repetir compra, etc.)
function viewDetails(orderId) {
    alert("Mostrando detalles de la compra con ID: " + orderId);
}

function repeatPurchase(orderId) {
    alert("Repitiendo compra con ID: " + orderId);
}

function printReceipt(orderId) {
    alert("Imprimiendo recibo de la compra con ID: " + orderId);
}
