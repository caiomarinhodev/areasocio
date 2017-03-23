from django.contrib import admin

# Register your models here.
from app.models import Usuario, Categoria

admin.site.register(Usuario)
admin.site.register(Categoria)
