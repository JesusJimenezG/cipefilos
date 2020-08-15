from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class Genero(models.Model):
    genero = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.genero

class Pelicula(models.Model):
  titulo = models.CharField(max_length=150)
  estreno = models.IntegerField(default=2000)
  imagen = models.URLField(help_text="De imdb mismo")
  resumen = models.TextField(help_text="Descripción corta")
  generos = models.ManyToManyField(Genero)
  class Meta:
    ordering = ['titulo']

class Series(models.Model):
    titulo = models.CharField(max_length=150)
    estreno = models.IntegerField(default=2000)
    temporadas = models.IntegerField(default=1)
    episodios = models.IntegerField(default=1)
    imagen = models.URLField(help_text="De imdb mismo")
    resumen = models.TextField(help_text="Descripción corta")
    generos = models.ManyToManyField(Genero)
    class Meta:
        ordering = ['titulo']

class Actores(models.Model):
    nombre = models.CharField(max_length=150)
    nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=150)
    imagen = models.URLField(help_text="De imdb mismo",default='https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB466677935_.png')
    peliculas = models.ForeignKey(Pelicula, null=True, on_delete=models.SET_NULL)
    series = models.ForeignKey(Series, null=True, on_delete=models.SET_NULL)
    class Meta:
        ordering = ['nombre']





    