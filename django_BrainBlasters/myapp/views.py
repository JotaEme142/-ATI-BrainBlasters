from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Categoria, Trivia


def base(request):
    return render(request,"base.html")

@login_required
def home_jugador(request):
    categorias = Categoria.objects.all()  # Obteniendo todas las categorías de la base de datos
    return render(request, 'home_jugador.html', {"categorias": categorias})

def base_SeleccionarCategoria(request):
    categorias = ["Arte","Ciencia","Deportes","Entretenimiento","Geografia","Historia","Cine","Matematica"]
    return render(request,"base_SeleccionarCategoria.html",{"categorias":categorias,})

def seleccionarcategoria(request):
    categorias = Categoria.objects.all()  # Obtén todas las categorías
    return render(request, 'seleccionarcategoria.html', {'categorias': categorias})

def respondercategoria(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria_id')
        if categoria_id:
            # Obtener la instancia de la categoría usando el ID
            categoria = get_object_or_404(Categoria, id=categoria_id)
            
            # Obtener los IDs de las trivias ya enviadas desde la sesión
            trivias_enviadas = request.session.get('trivias_enviadas', [])
            
            # Obtener las trivias asociadas a la categoría, excluyendo las ya enviadas
            trivia = Trivia.objects.filter(categoria=categoria).exclude(id__in=trivias_enviadas)
            
            # Si hay trivias disponibles, selecciona una y actualiza la sesión
            if trivia.exists():
                trivia_seleccionada = trivia.first()
                trivias_enviadas.append(trivia_seleccionada.id)
                request.session['trivias_enviadas'] = trivias_enviadas
                
                # Pasar los datos a la plantilla
                return render(request, 'respondercategoria.html', {'trivia': trivia_seleccionada, 'categoria_nombre': categoria.nombre})
            else:
                # Manejar el caso donde no hay trivias disponibles
                return render(request, 'respondercategoria.html', {'mensaje': 'No hay más trivias disponibles en esta categoría.'})