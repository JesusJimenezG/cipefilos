#models
from .models import Pelicula, Series, Actores, PeliculaFavorita

#serializers
from .serializers import PeliculaSerializer, SeriesSerializer, ActorSerializer, PeliculaFavoritaSerializer

#django
from rest_framework import viewsets, views, response
from rest_framework.decorators import action

#permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

#filters
from rest_framework.filters import SearchFilter, OrderingFilter

class PeliculaViewSet(viewsets.ModelViewSet):

    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

    #filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['titulo', 'estreno']
    ordering_fields = ['titulo', 'estreno']
    pagination_class = None

class SerieViewSet(viewsets.ModelViewSet):

    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    #filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['titulo', 'estreno', 'temporadas']
    ordering_fields = ['titulo', 'temporadas', 'estreno']
    pagination_class = None

class ActorViewSet(viewsets.ModelViewSet):

    queryset = Actores.objects.all()
    serializer_class = ActorSerializer

    #filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['nombre', 'nacionalidad', 'peliculas__titulo', 'series__titulo']
    ordering_fields = ['nombre']
    pagination_class = None
