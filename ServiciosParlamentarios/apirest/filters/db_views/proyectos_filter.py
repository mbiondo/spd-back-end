from rest_framework.compat import django_filters
from apirest.models.db_views.proyectos import Proyectos
from django.db.models import Q

class ProyectosFilter(django_filters.FilterSet):
    
    tipoproy = django_filters.CharFilter(lookup_type='icontains',name="tipo_proy");
    
    class Meta:
        model = Proyectos
        fields = ['codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','fecha','periodo','titulo','voces','resultado','tipo_proy','nro_ley']
        
        