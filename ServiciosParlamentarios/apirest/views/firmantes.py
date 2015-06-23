from rest_framework import viewsets
from apirest.serializers.db_views.firmantes import FirmanteFullSerializer
from apirest.models.db_views.firmantes import Firmantes

class FirmantesViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Firmantes.objects.all()
    serializer_class = FirmanteFullSerializer
    ordering_fields = '__all__'
    search_fields = ()
             
    def list(self, request, proyectos_pk=None):
        """
        Lista los firmantes de un expediente determinado.
        """
        self.queryset = self.queryset.filter(proyecto_id = proyectos_pk)
         
        return viewsets.ReadOnlyModelViewSet.list(self, request, proyectos_pk)
     
    def retrieve(self, request, pk=None, proyectos_pk=None):        
        """
        Devuelve los datos de un firmante para el expediente solicitado.
        """
        self.queryset = self.queryset.filter(id=pk, proyecto_id = proyectos_pk)
        
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, pk, proyectos_pk)
    