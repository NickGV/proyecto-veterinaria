from django import forms
from .models import AcercaDe

class AcercaDeForm(forms.ModelForm):
    class Meta:
        model = AcercaDe
        fields = ['mision', 'ubicacion', 'instagram', 'facebook', 'telefono', 'whatsapp']
