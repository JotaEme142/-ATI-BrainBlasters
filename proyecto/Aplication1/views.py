from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("Hola profe!!, Bienvenida a la primera prueba del proyecto BrainBlasters!!")