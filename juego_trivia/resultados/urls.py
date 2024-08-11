from django.urls import path
from . import views

app_name = 'resultado'

urlpatterns = [
    path('result/', views.result, name='result'),
    path('top_five/', views.top_five, name='top_five'),
]
