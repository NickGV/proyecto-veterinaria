from django.shortcuts import render, redirect
from .models import AcercaDe
from .forms import AcercaDeForm
# Create your views here.
def moduloadmin_view(request):
     return render(request, 'modAdmin.html')

def inventario_view(request):
     return render(request, 'inventario.html')

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
     return

def edit_product(request):
     return

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