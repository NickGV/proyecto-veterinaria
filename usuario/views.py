from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import RegistroForm, LoginForm, EditarPerfilForm
from django.contrib.auth.models import User

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
