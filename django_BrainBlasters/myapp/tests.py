from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Categoria, Trivia  # Asegúrate de importar los modelos correctos

User = get_user_model()

class ResponderCategoriaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            nombre='Test User',
            alias='testuser'
        )
        self.client.login(email='test@example.com', password='testpassword')
        
        # Crea una categoría
        self.categoria = Categoria.objects.create(nombre='Test Category')
        
        # Crea una trivia con todos los campos necesarios
        self.trivia = Trivia.objects.create(
            categoria=self.categoria,
            tipo=False,
            pregunta='¿Cuál es la respuesta?',
            opcion_txt1='Opción 1',
            opcion_txt2='Opción 2',
            opcion_txt3='Opción 3',
            opcion_txt4='Opción 4',
            respuesta=1  # Respuesta correcta es la opción 1
        )

    def test_responder_categoria_valid(self):
        response = self.client.post(reverse('respondercategoria'), {
            'categoria_id': self.categoria.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'respondercategoria.html')
        self.assertContains(response, '¿Cuál es la respuesta?')  # Verifica que la trivia se ha pasado a la plantilla
        self.assertContains(response, self.categoria.nombre)  # Verifica que el nombre de la categoría se muestra


class LoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        # Crear un usuario
        self.user = User.objects.create_user(
            email='test@brainblasters.com',
            password='test',
            nombre='test de login',
            alias='LoginTest'
        )
        self.user.save()

def test_usuario_valido(self):
    response = self.client.post(reverse('login'), {
        'email': 'test@brainblasters.com',
        'password': 'test',
        'form1_submit': 'Submit'
    })
    # Redireccion
    self.assertEqual(response.status_code, 302)
    # URL de exito
    self.assertRedirects(response, reverse('home_jugador'))

def test_usuario_invalido(self):
    response = self.client.post(reverse('login'), {
        'email': 'test@brainblasters.com',
        'password': '321',
        'form1_submit': 'Submit'
    })
    # mantiene el estado 
    self.assertEqual(response.status_code, 200)
    # mensaje de error
    self.assertContains(response, 'Usuario o contraseña inválidos')