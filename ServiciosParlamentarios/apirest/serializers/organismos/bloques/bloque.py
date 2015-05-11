from rest_framework import serializers
from apirest.models.organismos.bloques.bloque import Bloque
from datetime import datetime
from django.db.models import Q
from apirest.models.db_views.bloque_detalle import BloqueDetalle
from apirest.serializers.db_views.bloque_detalle import BloqueDetalleSerializer

class BloqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bloque
#         fields = ('id','nombre','nrointegrantes','finicio','ffin','tipocamara','nota','sigla')


class BloqueIntegrantesSerializer(serializers.ModelSerializer):      
    
    date = None 
    integrantes = serializers.SerializerMethodField('get_bloque_estructura_serializer')
    
    id =  serializers.SerializerMethodField('get_name_id')    
    def get_name_id(self, obj):
        return obj.entidad_id
    
    def get_bloque_estructura_serializer(self, bloque):
        
        if self.date is not None:
            filtered_qs = BloqueDetalle.objects.filter(id=bloque.id).filter(Q(fdesde__lte=self.date), Q(fhasta__isnull=True) | Q(fhasta__gt=self.date))
        else:    
            filtered_qs = BloqueDetalle.objects.filter(id=bloque.id)        
             
        serializer = BloqueDetalleSerializer(filtered_qs, many=True)

        return serializer.data
    
    def __init__(self, *args, **kwargs):
        
        super(BloqueIntegrantesSerializer, self).__init__(*args, **kwargs)
          
        try:
            self.date = datetime.strptime(kwargs['context']['request'].QUERY_PARAMS['fecha'], '%Y-%m-%d')
        except:
            pass         
    
    class Meta:
        model = Bloque
        fields = ('id','nombre','nro_integrantes','fecha_inicio','fecha_fin','tipo_camara','nota','sigla','integrantes')