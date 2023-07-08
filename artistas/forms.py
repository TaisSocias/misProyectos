from django import forms
from .models import Contacto, Obra
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):

     class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "telefono", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

class ObraForm(forms.ModelForm):

    class Meta:
        model = Obra
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    pass
