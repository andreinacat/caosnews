from caos_news.models import Noticia,Comentarios
from rest_framework import serializers

# se define el modelo de datos para serializar

class noticias_serialize(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ["nombre_not","fecha_not","autor","redac","img_not","categoria","publicar","comentario"]

class comentario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ["nombre_c","apellido_c","mail_c","coment"]

         

          
           
            
          
            
          