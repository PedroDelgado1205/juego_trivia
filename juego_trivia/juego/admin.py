from django.contrib import admin
from .models import Nivel, Pregunta, Respuesta, Juego, Resultado

# Registrando todos los modelos de la aplicación 'juego'
admin.site.register([Nivel, Pregunta, Respuesta, Juego, Resultado])
