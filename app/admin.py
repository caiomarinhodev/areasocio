from django.contrib import admin

# Register your models here.
from app.models import Usuario, Categoria


class UsuarioAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_display = ('nome', 'id', 'cep', 'titulo', 'universidade', 'categoria', 'status_pagamento')


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'valor_categoria', 'is_active', 'created_at')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
