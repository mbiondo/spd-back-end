from rest_framework import viewsets
from apirest.models.organismos.comisiones.comision import Comision
from apirest.serializers.organismos.comisiones.comision import ComisionSerializer#,\
from apirest.filters.organismos.comisiones.comision_filter import ComisionFilter
       
class ComisionViewSet(viewsets.ReadOnlyModelViewSet):
  
    queryset = Comision.objects.all()
    serializer_class = ComisionSerializer
    filter_class = ComisionFilter
    
    def list(self, request, *args, **kwargs):
        """
        Lista todas las comisiones ordenados por id.        
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve la comision solicitada por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    
    
# class ComisionHistoricoViewSet(viewsets.ReadOnlyModelViewSet):
#   
#     queryset = Comision.objects.all()
#     serializer_class = ComisionHistoricoSerializer
#     
#     def list(self, request, *args, **kwargs):
#         """
#         Lista todas las comisiones ordenados por id.        
#         """
#         return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
#     
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Devuelve la comision solicitada por id.
#         """
#         return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
    

# class ComisionDetalleViewSet(viewsets.ReadOnlyModelViewSet):
#   
#     queryset = ComisionesDetalle.objects.distinct('comision_id')
#     serializer_class = ComisionIntegrantesSerializer
#     filter_class = ComisionDetalleFilter
# 
#     def list(self, request, *args, **kwargs):
#         """
#         Lista todas las comisiones ordenados por id.
#         \n
#         Filtros posible:
#         -fecha=[AAAA-MM-DD]
#         -nombre=[Nombre Comision]
#         -nombre_legislador=[Nombre o apellido del legislador]
#         -tipo_camapara=[D,S]
#         -caracter=[P,E]
#         """
#         return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
#     
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Devuelve la comision solicitada por id.
#         """
#         return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
