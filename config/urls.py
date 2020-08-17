from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    path("", include(('cipefilos.users.urls', 'users'), namespace="users")),
    # API base url
    path("", include(('cipefilos.api.urls', 'api'), namespace="api")),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
