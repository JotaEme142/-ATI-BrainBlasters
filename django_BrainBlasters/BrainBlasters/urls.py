from django.contrib import admin
from django.urls import path, include
from usuarios.views import login, register, exit
from myapp.views import home_jugador, seleccionarcategoria, respondercategoria, perfil_jugador, editar_perfil, help
from django.shortcuts import redirect

def home_or_login(request):
    if request.user.is_authenticated:
        return redirect('home_jugador')
    else:
        return redirect('login')

urlpatterns = [
    path('', home_or_login, name='home_or_login'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('home_jugador', home_jugador, name='home_jugador'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', exit, name='exit'),
    path('seleccionarcategoria/', seleccionarcategoria, name='seleccionarcategoria'),
    path('respondercategoria/', respondercategoria, name='respondercategoria'),
    path('perfil_jugador.html', perfil_jugador, name='perfil_jugador'),
    path('home_usuario/perfil_jugador.html', perfil_jugador, name='perfil_jugador'),
    path('home_usuario/editar_perfil.html', editar_perfil, name='editar_perfil'),
    path('editar_perfil.html', editar_perfil, name='editar_perfil'),
    path('help/', help, name='help'),
]
