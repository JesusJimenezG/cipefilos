from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Pelicula, Series, Actores, Directores, Casting

# Register your models here.
class PeliculaAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Titulo", {"fields": ["titulo"]}),
        ("Estreno", {"fields": ["estreno"]}),
        ("Resumen", {"fields": ["resumen"]}),
     )
    list_display = ["titulo", "estreno"]
    search_fields = ["titulo"]

class SeriesAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Titulo", {"fields": ["titulo"]}),
        ("Estreno", {"fields": ["estreno"]}),
        ("Temporadas", {"fields": ["temporadas"]}),
        ("Episodios", {"fields": ["episodios"]}),
        ("Resumen", {"fields": ["resumen"]}),
     )
    list_display = ["titulo", "estreno", "temporadas", "episodios"]
    search_fields = ["titulo"]

class CastingInLine(admin.TabularInline):
    model = Casting
    extra = 1

class ActoresAdmin(admin.ModelAdmin):
    inlines = [CastingInLine]
    fieldsets = (
        ("Nombre", {"fields": ["nombre"]}),
        ("Nacimiento", {"fields": ["nacimiento"]}),
        ("Nacionalidad", {"fields": ["nacionalidad"]}),
     )
    list_display = ["nombre", "nacimiento", "nacionalidad"]
    search_fields = ["nombre"]

class DirectoresAdmin(admin.ModelAdmin):
    inlines = [CastingInLine]
    fieldsets = (
        ("Nombre", {"fields": ["nombre"]}),
        ("Nacimiento", {"fields": ["nacimiento"]}),
        ("Nacionalidad", {"fields": ["nacionalidad"]}),
     )
    list_display = ["nombre", "nacimiento", "nacionalidad"]
    search_fields = ["nombre"]



admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Actores, ActoresAdmin)
admin.site.register(Directores, DirectoresAdmin)
