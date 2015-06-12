from rest_framework import viewsets
from apirest.models.db_views.giros import Giros
from apirest.serializers.db_views.giros import GirosSerializer
from apirest.filters.giro_filter import GiroFilter

class GirosViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Giros.objects.all()
    serializer_class = GirosSerializer
    filter_class = GiroFilter
                    
    def list(self, request, proyectos_pk=None):
        """
        Lista los giros de un expediente determinado.
        """
        self.queryset = self.queryset.filter(proyecto_id = proyectos_pk)
        
        return viewsets.ReadOnlyModelViewSet.list(self, request, proyectos_pk)
    
    def retrieve(self, request, pk=None, proyectos_pk=None):        
        """
        Devuelve los datos de un giro para el expediente solicitado.
        """
        self.queryset = self.queryset.filter(id=pk, proyecto_id = proyectos_pk)
                
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, pk, proyectos_pk)