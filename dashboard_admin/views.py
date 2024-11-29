from django.shortcuts import render, redirect, get_object_or_404
from .models import AcercaDe, Producto, Proveedor, Compra, Menu
from .forms import AcercaDeForm, ProductoForm, ProveedorForm, CompraForm, Userform, MenuForm, CatalogoProductoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from db_connection import catalogos_collection

# TODO: metodos para obtener y mostrar todas las ventas realizadas

# TODO: Metodos para generar reportes de inventario, ventas y compras

# Usando librerias como panda para generar archivos PDF o Excel, crear tambien una template de reporte con las opciones de geneerar y descargar reportes

def moduloadmin_view(request):
    return render(request, 'modAdmin.html')


def reportes_view(request):
    return render(request, 'Reportes.html')

def inventario_view(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'inventario.html', {'productos': productos, 'form': form})

def hisVentas_view(request):
    return render(request, 'hisVentas.html', {'ventas': ventas})

def hisCompras_view(request):
    compras = Compra.objects.all()
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    return render(request, 'hisCompras.html', {'compras': compras, 'proveedores': proveedores, 'productos': productos})

def gestionUsusarios_view(request):
    usuarios = User.objects.all()
    return render(request, 'GestionUsuarios.html', {'Users': usuarios, 'form': Userform})

def infoClientes_view(request):
    return render(request, 'infoClient.html')

def proveedores_view(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})

def ver_catalogo(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    catalogo = catalogos_collection.find_one({'proveedor_id': proveedor_id})
    productos = catalogo['productos'] if catalogo else []
    return render(request, 'catalogo.html', {'proveedor': proveedor, 'productos': productos})

def agregar_producto_catalogo(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = float(request.POST.get('precio'))
        cantidad_disponible = int(request.POST.get('cantidad_disponible'))

        producto = {
            'nombre': nombre,
            'descripcion': descripcion,
            'precio': precio,
            'cantidad_disponible': cantidad_disponible
        }

        catalogo = catalogos_collection.find_one({'proveedor_id': proveedor_id})
        if catalogo:
            catalogos_collection.update_one({'proveedor_id': proveedor_id}, {'$push': {'productos': producto}})
        else:
            catalogos_collection.insert_one({'proveedor_id': proveedor_id, 'productos': [producto]})

        return redirect('ver_catalogo', proveedor_id=proveedor.id)
    return redirect('ver_catalogo', proveedor_id=proveedor.id)

def edit_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = Userform(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if 'password' in form.cleaned_data and form.cleaned_data['password']:
                user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('gestionUsuarios')
    return redirect('gestionUsuarios')

def delete_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('gestionUsuarios')
    return redirect('gestionUsuarios')


def add_user(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('gestionUsuarios')
    return redirect('gestionUsuarios')

def add_provider(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        # Parsear los productos
        productos_list = []
        nombres_productos = request.POST.getlist('producto_nombre')
        precios_productos = request.POST.getlist('producto_precio')
        for nombre_producto, precio_producto in zip(nombres_productos, precios_productos):
            productos_list.append({
                'nombre': nombre_producto.strip(),
                'descripcion': '',  # Puedes agregar un campo de descripción si es necesario
                'precio': float(precio_producto.strip()),
                'cantidad_disponible': 0  # Puedes agregar un campo de cantidad disponible si es necesario
            })

        # Guardar proveedor en MySQL
        proveedor = Proveedor(nombre=nombre, contacto=contacto, direccion=direccion, telefono=telefono)
        proveedor.save()

        # Guardar catálogo en MongoDB
        catalogo_id = catalogos_collection.insert_one({'proveedor_id': proveedor.id, 'productos': productos_list}).inserted_id

        return redirect('proveedores')
    return redirect('proveedores')

def edit_provider(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            # Actualizar productos en MongoDB
            productos_list = []
            nombres_productos = request.POST.getlist('producto_nombre')
            precios_productos = request.POST.getlist('producto_precio')
            for nombre_producto, precio_producto in zip(nombres_productos, precios_productos):
                productos_list.append({
                    'nombre': nombre_producto.strip(),
                    'descripcion': '',  # Puedes agregar un campo de descripción si es necesario
                    'precio': float(precio_producto.strip()),
                    'cantidad_disponible': 0  # Puedes agregar un campo de cantidad disponible si es necesario
                })
            catalogos_collection.update_one({'proveedor_id': proveedor.id}, {'$set': {'productos': productos_list}})
            return redirect('proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
        catalogo = catalogos_collection.find_one({'proveedor_id': proveedor.id})
        productos = ';'.join([f"{p['nombre']},{p['precio']}" for p in catalogo['productos']]) if catalogo else ''
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor, 'productos': productos})

def delete_provider(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores')
    return redirect('proveedores')

def add_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    return redirect('inventario')

def edit_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    return redirect('inventario')

def delete_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('inventario')
    return redirect('inventario')

def add_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            producto = compra.producto
            producto.cantidad_disponible += compra.cantidad
            producto.save()
            return redirect('hisCompras')
    return redirect('hisCompras')

def add_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            producto = venta.producto
            producto.cantidad_disponible -= venta.cantidad
            producto.save()
            return redirect('hisVentas')
    return redirect('hisVentas')

def editar_acerca_de(request):
    acerca_de, created = AcercaDe.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = AcercaDeForm(request.POST, instance=acerca_de)
        if form.is_valid():
            form.save()
            return redirect('modulo_admin')
    else:
        form = AcercaDeForm(instance=acerca_de)
    return render(request, 'editar_acerca_de.html', {'form': form})

def editar_menu(request):
    menu, created = Menu.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('editar_menu')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'editar_menu.html', {'form': form})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        # Parsear los productos
        productos_list = []
        nombres_productos = request.POST.getlist('producto_nombre')
        precios_productos = request.POST.getlist('producto_precio')
        for nombre_producto, precio_producto in zip(nombres_productos, precios_productos):
            productos_list.append({
                'nombre': nombre_producto.strip(),
                'descripcion': '',  # Puedes agregar un campo de descripción si es necesario
                'precio': float(precio_producto.strip()),
                'cantidad_disponible': 0  # Puedes agregar un campo de cantidad disponible si es necesario
            })

        # Guardar proveedor en MySQL
        proveedor = Proveedor(nombre=nombre, contacto=contacto, direccion=direccion, telefono=telefono)
        proveedor.save()

        # Guardar catálogo en MongoDB
        catalogo_id = catalogos_collection.insert_one({'proveedor_id': proveedor.id, 'productos': productos_list}).inserted_id

        return redirect('proveedores')
    return redirect('proveedores')

def edit_provider(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            # Actualizar productos en MongoDB
            productos_list = []
            nombres_productos = request.POST.getlist('producto_nombre')
            precios_productos = request.POST.getlist('producto_precio')
            for nombre_producto, precio_producto in zip(nombres_productos, precios_productos):
                productos_list.append({
                    'nombre': nombre_producto.strip(),
                    'descripcion': '',  # Puedes agregar un campo de descripción si es necesario
                    'precio': float(precio_producto.strip()),
                    'cantidad_disponible': 0  # Puedes agregar un campo de cantidad disponible si es necesario
                })
            catalogos_collection.update_one({'proveedor_id': proveedor.id}, {'$set': {'productos': productos_list}})
            return redirect('proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
        catalogo = catalogos_collection.find_one({'proveedor_id': proveedor.id})
        productos = catalogo['productos'] if catalogo else []
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor, 'productos': productos})

def delete_provider(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedores')
    return redirect('proveedores')

def add_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    return redirect('inventario')

def edit_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    return redirect('inventario')

def delete_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('inventario')
    return redirect('inventario')

def add_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()
            producto = compra.producto
            producto.cantidad_disponible += compra.cantidad
            producto.save()
            return redirect('hisCompras')
    return redirect('hisCompras')

def add_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            producto = venta.producto
            producto.cantidad_disponible -= venta.cantidad
            producto.save()
            return redirect('hisVentas')
    return redirect('hisVentas')

def editar_acerca_de(request):
    acerca_de, created = AcercaDe.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = AcercaDeForm(request.POST, instance=acerca_de)
        if form.is_valid():
            form.save()
            return redirect('modulo_admin')
    else:
        form = AcercaDeForm(instance=acerca_de)
    return render(request, 'editar_acerca_de.html', {'form': form})

def editar_menu(request):
    menu, created = Menu.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('editar_menu')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'editar_menu.html', {'form': form})