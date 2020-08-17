from .models import Pelicula, Series, Actores, Genero, PeliculaFavorita
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['genero']

class PeliculaSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Pelicula
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'

class SeriesSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Series
        fields = '__all__'

class ActorSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Actores
        fields = '__all__'
        expandable_fields = {
            'peliculas': (PeliculaSerializer, {'many': True, "field": ["titulo"]}),
            'series': (SeriesSerializer, {'many': True, "field": ["titulo"]}),
        }

class PeliculaFavoritaSerializer(serializers.ModelSerializer):
  
    pelicula = PeliculaSerializer()

    class Meta:
        model = PeliculaFavorita
        fields = ['pelicula']
