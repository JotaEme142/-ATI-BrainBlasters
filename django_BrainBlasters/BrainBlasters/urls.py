from django.contrib import admin
from django.urls import path, include
from usuarios.views import login, register, exit
from myapp.views import home_jugador, seleccionarcategoria, respondercategoria, help

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('home_usuario/', home_jugador, name='home_usuario'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', exit, name='exit'),
    path('seleccionarcategoria/', seleccionarcategoria, name='seleccionarcategoria'),
    path('respondercategoria/', respondercategoria, name='respondercategoria'),
    path('help/', help, name='help'),
]
