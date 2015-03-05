from rest_framework import viewsets
from apirest.models.individuos.persona_fisica import PersonaFisica
# from apirest.serializers.individuos.persona_fisica import PersonaFisicaFullSerializer,\
#     PersonaFisicaActualSerializer
from apirest.serializers.individuos.persona_fisica import PersonaFisicaSerializer     
# from apirest.filters.persona_fisica_filter import PersonaFisicaFilter
# from django.db.models import Q
# import datetime

class PersonaFisicaViewSet(viewsets.ReadOnlyModelViewSet):
    
    model = PersonaFisica
    queryset = PersonaFisica.objects.all()
    serializer_class = PersonaFisicaSerializer
    
    def list(self, request, *args, **kwargs):
        """
        Lista todas las personas fisicas.
        """
        return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Devuelve la persona fisica solicitada por id.
        """
        return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)    

# class PersonaFisicaActualViewSet(viewsets.ReadOnlyModelViewSet):
#   
#     model = PersonaFisica
#     serializer_class = PersonaFisicaActualSerializer
#     filter_class = PersonaFisicaFilter
#     search_fields = ('numerodoc','fechanacimiento','historial__nombre','historial__apellido')
#     
#     def get_queryset(self):
#         actual_date = datetime.date.today()
#         
#         queryset1 = PersonaFisica.objects.filter( Q(cargo__legislador__ffin__gte=actual_date) &
#                                                   Q(cargo__legislador__fcese__gte=actual_date) | 
#                                                   Q(cargo__funcionario__ffin__gte=actual_date) ).distinct('id') #entidad_id
#         
#         return queryset1
# 
#     
#     def list(self, request, *args, **kwargs):
#         """
#         Lista todas las personas fisicas que tienen cargos actuales.
#         \n
#         Filtros posible:
#         -cargo=[diputado, senador, presidente, ministro..]
#         Campos de busqueda posibles:
#         -numerodoc
#         -fechanacimiento
#         -historial__nombre
#         -historial__apellido
#         """
#         return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
#     
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Devuelve la persona fisica solicitada con sus datos actuales.
#         """
#         return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)


# class PersonaFisicaFullViewSet(viewsets.ReadOnlyModelViewSet):
#   
#     queryset = PersonaFisica.objects.all()
#     serializer_class = PersonaFisicaFullSerializer
# #     filter_fields = ('numerodoc','fechanacimiento','historial__nombre','historial__apellido','historial__genero')
#     search_fields = ('numerodoc','fechanacimiento','historial__nombre','historial__apellido')
#     
#     def list(self, request, *args, **kwargs):
#         """
#         Lista todas las personas fisicas ordenados por id. 
#         \n
#         Campos de busqueda posibles:
#         -numerodoc
#         -fechanacimiento
#         -historial__nombre
#         -historial__apellido       
#         """
#         return viewsets.ReadOnlyModelViewSet.list(self, request, *args, **kwargs)
#     
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Devuelve la persona fisica solicitada por id.
#         """
#         return viewsets.ReadOnlyModelViewSet.retrieve(self, request, *args, **kwargs)
