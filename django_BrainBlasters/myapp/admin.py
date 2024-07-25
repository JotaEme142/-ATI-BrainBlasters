from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Categoria, Jugador, Pregunta, Trivia, Sorteo, Ranking, Premio

class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ['email', 'nombre', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('nombre', 'alias')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'alias', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Usuario, CustomUserAdmin)
admin.site.register(Categoria)
admin.site.register(Jugador)
admin.site.register(Pregunta)
admin.site.register(Trivia)
admin.site.register(Sorteo)
admin.site.register(Ranking)
admin.site.register(Premio)

