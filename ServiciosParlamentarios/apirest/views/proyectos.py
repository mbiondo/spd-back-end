from rest_framework import viewsets
from apirest.models.db_views.proyectos import Proyectos
from apirest.serializers.db_views.proyectos import ProyectoSerializer
from apirest.filters.db_views.proyectos_filter import ProyectosFilter
from django.db.models import Q

class ProyectosViewSet(viewsets.ReadOnlyModelViewSet):

    queryset =  Proyectos.objects.all()
    serializer_class = ProyectoSerializer
    filter_class = ProyectosFilter
    ordering_fields = '__all__'
    search_fields = ('codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara',
                     'tipo','codigo_estado','fecha_caducidad','fecha','periodo','titulo','voces','resultado','tipo_proy','nro_ley')
    
      
    def list (self, request, *args, **kwargs):
        """
        Lista todos los proyectos.   
        \n
        Filtros posible:\n
         
        - tipo_proy=[tipo de proyecto]
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un proyecto determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)