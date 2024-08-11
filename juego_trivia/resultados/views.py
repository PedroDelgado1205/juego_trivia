from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from juego.models import Pregunta, Respuesta, Resultado, Nivel, Juego
from django.utils import timezone
from registro.models import PerfilUsuario

def result(request):
    resultado = Resultado.objects.all().order_by('fecha').first()
    total_preguntas = 3
    print(resultado)
    return render(request, 'resultado/result.html', {'resultado': resultado, 'total_preguntas': total_preguntas})

def top_five(request):
    return render(request, 'resultado/top_five.html')
