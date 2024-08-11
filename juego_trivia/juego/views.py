from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from juego.models import Pregunta, Respuesta, Resultado, Nivel, Juego
from django.utils import timezone
from registro.models import PerfilUsuario

@login_required
def game(request):
    perfil = get_object_or_404(PerfilUsuario, usuario=request.user)
    nivel_actual = perfil.nivel

    pregunta_id = request.session.get('pregunta_id')
    if pregunta_id:
        pregunta = get_object_or_404(Pregunta, id=pregunta_id, nivel=nivel_actual)
    else:
        pregunta = Pregunta.objects.filter(nivel=nivel_actual).first()
        if pregunta:
            request.session['pregunta_id'] = pregunta.id

    if pregunta is None:
        return HttpResponse("No hay preguntas disponibles para el nivel actual", status=404)

    respuestas = pregunta.respuestas.all()

    return render(request, 'juego/game.html', {'pregunta': pregunta, 'respuestas': respuestas})

@login_required
def respuesta(request):
    if request.method == 'POST':
        respuesta_id = request.POST.get('respuesta_id')
        pregunta_id = request.POST.get('pregunta_id')
        tiempo_tomado = int(request.POST.get('tiempo_tomado', 0))

        if 'tiempo_total' not in request.session:
            request.session['tiempo_total'] = 0
        request.session['tiempo_total'] += tiempo_tomado

        pregunta = get_object_or_404(Pregunta, id=pregunta_id)
        juego, created = Juego.objects.get_or_create(usuario=request.user, nivel_actual=pregunta.nivel)

        if respuesta_id == '-1':
            siguiente_pregunta = Pregunta.objects.filter(nivel=pregunta.nivel, id__gt=pregunta.id).first()
            if siguiente_pregunta:
                request.session['pregunta_id'] = siguiente_pregunta.id
            else:
                return finalizar_juego(request, juego)
        else:
            respuesta = get_object_or_404(Respuesta, id=respuesta_id)

            if respuesta.es_correcta:
                juego.respuestas_correctas += 1
                juego.save()
                siguiente_pregunta = Pregunta.objects.filter(nivel=pregunta.nivel, id__gt=pregunta.id).first()
                if siguiente_pregunta:
                    request.session['pregunta_id'] = siguiente_pregunta.id
                else:
                    return finalizar_juego(request, juego)
            else:
                siguiente_pregunta = Pregunta.objects.filter(nivel=pregunta.nivel, id__gt=pregunta.id).first()
                if siguiente_pregunta:
                    request.session['pregunta_id'] = siguiente_pregunta.id
                else:
                    return finalizar_juego(request, juego)

        return redirect('juego:game')
    else:
        return redirect('juego:game')

@login_required
def anterior_pregunta(request):
    pregunta_id = request.session.get('pregunta_id')
    if pregunta_id:
        pregunta_actual = get_object_or_404(Pregunta, id=pregunta_id)
        pregunta_anterior = Pregunta.objects.filter(nivel=pregunta_actual.nivel, id__lt=pregunta_id).last()
        
        if pregunta_anterior:
            request.session['pregunta_id'] = pregunta_anterior.id

    return redirect('juego:game')

@login_required
def siguiente_pregunta(request):
    pregunta_id = request.session.get('pregunta_id')
    if pregunta_id:
        pregunta_actual = get_object_or_404(Pregunta, id=pregunta_id)
        siguiente_pregunta = Pregunta.objects.filter(nivel=pregunta_actual.nivel, id__gt=pregunta_id).first()

        if siguiente_pregunta:
            request.session['pregunta_id'] = siguiente_pregunta.id
        else:
            return redirect('resultado:result')

    return redirect('juego:game')

@login_required
def finalizar_juego(request, juego):
    puntuacion = juego.respuestas_correctas * 10
    tiempo_total = request.session.get('tiempo_total', 0)
    perfil = get_object_or_404(PerfilUsuario, usuario=request.user)
    
    resultado = Resultado.objects.create(
        usuario=request.user,
        puntuacion=puntuacion,
        tiempo=tiempo_total,
        aciertos=juego.respuestas_correctas,
        nivel=perfil.nivel,
    )

    juego.resultado_juego = resultado
    juego.save()

    if juego.respuestas_correctas == Pregunta.objects.filter(nivel=juego.nivel_actual).count():
        perfil.nivel = perfil.nivel + 1
        perfil.save()

    del request.session['pregunta_id']
    del request.session['tiempo_total']

    return redirect('resultado:result')

@login_required
def user_profile(request):
    return render(request, 'juego/user_profile.html')


