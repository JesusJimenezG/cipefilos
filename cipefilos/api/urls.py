# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import (
    PeliculaViewSet,
    SerieViewSet,
    ActorViewSet,
    GeneroViewSet,
    MarcarPeliculaFavorita,
    ListPeliculasFavoritas,
)

router = DefaultRouter()

#endpoints
router.register("genero", GeneroViewSet)
router.register("pelicula", PeliculaViewSet)
router.register("series", SerieViewSet)
router.register("actores", ActorViewSet)

app_name = "api"
urlpatterns = router.urls