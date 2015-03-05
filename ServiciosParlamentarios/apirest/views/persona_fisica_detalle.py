from rest_framework import viewsets
from apirest.models.db_views.persona_fisica_detalle import PersonaFisicaDetalle
from apirest.serializers.db_views.persona_fisica_detalle import PersonaFisicaDetalleSerializer

class PersonaFisicaDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    model = PersonaFisicaDetalle
    queryset = PersonaFisicaDetalle.objects.all()
    serializer_class = PersonaFisicaDetalleSerializer
                                        
    def list(self, request, *args, **kwargs):
        """
        Lista todas las personas fisicas con sus datos actualizados.
        """        
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve la persona fisica solicitada por id con sus datos actualizados.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)    
