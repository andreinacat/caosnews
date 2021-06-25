from django.shortcuts import render
# permite accedr a vistas genericas
from rest_framework import generics
from caos_news.models import Noticia,Comentarios
from .serializers import noticias_serialize,comentario_serializer



# Create your views here.

class noticiasViewSet(generics.ListAPIView):
    queryset = Noticia.objects.filter(publicar=True).order_by('-fecha_not')
    serializer_class = noticias_serialize

class comentarioCreateViewSet(generics.ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = comentario_serializer

class noticiaBuscarViewSet(generics.ListAPIView):
    serializer_class = noticias_serialize
    def get_queryset(self):
        cate_id = self.kwargs['categoria_id']
        return Noticia.objects.filter(categoria=cate_id)
    