from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cipefilos.users.api.views import UserViewSet
from api import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

#endpoints
router.register("pelicula", views.PeliculaViewSet)
router.register("series", views.SerieViewSet)
router.register("actores", views.ActorViewSet)

app_name = "api"
urlpatterns = router.urls
