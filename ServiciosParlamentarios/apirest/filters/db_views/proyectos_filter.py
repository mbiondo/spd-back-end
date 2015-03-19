from rest_framework.compat import django_filters
from apirest.models.db_views.proyectos import Proyectos
from django.db.models import Q

class ProyectosFilter(django_filters.FilterSet):
    
    tipoproy = django_filters.CharFilter(lookup_type='icontains',name="tipoproy");
    
    class Meta:
        model = Proyectos
        fields = ['codigoexp','codigonum','codigoorigen','codigoanio','sumario','tipocamara','tipo','codigoestado','fechacaducidad','fecha','periodo','titulo','voces','resultado','tipoproy','nroley']
        
        