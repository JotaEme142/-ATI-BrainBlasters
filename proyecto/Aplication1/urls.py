from django.urls import path
from .views import bienvenida

urlpatterns = [
    #http://127.0.0.1:8000/Aplication1/bienvenida/
    path('bienvenida/', bienvenida, name='bienvenida'),
]