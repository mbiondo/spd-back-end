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
    search_fields = ('codigoexp','codigonum','codigoorigen','codigoanio','sumario','tipocamara','tipo','codigoestado','fechacaducidad','fecha','periodo','titulo','voces','resultado','tipoproy','nroley')
    
      
    def list (self, request, *args, **kwargs):
        """
        Lista todos los proyectos.   
        \n
        Filtros posible:\n
         
        - tipoProy=[tipo de proyecto]
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un proyecto determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)