from django.shortcuts import render
# permite accedr a vistas genericas
from rest_framework import generics
from caos_news.models import Noticia,Comentarios
from .serializers import noticias_serialize,comentario_serializer



# Create your views here.

class noticiasViewSet(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = noticias_serialize

class comentarioCreateViewSet(generics.ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = comentario_serializer

class noticiaBuscarViewSet(generics.ListAPIView):
    serializer_class = noticias_serialize
    def get_queryset(self):
        nombre_noti = self.kwargs['nombre_not']
        return Noticia.objects.filter(nombre_not=nombre_noti)
    