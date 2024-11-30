from django.shortcuts import render, redirect, get_object_or_404
from .models import AcercaDe, Producto, Proveedor, Compra, Menu
from .forms import AcercaDeForm, ProductoForm, ProveedorForm, CompraForm, Userform, MenuForm, CatalogoProductoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from db_connection import catalogos_collection, compras_collection, ventas_collection
from django.http import JsonResponse
from django.http import Http404
from datetime import datetime

def moduloadmin_view(request):
    return render(request, 'modAdmin.html')

def inventario_view(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'inventario.html', {'productos': productos, 'form': form})

def hisVentas_view(request):
    ventas = list(ventas_collection.find())
    for venta in ventas:
        venta['user'] = get_object_or_404(User, id=venta['user_id'])
    return render(request, 'hisVentas.html', {'ventas': ventas})

def hisCompras_view(request):
    compras = list(compras_collection.find())
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    for compra in compras:
        compra['proveedor'] = get_object_or_404(Proveedor, id=compra['proveedor_id'])
        catalogo = catalogos_collection.find_one({'proveedor_id': compra['proveedor_id']})
        if catalogo:
            catalogo_productos_nombres = [producto['nombre'] for producto in catalogo['productos']]
            for producto in compra['productos']:
                if 'nombre' in producto:
                    producto_obj = next((p for p in catalogo['productos'] if p['nombre'] == producto['nombre']), None)
                    if producto_obj:
                        producto['nombre'] = producto_obj['nombre']
                    else:
                        compra['productos'].remove(producto)
                else:
                    compra['productos'].remove(producto)
        else:
            compra['productos'] = []
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
        precio = float(request.POST.get('precio'))

        producto = {
            'nombre': nombre,
            'precio': precio,
        }

        catalogo = catalogos_collection.find_one({'proveedor_id': proveedor_id})
        if catalogo:
            catalogos_collection.update_one({'proveedor_id': proveedor_id}, {'$push': {'productos': producto}})
        else:
            catalogos_collection.insert_one({'proveedor_id': proveedor_id, 'productos': [producto]})

        return redirect('ver_catalogo', proveedor_id=proveedor.id)
    return redirect('ver_catalogo', proveedor_id=proveedor.id)

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = Userform(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if 'password' in form.cleaned_data and form.cleaned_data['password']:
                user.password = make_password(form.cleaned_data['password'])
            user.is_superuser = form.cleaned_data['is_superuser'] == 'True'
            user.save()
            return redirect('gestionUsuarios')
    else:
        form = Userform(instance=user)
    return render(request, 'GestionUsuarios.html', {'form': form, 'user': user})

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
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.is_superuser = form.cleaned_data['is_superuser'] == 'True'
            user.save()
            return redirect('gestionUsuarios')
    else:
        form = Userform()
    return render(request, 'GestionUsuarios.html', {'form': form})

def add_provider(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        productos_list = []
        nombres_productos = request.POST.getlist('producto_nombre')
        precios_productos = request.POST.getlist('producto_precio')
        for nombre_producto, precio_producto in zip(nombres_productos, precios_productos):
            productos_list.append({
                'nombre': nombre_producto.strip(),
                'descripcion': '',  
                'precio': float(precio_producto.strip()),
                'cantidad_disponible': 0 
            })

        proveedor = Proveedor(nombre=nombre, contacto=contacto, direccion=direccion, telefono=telefono)
        proveedor.save()

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
                    'descripcion': '',  
                    'precio': float(precio_producto.strip()),
                    'cantidad_disponible': 0  
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
        proveedor_id = request.POST.get('proveedor')
        productos = request.POST.getlist('producto')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio')
        total = 0

        compra_productos = []
        for i in range(len(productos)):
            try:
                producto_id = int(productos[i])
                cantidad = int(cantidades[i])
                precio = float(precios[i])
                total += precio * cantidad
                compra_productos.append({'producto_id': producto_id, 'cantidad': cantidad, 'precio': precio})
            except ValueError:
                # Manejar el error si no se puede convertir a int o float
                print(f"Error al convertir los valores: producto_id={productos[i]}, cantidad={cantidades[i]}, precio={precios[i]}")
                continue

        compra = {
            'proveedor_id': int(proveedor_id),
            'productos': compra_productos,
            'total': total,
            'fecha': request.POST.get('fecha')
        }

        # Verificar que los productos existen antes de insertarlos en MongoDB
        for item in compra_productos:
            try:
                producto = get_object_or_404(Producto, id=item['producto_id'])
                producto.cantidad_disponible -= item['cantidad']
                producto.save()
            except Http404:
                print(f"Producto con ID {item['producto_id']} no encontrado.")
                # Manejar el error como desees, por ejemplo, puedes redirigir o mostrar un mensaje de error.

        compras_collection.insert_one(compra)

        return redirect('hisCompras')
    else:
        proveedores = Proveedor.objects.all()
        productos = Producto.objects.all()
        return render(request, 'add_compra.html', {'proveedores': proveedores, 'productos': productos})
    
def add_venta(request):
    if request.method == 'POST':
        user_id = request.user.id
        items = request.POST.getlist('items')
        total = request.POST.get('total')

        venta = {
            'user_id': user_id,
            'fecha': datetime.now(),
            'items': items,
            'total': total
        }

        ventas_collection.insert_one(venta)

        # Actualizar la cantidad disponible de los productos
        for item in items:
            producto = get_object_or_404(Producto, id=item['producto_id'])
            producto.cantidad_disponible -= item['cantidad']
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

def get_productos_proveedor(request, proveedor_id):
    catalogo = catalogos_collection.find_one({'proveedor_id': proveedor_id})
    if catalogo:
        productos_data = [{'id': idx, 'nombre': producto['nombre'], 'precio': producto['precio']} for idx, producto in enumerate(catalogo['productos'])]
    else:
        productos_data = []
    return JsonResponse(productos_data, safe=False)

def editar_producto_catalogo(request, proveedor_id, producto_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    catalogo = catalogos_collection.find_one({'proveedor_id': proveedor_id})
    producto = catalogo['productos'][producto_id]

    if request.method == 'POST':
        producto['nombre'] = request.POST.get('nombre')
        producto['precio'] = float(request.POST.get('precio'))

        catalogos_collection.update_one({'proveedor_id': proveedor_id}, {'$set': {f'productos.{producto_id}': producto}})
        return redirect('ver_catalogo', proveedor_id=proveedor_id)

    return render(request, 'editar_producto_catalogo.html', {'proveedor': proveedor, 'producto': producto, 'producto_id': producto_id})

def eliminar_producto_catalogo(request, proveedor_id, producto_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    catalogos_collection.update_one({'proveedor_id': proveedor_id}, {'$unset': {f'productos.{producto_id}': 1}})
    catalogos_collection.update_one({'proveedor_id': proveedor_id}, {'$pull': {'productos': None}})
    return redirect('ver_catalogo', proveedor_id=proveedor_id)