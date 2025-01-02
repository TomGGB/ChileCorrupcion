from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('partidos/', views.partidos, name='partidos'),
    path('partidos/<int:partido_id>/', views.partido_detalle, name='partido_detalle'),
    path('involucrados/', views.involucrados, name='involucrados'),
    path('involucrados/<int:responsable_id>/', views.responsable_detalle, name='responsable_detalle'),
]
