from distutils.command.upload import upload

from django.db import models

# Create your models here.


class Servicio(models.Model):
    #campos del modelo servicio
    titulo= models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='servicios') #aquí le digo que suba la imágen en la carpeta servicios que va a estar dentro de la carpeta media
    #created y updated sirven para ordenar por fechas y actualización ((se suelen utilizar así))
    created= models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add= True)

    #sirve par especificar el nombre que va a tener el modelo dentro de la BD como los campos
    class Meta:
        verbose_name= 'servicio'
        verbose_name_plural = 'servicios'

    #para que devuelva el título del servicio
    def __str__(self):
        return self.titulo