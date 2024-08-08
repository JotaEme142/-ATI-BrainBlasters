from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Categoria, Trivia
from .models import Jugador
from .forms import EditProfileForm
from django.contrib import messages

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
                return render(request, 'respondercategoria.html', {'trivia': trivia_seleccionada, 'categoria_nombre': categoria.nombre,'categoria_id': categoria.id})
            else:
                # Manejar el caso donde no hay trivias disponibles
                return render(request, 'respondercategoria.html', {'mensaje': 'No hay más trivias disponibles en esta categoría.'})
          

def perfil_jugador(request):

    user_id = request.user.id

    try:
        jugador = Jugador.objects.get(usuario_id=user_id)
        puntaje_acumulado = jugador.puntaje_acumulado
    except Jugador.DoesNotExist:
        puntaje_acumulado = 0  # Si no hay registro para este usuario, establecer el puntaje en 0

    return render(request, "perfil_jugador.html", {'puntaje_acumulado': puntaje_acumulado})

def editar_perfil(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil_jugador')
    else:
        form = EditProfileForm(instance=request.user)
    

    return render(request, 'editar_perfil.html', {'form': form})





def help(request):
    return render(request,"help.html")


def procesar_respuesta(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria_id')
        trivia_id = request.POST.get('trivia_id')
        respuesta_seleccionada = int(request.POST.get('respuesta'))
        
        print(f"categoria_id: {categoria_id}")
        print(f"trivia_id: {trivia_id}")
        print(f"respuesta_seleccionada: {respuesta_seleccionada}")

        # Obtener la trivia correspondiente
        trivia = get_object_or_404(Trivia, id=trivia_id)
        jugador = get_object_or_404(Jugador, usuario=request.user)
        categoria = get_object_or_404(Categoria, id=categoria_id)
        
        
        
        # Verificar si la respuesta seleccionada es correcta
        if respuesta_seleccionada == trivia.respuesta:
            # Actualizar el puntaje del jugador
            jugador.puntaje_acumulado += 100
            jugador.categoria = categoria
            jugador.save()
            
            # Mostrar mensaje de éxito
            mensaje_exito = "¡FELICIDADES, Respuesta correcta! Has ganado 100 puntos."
            messages.success(request, mensaje_exito)
            print(mensaje_exito)
            
            # Obtener la categoría de la trivia
            categoria = trivia.categoria
            print(f"Categoria: {categoria.nombre}")

            # Redirigir a una nueva trivia de la misma categoría
            # Obtener los IDs de las trivias ya enviadas desde la sesión
            trivias_enviadas = request.session.get('trivias_enviadas', [])
            print(f"Trivias enviadas: {trivias_enviadas}")

            # Obtener las trivias asociadas a la categoría, excluyendo las ya enviadas
            nueva_trivia = Trivia.objects.filter(categoria=categoria).exclude(id__in=trivias_enviadas).first()
            print(f"Nueva trivia: {nueva_trivia}")

            if nueva_trivia:
                trivias_enviadas.append(nueva_trivia.id)
                request.session['trivias_enviadas'] = trivias_enviadas
                return render(request, 'respondercategoria.html', {'trivia': nueva_trivia, 'categoria_nombre': categoria.nombre,'categoria_id': categoria.id, 'puntaje_acumulado': jugador.puntaje_acumulado})
            else:
                mensaje_info = 'No hay más trivias disponibles en esta categoría.'
                messages.info(request, mensaje_info)
                print(mensaje_info)
                return redirect('home_jugador')  
        else:
            # Mostrar mensaje de error si la respuesta es incorrecta
            mensaje_error = f"Respuesta incorrecta. La respuesta correcta era {trivia.respuesta}"
            messages.error(request, mensaje_error)
            print(mensaje_error)
            return render(request, 'respondercategoria.html', {'mensaje': mensaje_error})
