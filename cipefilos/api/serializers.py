from .models import Pelicula, Series, Actores, Directores, Casting, PeliculaFavorita
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

class ActorSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Actores
        fields = '__all__'
        depth = 1

class DirectoresSerializer(FlexFieldsModelSerializer):

    class Meta: 
        model = Directores
        fields = '__all__'
        depth = 1

class CastingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Casting
        fields = '__all__'

class PeliculaSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Pelicula
        #fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
        depth = 1
        expandable_fields = {
            'reparto': CastingSerializer
        }
class SeriesSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Series
        fields = '__all__'
        depth = 1
        
        expandable_fields = {
            'reparto': CastingSerializer
        }

class PeliculaFavoritaSerializer(serializers.ModelSerializer):
  
    pelicula = PeliculaSerializer()

    class Meta:
        model = PeliculaFavorita
        fields = ['pelicula']
