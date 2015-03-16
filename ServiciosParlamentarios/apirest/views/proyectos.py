from rest_framework import viewsets
from apirest.models.db_views.proyectos import Proyectos
from apirest.serializers.db_views.proyectos import ProyectoSerializer

class ProyectosViewSet(viewsets.ReadOnlyModelViewSet):

    queryset =  Proyectos.objects.all()
    serializer_class = ProyectoSerializer
    
    def list (self, request, *args, **kwargs):
        """
        Lista todos los proyectos.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un proyecto determinado por su id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)