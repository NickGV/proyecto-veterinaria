from django.shortcuts import render, redirect, get_object_or_404
from .models import AcercaDe, Producto, Proveedor, Compra, Menu
from .forms import AcercaDeForm, ProductoForm, ProveedorForm, CompraForm, Userform, MenuForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

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
    form = ProveedorForm()
    return render(request, 'proveedores.html', {'proveedores': proveedores, 'form': form})

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
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    return redirect('proveedores')

def edit_provider(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    return redirect('proveedores')

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