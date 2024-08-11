from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'juego'

urlpatterns = [
    path('game/', views.game, name='game'),
    path('respuesta/', views.respuesta, name='respuesta'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('anterior_pregunta', views.anterior_pregunta, name='anterior_pregunta'),
    path('siguiente_pregunta', views.siguiente_pregunta, name='siguiente_pregunta'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)