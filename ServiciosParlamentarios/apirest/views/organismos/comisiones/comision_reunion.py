from rest_framework import viewsets 
from apirest.models.organismos.comisiones.comision_reunion import ComisionReunion 
from apirest.serializers.organismos.comisiones.comision_reunion import ComisionReunionSerializer 
from apirest.authorizers.authorizator import has_permission

class ComisionReunionViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = ComisionReunion.objects.all()
    serializer_class = ComisionReunionSerializer
#     filter_class = ComisionFilter
    
    @has_permission         
    def list(self, request, *args, **kwargs):
        """
        Lista todas los partes ordenados por id.        
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    @has_permission         
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve un parte por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    