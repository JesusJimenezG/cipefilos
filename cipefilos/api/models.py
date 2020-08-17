from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Pelicula(models.Model):

    titulo = models.CharField(max_length=150)
    estreno = models.IntegerField(default=2000)
    imagen = models.URLField(help_text="De imdb mismo")
    resumen = models.TextField(help_text="Descripción corta")
    class Meta:
        ordering = ['titulo']

class Series(models.Model):
    
    titulo = models.CharField(max_length=150)
    estreno = models.IntegerField(default=2000)
    temporadas = models.IntegerField(default=1)
    episodios = models.IntegerField(default=1)
    imagen = models.URLField(help_text="De imdb mismo")
    resumen = models.TextField(help_text="Descripción corta")
    
    class Meta:
        ordering = ['titulo']

class Actores(models.Model):
    nombre = models.CharField(max_length=150)
    nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=150)
    imagen = models.URLField(help_text="De imdb mismo",default='https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB466677935_.png')
    peliculas = models.ManyToManyField (
        Pelicula, 
        through = 'Casting',
        null=True, 
    )
    series = models.ManyToManyField (
        Series, 
        through = 'Casting',
        null=True, 
    )
    class Meta:
        ordering = ['nombre']

class Directores(models.Model):
    nombre = models.CharField(max_length=150)
    nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=150)
    imagen = models.URLField(help_text="De imdb mismo",default='https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB466677935_.png')
    peliculas = models.ManyToManyField (
        Pelicula, 
        through = 'Casting',
        null=True, 
    )
    series = models.ManyToManyField (
        Series, 
        through = 'Casting',
        null=True, 
    )

class Casting(models.Model):

    actores = models.ForeignKey(
        Actores,
        null=True,
        on_delete=models.CASCADE
    )
    directores = models.ForeignKey(
        Directores,
        null=True,
        on_delete=models.CASCADE
    )
    pelicula = models.ForeignKey(
        Pelicula,
        null=True,
        on_delete=models.CASCADE
    )
    serie = models.ForeignKey(
        Series,
        null=True,
        on_delete=models.CASCADE
    )

class PeliculaFavorita(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)