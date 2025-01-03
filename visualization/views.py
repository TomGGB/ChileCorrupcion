from django.shortcuts import render, get_object_or_404
from data.models import CasoCorrupcion, CorruptionPerceptionIndexChile, CEPDatosPercepcion, Partido, Sector, Responsable
from django.db.models import Sum, Count, Q

def dashboard(request):
    # Datos para las tarjetas
    total_casos = CasoCorrupcion.objects.count()
    total_monto = CasoCorrupcion.objects.aggregate(Sum('monto'))['monto__sum'] or 0
    casos_resueltos = CasoCorrupcion.objects.filter(estado='Resuelto').count()
    
    # Calcular promedio
    promedio_monto = total_monto / total_casos if total_casos > 0 else 0

    # Corregir los campos año -> año
    rango_años = {
        'min': CasoCorrupcion.objects.order_by('año').first().año if CasoCorrupcion.objects.exists() else 0,
        'max': CasoCorrupcion.objects.order_by('-año').first().año if CasoCorrupcion.objects.exists() else 0
    }

    # Corregir las consultas para que coincidan con el template
    casos_por_ano = (
        CasoCorrupcion.objects
        .values('año')
        .annotate(total=Count('id'))
        .order_by('año')
    )
    
    casos_por_sector = (
        CasoCorrupcion.objects
        .values(
            'partido__sector__nombre',
            'partido__sector__color'
        )
        .annotate(
            total=Count('id'),
            total_monto=Sum('monto', default=0)
        )
        .exclude(partido__sector__isnull=True)
    )
    
    percepcion_corrupcion = list(CorruptionPerceptionIndexChile.objects.all().order_by('año').values('año', 'cpi'))
    
    casos_por_partido = (
        CasoCorrupcion.objects
        .values(
            'partido__nombre',
            'partido__sector__color'
        )
        .annotate(
            total_casos=Count('id'),
            total_monto=Sum('monto', default=0)
        )
        .exclude(partido__isnull=True)
        .order_by('-total_casos')
    )

    context = {
        'total_casos': total_casos,
        'total_monto': total_monto,
        'promedio_monto': promedio_monto,
        'casos_resueltos': casos_resueltos,
        'rango_años': rango_años,
        'casos_por_ano': list(casos_por_ano),
        'casos_por_sector': list(casos_por_sector),
        'percepcion_corrupcion': percepcion_corrupcion,
        'casos_por_partido': list(casos_por_partido),
    }
    
    return render(request, 'visualization/dashboard.html', context)

def partidos(request):
    sector_id = request.GET.get('sector')
    query = request.GET.get('q', '')
    
    partidos = (
        Partido.objects
        .annotate(
            total_casos=Count('casocorrupcion'),
            total_monto=Sum('casocorrupcion__monto', default=0)
        )
        .select_related('sector')
        .order_by('nombre')
    )
    
    if sector_id:
        partidos = partidos.filter(sector_id=sector_id)
    if query:
        partidos = partidos.filter(nombre__icontains=query)
    
    sectores = Sector.objects.all().order_by('nombre')
    
    return render(request, 'visualization/partidos.html', {
        'partidos': partidos,
        'sectores': sectores,
        'sector_actual': sector_id,
        'query': query
    })

def partido_detalle(request, partido_id):
    partido = (
        Partido.objects
        .annotate(
            total_casos=Count('casocorrupcion'),
            total_monto=Sum('casocorrupcion__monto', default=0),
            casos_resueltos=Count('casocorrupcion', filter=Q(casocorrupcion__estado='Resuelto'))
        )
        .select_related('sector')
        .get(id=partido_id)
    )
    
    casos = (
        CasoCorrupcion.objects
        .filter(partido=partido)
        .order_by('-año')
    )
    
    return render(request, 'visualization/partido_detalle.html', {
        'partido': partido,
        'casos': casos
    })

def involucrados(request):
    query = request.GET.get('q', '')
    
    responsables = (
        Responsable.objects
        .annotate(
            total_casos=Count('casocorrupcion'),
            total_monto=Sum('casocorrupcion__monto', default=0)
        )
        .order_by('-total_casos')
    )
    
    if query:
        responsables = responsables.filter(nombre__icontains=query)
    
    return render(request, 'visualization/involucrados.html', {
        'responsables': responsables,
        'query': query
    })

def responsable_detalle(request, responsable_id):
    responsable = (
        Responsable.objects
        .annotate(
            total_casos=Count('casocorrupcion'),
            total_monto=Sum('casocorrupcion__monto', default=0)
        )
        .get(id=responsable_id)
    )
    
    casos = (
        CasoCorrupcion.objects
        .filter(responsables=responsable)
        .prefetch_related('partido')
        .order_by('-año')
    )
    
    return render(request, 'visualization/responsable_detalle.html', {
        'responsable': responsable,
        'casos': casos
    })
