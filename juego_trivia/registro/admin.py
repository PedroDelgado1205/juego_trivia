from django.contrib import admin
from .models import PerfilUsuario

# Registrando todos los modelos en una sola línea
admin.site.register([PerfilUsuario])
