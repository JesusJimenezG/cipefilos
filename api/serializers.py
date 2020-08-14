from .models import Pelicula, Series, Actores
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

class PeliculaSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Pelicula
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
        

class SeriesSerializer(FlexFieldsModelSerializer):
    
    class Meta:
        model = Series
        fields = '__all__'

class ActoresSerializers(FlexFieldsModelSerializer):
    
    class Meta:
        model = Actores
        fields = '__all__'
        expandable_fields = {
            'peliculas': (PeliculaSerializer, {'many': True}),
            'series': (SeriesSerializer, {'many': True}),
        }
