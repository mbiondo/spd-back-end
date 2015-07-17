from rest_framework import viewsets
from apirest.models.relaciones.plp_detalle_estructura import PlpDetalleEstructura
from apirest.serializers.plp_detalle_estructura import PlpDetalleEstructuraSerializer
from apirest.authorizers.authorizator import has_permission

class PlpDetalleEstructuraViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset =  PlpDetalleEstructura.objects.all()
    serializer_class = PlpDetalleEstructuraSerializer
#     filter_class = 

    @has_permission        
    def list (self, request, *args, **kwargs):
        """
        Lista todas los planes de labor.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    @has_permission
    def retrieve (self, request, *args, **kwargs):
        """
        Devuelve un plan de labor por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    