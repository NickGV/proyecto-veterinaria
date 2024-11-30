from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import RegistroForm, LoginForm, EditarPerfilForm, PagoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import carritos_collection
from dashboard_admin.models import Producto
from django.http import HttpRequest
from django.http import JsonResponse
import json

#  TODO: Implementar metodos para agregar, eliminar y modificar cantidades de productos den el carrito

# - Implementar logica para procesar pagos, servicios como stripe o paypal


def auth_view(request):
    registro_form = RegistroForm()
    login_form = LoginForm()

    if request.method == 'POST':
        if 'registro_submit' in request.POST:
            registro_form = RegistroForm(request.POST)
            if registro_form.is_valid():
                user = User.objects.create_user(
                    username=registro_form.cleaned_data['username'],
                    email=registro_form.cleaned_data['email'],
                    password=registro_form.cleaned_data['password']
                )
                user.save()
                messages.success(request, 'Registro exitoso. Puedes iniciar sesión ahora.')
                return redirect('auth')
            else:
                messages.error(request, 'Por favor corrige los errores a continuación.')

        elif 'login_submit' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                try:
                    user = authenticate(request, username=User.objects.get(email=email).username, password=password)
                except User.DoesNotExist:
                    user = None
                if user is not None:
                    login(request, user)
                    return redirect('menu')
                else:
                    messages.error(request, 'Credenciales incorrectas')

    return render(request, 'auth.html', {'registro_form': registro_form, 'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('menu')

@login_required
def editar_view(request):
    user = request.user
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('perfil_usuario')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = EditarPerfilForm(instance=user)
    return render(request, 'editar_perfilU.html', {'form': form})

def recuperar_view(request):
    return render(request, 'recuperar.html')

@login_required
def perfil_usuario(request):
    user = request.user
   

    return render(request, 'perfil_usuario.html', {
        'user': user,
    })

@login_required
def eliminar_usuario(request):
    usuario = request.user
    usuario.delete()
    messages.success(request, 'Tu cuenta ha sido eliminada.')
    return redirect('auth')  # Redirigir al login después de eliminar la cuenta

@login_required
def agregar_al_carrito(request, producto_id):
    user = request.user
    producto = Producto.objects.get(id=producto_id)
    cantidad = int(request.POST.get('cantidad', 1))
    
    carrito = carritos_collection.find_one({'user_id': user.id})
    if carrito:
        for item in carrito['items']:
            if item['producto_id'] == producto_id:
                item['cantidad'] += cantidad
                break
        else:
            carrito['items'].append({
                'producto_id': producto_id,
                'nombre': producto.nombre,
                'precio': float(producto.precio),
                'cantidad': cantidad,
                'imagen': producto.imagen.url
            })
        carritos_collection.update_one({'user_id': user.id}, {'$set': {'items': carrito['items']}})
    else:
        carritos_collection.insert_one({
            'user_id': user.id,
            'items': [{
                'producto_id': producto_id,
                'nombre': producto.nombre,
                'precio': float(producto.precio),
                'cantidad': cantidad,
                'imagen': producto.imagen.url
            }]
        })
    
    return redirect('tienda')  

@login_required
def eliminar_del_carrito(request, producto_id):
    user = request.user
    carrito = carritos_collection.find_one({'user_id': user.id})
    if carrito:
        carrito['items'] = [item for item in carrito['items'] if item['producto_id'] != producto_id]
        carritos_collection.update_one({'user_id': user.id}, {'$set': {'items': carrito['items']}})
    
    return redirect('carrito') 

@login_required
def ver_carrito(request):
    user = request.user
    carrito = carritos_collection.find_one({'user_id': user.id})
    total = 0
    if carrito:
        for item in carrito['items']:
            total += item['precio'] * item['cantidad']
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

@login_required
def modificar_cantidad(request, producto_id):
    user = request.user
    nueva_cantidad = int(request.POST.get('cantidad', 1))
    
    carrito = carritos_collection.find_one({'user_id': user.id})
    if carrito:
        for item in carrito['items']:
            if item['producto_id'] == producto_id:
                item['cantidad'] = nueva_cantidad
                break
        carritos_collection.update_one({'user_id': user.id}, {'$set': {'items': carrito['items']}})
    
    return redirect('carrito')  # Redirigir al carrito después de modificar la cantidad

def procesar_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # Procesar el pago
            carrito = carritos_collection.objects.get(id=request.session['carrito_id'])
            carrito.estado = 'pagado'
            carrito.save()
            return redirect('carrito')
    else:
        form = PagoForm()
    return render(request, 'carrito.html', {'form': form})
