#models
from .models import Pelicula, Series, Actores, Genero, PeliculaFavorita

#serializers
from .serializers import PeliculaSerializer, SeriesSerializer, ActorSerializer, GeneroSerializer, PeliculaFavoritaSerializer

#django
from rest_framework import viewsets, views, response
from django.shortcuts import get_object_or_404

#permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

#filters
from rest_framework.filters import SearchFilter, OrderingFilter

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    #filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['titulo', 'estreno']
    ordering_fields = ['titulo', 'estreno']

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    #filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['titulo', 'estreno', 'temporadas']
    ordering_fields = ['titulo', 'temporadas', 'estreno']

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actores.objects.all()
    serializer_class = ActorSerializer
    #filters
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['nombre', 'nacionalidad', 'peliculas__titulo', 'series__titulo']
    ordering_fields = ['nombre']

class MarcarPeliculaFavorita(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        pelicula = get_object_or_404(
            Pelicula, id=self.request.data.get('id', 0)
        )

        favorita, created = PeliculaFavorita.objects.get_or_create(
            pelicula=pelicula, usuario=request.user
        )

        content = {
            'id': pelicula.id,
            'favorita': True
        }

        if not created:
            favorita.delete()
            content['favorita'] = False

        return Response(content)

class ListPeliculasFavoritas(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        peliculas_favoritas = PeliculaFavorita.objects.filter(usuario=request.user)
        serializer = PeliculaFavoritaSerializer(peliculas_favoritas, many=True)

        return Response(serializer.data)
        