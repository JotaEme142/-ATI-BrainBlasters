from django.shortcuts import render


# Create your views here.



def base(request):
    return render(request,"base.html")

def base_SeleccionarCategoria(request):
    categorias = ["Arte","Ciencia","Deportes","Entretenimiento","Geografia","Historia","Cine","Matematica"]
    return render(request,"base_SeleccionarCategoria.html",{"categorias":categorias,})