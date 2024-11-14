from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, LoginForm
from django.contrib.auth.models import User


def auth_view(request):
    registro_form = RegistroForm()
    login_form = LoginForm()

    if request.method == 'POST':
        # Verificar si el formulario enviado es de registro
        if 'registro_submit' in request.POST:
            registro_form = RegistroForm(request.POST)
            if registro_form.is_valid():
                # Aquí puedes crear el usuario
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

        # Verificar si el formulario enviado es de inicio de sesión
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

def editar_view(request):
    return render(request, 'editar_perfilU.html')

def recuperar_view(request):
    return render(request, 'recuperar.html')


def logout_view(request):
    logout(request)
    return redirect('auth')