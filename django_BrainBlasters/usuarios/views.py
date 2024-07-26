from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def login(request):
    if request.method == 'POST':
        if 'form1_submit' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            remember_me = request.POST.get('remember_me')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home_usuario')
            else:
                # Manejar error de autenticación
                pass
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
                return redirect('login')
            else:
                # Manejar error de usuario ya existente
                pass
    return render(request, 'registration/login.html')

def home_usuario(request):
    return render(request, 'home_jugador.html')

def exit(request):
    logout(request)
    return redirect('login')