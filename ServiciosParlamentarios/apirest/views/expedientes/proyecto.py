from rest_framework import viewsets, filters
from apirest.models.expedientes.proyecto import Proyecto
from apirest.serializers.expedientes.proyecto import ProyectoSerializer
from apirest.filters.expedientes.proyecto_filter import ProyectoFilter
from apirest.authorizers.authorizator import has_permission

class ProyectoViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = Proyecto
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    filter_class = ProyectoFilter
    ordering_fields = '__all__'
    search_fields = ( 'sumario', 'titulo', 'voces',)
        
    @has_permission
    def list(self, request, *args, **kwargs):
        """
        Lista todos los proyectos.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve el proyecto solicitado por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)