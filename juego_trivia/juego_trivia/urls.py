from django.contrib import admin
from django.urls import include, path
from registro.views import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('registro/', include('registro.urls')),
    path('juego/', include('juego.urls', namespace='juego')),
    path('resultados/', include('resultados.urls', namespace='resultado')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

