from django.contrib import admin
from .models import Categoria, Noticia,Comentarios

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Comentarios)