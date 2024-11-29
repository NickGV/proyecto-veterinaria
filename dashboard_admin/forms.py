from django import forms
from .models import AcercaDe, Producto, Proveedor, Compra, Menu
from django.contrib.auth.models import User

class AcercaDeForm(forms.ModelForm):
    mision = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    ubicacion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    whatsapp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AcercaDe
        fields = ['mision', 'ubicacion', 'instagram', 'facebook', 'telefono', 'whatsapp']

class MenuForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subtitulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    servCaninos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    servFelinos = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    testimonio1 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    testimonio2 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    testimonio3 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    
    class Meta:
        model = Menu
        fields = ['titulo', 'subtitulo', 'servCaninos', 'servFelinos', 'testimonio1', 'testimonio2', 'testimonio3']
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_disponible', 'categoria', 'imagen']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'direccion', 'telefono']  

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'producto', 'cantidad']

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']

class CatalogoProductoForm(forms.Form):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cantidad_disponible = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))