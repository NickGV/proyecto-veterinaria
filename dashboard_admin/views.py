from django.shortcuts import render

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