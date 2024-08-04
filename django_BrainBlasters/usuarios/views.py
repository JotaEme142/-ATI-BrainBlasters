from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from myapp.models import Jugador

User = get_user_model()


@login_required
def login(request):
    if request.method == 'POST':
        if 'form1_submit' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            #remember_me = request.POST.get('remember_me')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home_usuario')
            else:   
                messages.error(request, 'Usuario o contraseña inválidos')          
    return render(request, "home_jugador.html")

def register(request):
    if request.method == 'POST':
        if 'form2_submit' in request.POST:
            nombre = request.POST.get('nombre_usuario')
            alias = request.POST.get('alias')
            password = request.POST.get('password')
            email = request.POST.get('email')
            acepto = request.POST.get('acepto')
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email, password=password, nombre=nombre, alias=alias)
                user.save()
                jugador = Jugador.objects.create(usuario=user, categoria=None)
                jugador.save()
                messages.success(request, 'Tu cuenta ha sido creada exitosamente.')
                return redirect('login')
            else:
                # Manejar error de usuario ya existente
                messages.error(request, 'Ya existe un usuario con este email.')
                pass
    return render(request, 'registration/login.html')

def home_usuario(request):
    return render(request, 'home_jugador.html')

def exit(request):
    logout(request)
    return redirect('login')