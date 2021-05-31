from django.contrib import admin
from django.urls import path
from .views import index,galeria,contactanos,noticias,nosotros,registrar,enviar_noti,categoria,ingresar

urlpatterns = [   
    path('',index,name="index"),
    path('galeria/',galeria,name='gal'),
    path('contacto/',contactanos,name='contac'),
    path('noticia/<id>/',noticias,name='noti'),
    path('nosotros/',nosotros,name='nos'),
    path('registrar/',registrar,name='regis'),
    path('enviar_noticia/',enviar_noti,name='enviar_n'),
    path('Categoria/<id>/',categoria,name='categ'),
    path('Ingresar/',ingresar,name='ingresar'),
]