from django.contrib import admin
from .models import Categoria, Galeria, Noticia,Comentarios

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Comentarios)
admin.site.register(Galeria)