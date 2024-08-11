from django.db import models
from django.contrib.auth.models import User
from juego.models import Nivel

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
