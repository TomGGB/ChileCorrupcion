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
    CEPDatosPercepcion,
    ComparacionMonetaria
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
    list_display = ('caso', 'año', 'get_responsables', 'get_partidos', 'monto', 'estado')
    list_filter = ('año', 'partido', 'estado', 'comuna')
    search_fields = ('caso', 'responsables__nombre', 'partido__nombre', 'comuna__comuna')
    autocomplete_fields = ['responsables', 'partido', 'comuna']
    filter_horizontal = ('partido', 'comuna', 'responsables')

    def get_responsables(self, obj):
        return ", ".join([r.nombre for r in obj.responsables.all()])
    get_responsables.short_description = 'Responsables'

    def get_partidos(self, obj):
        return ", ".join([p.nombre for p in obj.partido.all()])
    get_partidos.short_description = 'Partidos'

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

@admin.register(ComparacionMonetaria)
class ComparacionMonetariaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'formatted_valor', 'descripcion')
    search_fields = ('nombre',)
    
    def formatted_valor(self, obj):
        return f"${obj.valor:,}"
    formatted_valor.short_description = "Valor (CLP)"
