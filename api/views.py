from django.shortcuts import render
# permite accedr a vistas genericas
from rest_framework import generics
from caos_news.models import Noticia
from .serializers import noticias_serialize,noticias_serialize2



# Create your views here.

class noticiasViewSet(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = noticias_serialize

class noticiaCreateViewSet(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = noticias_serialize2

class noticiaBuscarViewSet(generics.ListAPIView):
    serializer_class = noticias_serialize
    def get_queryset(self):
        nombre_noti = self.kwargs['nombre_not']
        return Noticia.objects.filter(nombre_not=nombre_noti)
    