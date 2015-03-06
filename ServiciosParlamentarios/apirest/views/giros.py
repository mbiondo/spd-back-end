from rest_framework import viewsets
from apirest.models.db_views.giros import Giros
from apirest.serializers.db_views.giros import GirosSerializer

class GirosViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Giros.objects.all()
    serializer_class = GirosSerializer
                    
    def list(self, request, expediente_pk=None):
        """
        Lista los giros de un expediente determinado.
        """
        self.queryset = self.queryset.filter(expediente_id = expediente_pk)
        
        return viewsets.ReadOnlyModelViewSet.list(self, request, expediente_pk)
    
    def retrieve(self, request, pk=None, expediente_pk=None):        
        """
        Devuelve los datos de un giro para el expediente solicitado.
        """
        self.queryset = self.queryset.filter(giro_id=pk, expediente_id = expediente_pk)
                
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, pk, expediente_pk)