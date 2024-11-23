from django.shortcuts import render, redirect, get_object_or_404
from .models import AcercaDe, Producto
from .forms import AcercaDeForm, ProductoForm
# Create your views here.
def moduloadmin_view(request):
     return render(request, 'modAdmin.html')

def inventario_view(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    return render(request, 'inventario.html', {'productos': productos, 'form': form})

def hisVentas_view(request):
     return render(request, 'hisVentas.html')

def hisCompras_view(request):
     return render(request, 'hisCompras.html')

def gestionUsusarios_view(request):
     return render(request, 'gestionUsuarios.html')

def infoClientes_view(request):
     return render(request, 'infoClient.html')

def proveedores_view(request):
     return render(request, 'proveedores.html')

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

def add_provider(request):
     return

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