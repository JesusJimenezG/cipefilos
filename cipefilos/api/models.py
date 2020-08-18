from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Actores(models.Model):

    nombre = models.CharField(max_length=150)
    nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=150)
    imagen = models.URLField(help_text="De imdb mismo",default='https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB466677935_.png')

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):

    titulo = models.CharField(max_length=150)
    estreno = models.IntegerField(default=2000)
    imagen = models.URLField(help_text="De imdb mismo")
    resumen = models.TextField(help_text="Descripción corta")
    equipo = models.ManyToManyField(Actores, through='PeliculasReparto')
    class Meta:
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo

class Series(models.Model):
    
    titulo = models.CharField(max_length=150)
    estreno = models.IntegerField(default=2000)
    temporadas = models.IntegerField(default=1)
    episodios = models.IntegerField(default=1)
    imagen = models.URLField(help_text="De imdb mismo")
    resumen = models.TextField(help_text="Descripción corta")
    equipo = models.ManyToManyField(Actores, through='SeriesReparto')
    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo  

class PeliculasReparto(models.Model):

    actores = models.ForeignKey(Actores, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    director = models.CharField (max_length=150)
    imagen = models.URLField(help_text="De imdb mismo",default='https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB466677935_.png')
    nacimiento = models.DateField()

class SeriesReparto(models.Model):
    
    actores = models.ForeignKey(Actores, on_delete=models.CASCADE)
    serie = models.ForeignKey(Series, on_delete=models.CASCADE)
    director = models.CharField (max_length=150)
    imagen = models.URLField(help_text="De imdb mismo",default='https://m.media-amazon.com/images/G/01/imdb/images/nopicture/medium/name-2135195744._CB466677935_.png')
    nacimiento = models.DateField()


class PeliculaFavorita(models.Model):

    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)