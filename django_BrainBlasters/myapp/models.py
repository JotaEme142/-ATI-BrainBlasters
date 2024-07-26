from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from auditlog.models import AuditlogHistoryField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
class BaseModel(models.Model):
    created_by = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, related_name='%(class)s_created')
    modified_by = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True, related_name='%(class)s_modified')
    history = AuditlogHistoryField()

    class Meta:
        abstract = True

class Usuario(AbstractBaseUser, PermissionsMixin, BaseModel):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Añadido el campo is_active
    password = models.CharField(max_length=128, unique=True)
    alias = models.CharField(max_length=50, unique=True)
    ROLES = (
        ('admin', 'Administrador'),
        ('user', 'Usuario'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'alias']

    def __str__(self):
        return self.email

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    puntaje_acumulado = models.IntegerField(default=0)

class Pregunta(models.Model):
     categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
     tipo = models.BooleanField(default=False)
     pregunta_txt1 = models.CharField(max_length=100, null=True)
     pregunta_txt2 = models.CharField(max_length=100, null=True)
     pregunta_txt3 = models.CharField(max_length=100, null=True)
     pregunta_txt4 = models.CharField(max_length=100, null=True)
     pregunta_img1 = models.ImageField(null=True)
     pregunta_img2 = models.ImageField(null=True)
     pregunta_img3 = models.ImageField(null=True)
     pregunta_img4 = models.ImageField(null=True)
     respuesta = models.IntegerField(default=0)

class Trivia(models.Model):
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    pregunta = models.OneToOneField(Pregunta, on_delete=models.CASCADE)

class Sorteo(models.Model):
    fecha_sorteo = models.DateField()
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    ganador1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sorteos_ganados1')
    ganador2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sorteos_ganados2')
    ganador3 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sorteos_ganados3')

class Ranking(models.Model):
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    cantidad_jugadores = models.IntegerField(default=0)

class Premio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)
    ganador = models.OneToOneField(Usuario, null=True, unique=True, on_delete=models.CASCADE)


