# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import (
    PeliculaViewSet,
    SerieViewSet,
    ActorViewSet,
    MarcarPeliculaFavorita
)

router = DefaultRouter()

#endpoints
router.register("pelicula", PeliculaViewSet)
router.register("series", SerieViewSet)
router.register("actores", ActorViewSet)
router.register(r'favorita', MarcarPeliculaFavorita, basename="favorita")

app_name = "api"

urlpatterns = router.urls
