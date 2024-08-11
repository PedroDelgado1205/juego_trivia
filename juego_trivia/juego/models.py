from django.db import models
from django.contrib.auth.models import User

class Nivel(models.Model):
    numero = models.IntegerField(unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f'Nivel {self.numero}'

class Pregunta(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='preguntas/', null=True, blank=True)

    def __str__(self):
        return self.texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.texto} / {self.pregunta.texto}'

class Resultado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    tiempo = models.IntegerField()  # en segundos
    aciertos = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Resultado de {self.usuario.username}'

class Juego(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nivel_actual = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    respuestas_correctas = models.IntegerField(default=0)
    resultado_juego = models.ForeignKey(Resultado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Juego de {self.usuario.username} en {self.nivel_actual}'



