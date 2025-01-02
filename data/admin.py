from django.contrib import admin
from .models import (
    Responsable, 
    Sector, 
    Partido, 
    CasoCorrupcion,
    RegionChileCUT,
    ProvinciaChileCUT,
    ComunaChileCUT,
    CorruptionPerceptionIndexChile,
    CEPDatosPercepcion
)

@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color')
    search_fields = ('nombre',)

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sector')
    list_filter = ('sector',)
    search_fields = ('nombre',)

@admin.register(CasoCorrupcion)
class CasoCorrupcionAdmin(admin.ModelAdmin):
    list_display = ('caso', 'año', 'get_responsables', 'partido', 'monto', 'estado')
    list_filter = ('año', 'partido', 'estado')
    search_fields = ('caso', 'responsables__nombre')
    autocomplete_fields = ['responsables', 'partido']

    def get_responsables(self, obj):
        return ", ".join([r.nombre for r in obj.responsables.all()])
    get_responsables.short_description = 'Responsables'

@admin.register(RegionChileCUT)
class RegionChileCUTAdmin(admin.ModelAdmin):
    list_display = ('cut_region', 'region')
    search_fields = ('region',)

@admin.register(ProvinciaChileCUT)
class ProvinciaChileCUTAdmin(admin.ModelAdmin):
    list_display = ('cut_provincia', 'provincia', 'region')
    list_filter = ('region',)
    search_fields = ('provincia',)

@admin.register(ComunaChileCUT)
class ComunaChileCUTAdmin(admin.ModelAdmin):
    list_display = ('cut_comuna', 'comuna', 'provincia')
    list_filter = ('provincia__region',)
    search_fields = ('comuna',)

@admin.register(CorruptionPerceptionIndexChile)
class CorruptionPerceptionIndexChileAdmin(admin.ModelAdmin):
    list_display = ('año', 'pais', 'cpi')
    list_filter = ('año',)

@admin.register(CEPDatosPercepcion)
class CEPDatosPercepcionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'encuesta', 'variable', 'porcentaje')
    list_filter = ('año', 'variable')
    search_fields = ('variable',)
