from rest_framework import serializers
from apirest.models.organismos.bloques.bloque import Bloque
from datetime import datetime
from django.db.models import Q
# from apirest.serializers.organismos.bloques.bloque_estructura import BloqueEstructuraSerializer
# from apirest.models.db_views.bloque_detalle import BloqueDetalle
# from apirest.serializers.db_views.bloque_detalle import BloqueDetalleSerializer
from datetime import date

class BloqueSerializer(serializers.ModelSerializer):

    legisladores = serializers.SerializerMethodField()    
    
    def get_legisladores(self, obj):
        return obj.legisladores.filter(Q(fecha_hasta__gte=date.today()) | Q(fecha_hasta__isnull=True)).values_list('id', flat=True)
    
    class Meta: 
        model = Bloque
        fields = ('id','nombre','nro_integrantes','fecha_inicio','fecha_fin','tipo_camara','nota','sigla','legisladores','legisladores_historico')

# class BloqueIntegrantesSerializer(serializers.ModelSerializer):      
#     
#     date = None 
#     integrantes = serializers.SerializerMethodField('get_bloque_estructura_serializer')
#     
#     id =  serializers.SerializerMethodField('get_name_id')    
#     def get_name_id(self, obj):
#         return obj.entidad_id
#     
#     def get_bloque_estructura_serializer(self, bloque):
#         
#         if self.date is not None:
#             filtered_qs = BloqueDetalle.objects.filter(id=bloque.id).filter(Q(fdesde__lte=self.date), Q(fhasta__isnull=True) | Q(fhasta__gt=self.date))
#         else:    
#             filtered_qs = BloqueDetalle.objects.filter(id=bloque.id)        
#              
#         serializer = BloqueDetalleSerializer(filtered_qs, many=True)
# 
#         return serializer.data
#     
#     def __init__(self, *args, **kwargs):
#         
#         super(BloqueIntegrantesSerializer, self).__init__(*args, **kwargs)
#           
#         try:
#             self.date = datetime.strptime(kwargs['context']['request'].QUERY_PARAMS['fecha'], '%Y-%m-%d')
#         except:
#             pass         
#     
#     class Meta:
#         model = Bloque
#         fields = ('id','nombre','nro_integrantes','fecha_inicio','fecha_fin','tipo_camara','nota','sigla','integrantes')