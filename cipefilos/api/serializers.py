from .models import Pelicula, Series, Actores, PeliculasReparto, SeriesReparto, PeliculaFavorita
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

#utils
from django.shortcuts import get_object_or_404

class PeliculaSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Pelicula
        #fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
        depth = 1
        
class SeriesSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Series
        fields = '__all__'
        depth = 1

class ActorSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Actores
        fields = '__all__'
        depth = 1

class PeliculasRepartoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeliculasReparto
        fields = '__all__'

class SeriesRepartoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeriesReparto
        fields = '__all__'

class PeliculaFavoritaSerializer(serializers.ModelSerializer):
  
    pelicula = PeliculaSerializer()

    class Meta:
        model = PeliculaFavorita
        fields = ['pelicula']
