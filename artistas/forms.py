from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "telefono", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'