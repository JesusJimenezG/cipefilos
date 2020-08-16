from .models import Pelicula, Series, Actores, Genero
from .serializers import PeliculaSerializer, SeriesSerializer, ActorSerializer, GeneroSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['titulo', 'estreno']
    ordering_fields = ['titulo', 'estreno']

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['titulo', 'estreno', 'temporadas']
    ordering_fields = ['titulo', 'temporadas', 'estreno']

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actores.objects.all()
    serializer_class = ActorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['nombre', 'nacionalidad', 'peliculas__titulo', 'series__titulo']
    ordering_fields = ['nombre']
