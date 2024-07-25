from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def base(request):
    return render(request,"base.html")

@login_required
def home_jugador(request):
    return render(request, 'home_jugador.html')

def base_SeleccionarCategoria(request):
    categorias = ["Arte","Ciencia","Deportes","Entretenimiento","Geografia","Historia","Cine","Matematica"]
    return render(request,"base_SeleccionarCategoria.html",{"categorias":categorias,})

