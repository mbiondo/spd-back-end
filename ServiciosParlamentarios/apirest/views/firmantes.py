from rest_framework import viewsets
from apirest.models.db_views.firmantes import Firmantes
from apirest.serializers.db_views.firmantes import FirmanteSerializer

class FirmantesViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Firmantes.objects.all()
    serializer_class = FirmanteSerializer
                    
    def list(self, request, expediente_pk=None):
        """
        Lista los firmantes de un expediente determinado.
        """
        self.queryset = self.queryset.filter(expediente_id = expediente_pk)
        
        return viewsets.ReadOnlyModelViewSet.list(self, request, expediente_pk)
    
    def retrieve(self, request, pk=None, expediente_pk=None):        
        """
        Devuelve los datos de un firmante para el expediente solicitado.
        """
        self.queryset = self.queryset.filter(persona_fisica_id=pk, expediente_id = expediente_pk)
                
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, pk, expediente_pk)