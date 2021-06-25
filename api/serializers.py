from caos_news.models import Noticia
from rest_framework import serializers

# se define el modelo de datos para serializar

class noticias_serialize(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ["nombre_not","fecha_not","autor","redac","img_not","categoria","publicar","comentario"]

class noticias_serialize2(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ["nombre_not","autor","redac","img_not","categoria","comentario"]

          
           
            
          
            
          