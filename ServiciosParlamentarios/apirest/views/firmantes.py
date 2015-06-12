from rest_framework import viewsets
# from apirest.models.db_views.firmantes import Firmantes
from apirest.serializers.db_views.firmantes import FirmanteSerializer
from apirest.models.db_views.firmantes import Firmantes

class FirmantesViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = Firmantes.objects.all()
    ordering_fields = '__all__'
    search_fields = ()
             
    def list(self, request, proyectos_pk=None):
        """
        Lista los firmantes de un expediente determinado.
        """
        self.queryset = self.queryset.filter(expediente = proyectos_pk)
         
        return viewsets.ReadOnlyModelViewSet.list(self, request, proyectos_pk)
     
    def retrieve(self, request, pk=None, proyectos_pk=None):        
        """
        Devuelve los datos de un firmante para el expediente solicitado.
        """
        self.queryset = self.queryset.filter(id=pk, expediente = proyectos_pk)
                  
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, pk, proyectos_pk)
    
            
    
#     def list(self, request, *args, **kwargs):
#         """
#         Lista todos los firmantes
#         """
#         return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
#     
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Devuelve un firmante por id.
#         """
#         return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)