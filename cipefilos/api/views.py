#models
from .models import Pelicula, Series, Actores, PeliculaFavorita

#serializers
from .serializers import PeliculaSerializer, SeriesSerializer, ActorSerializer, PeliculaFavoritaSerializer

#django
from rest_framework import mixins, status, viewsets, response

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

class MarcarPeliculaFavorita(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pelicula = get_object_or_404(
            Pelicula, id=self.request.data.get('id', 0)
        )

        favorita, created = PeliculaFavorita.objects.get_or_create(
            pelicula=pelicula, usuario=request.user
        )
        # Por defecto suponemos que se crea bien
        content = {
            'id': pelicula.id,
            'favorita': True
        }
        # Si no se ha creado es que ya existe, entonces borramos el favorito
        if not created:
            favorita.delete()
            content['favorita'] = False
            
        return Response(content)
