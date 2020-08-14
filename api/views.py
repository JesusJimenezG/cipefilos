from .models import Pelicula, Series, Actores
from .serializers import PeliculaSerializer, SeriesSerializer, ActoresSerializers
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actores.objects.all()
    serializer_class = ActoresSerializers

