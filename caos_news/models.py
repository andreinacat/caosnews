from django.db import models
import datetime


# Create your models here.
class Categoria(models.Model):   
    cod_catg = models.IntegerField(primary_key=True)
    nombre_catg = models.CharField(max_length=50)
  
    def __str__(self):
        return self.nombre_catg

class Noticia(models.Model):
    nombre_not = models.CharField(primary_key= True, max_length=50)
    fecha_not = models.DateField(default=datetime.date.today)
    redac =  models.TextField()
    img_not = models.ImageField(upload_to='noticias',null=True)
    publicar = models.BooleanField(default=False)
    autor = models.CharField(null=True,max_length=25)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_not + "-- Publicada: "+ str(self.publicar)
class Comentarios(models.Model):
    cod_coment = models.AutoField(primary_key=True)
    nombre_c = models.CharField(max_length=25)
    apellido_c = models.CharField(max_length=25)
    mail_c = models.EmailField()
    coment = models.TextField()
    def __str__(self):
        return (str(self.cod_coment) + " - " + self.mail_c)
