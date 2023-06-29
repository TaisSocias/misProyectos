from django.contrib import admin
from .models import Especialidad, Artista, Obra, Contacto
# Register your models here.

admin.site.register(Especialidad)
admin.site.register(Artista)
admin.site.register(Obra)
admin.site.register(Contacto)