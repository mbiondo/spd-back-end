from rest_framework import serializers
from apirest.models.organismos.comisiones.comision import Comision
from apirest.serializers.organismos.comisiones.comision_hist import ComisionHistSerializer


class ComisionSerializer(serializers.ModelSerializer):
        
    comision_hist = ComisionHistSerializer(many=True)
    
    class Meta:
        model = Comision
        fields = ( 'id','caracter','tipocamara','finicio','ffin','sigla','normacreacion', 'comision_hist')


class ComisionChildSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Comision
        fields = ( 'id','caracter','tipocamara','finicio','ffin','sigla','normacreacion')
        
        
class ComisionExpedienteSerializer(serializers.ModelSerializer):
    
    nombre = serializers.SerializerMethodField('get_nombre_comision')
    
    def get_nombre_comision(self, comision):
        #El ultimo historico tiene fecha hasta null
        historico_flt = comision.comision_hist.filter(fhasta__isnull=True)
        for h in historico_flt:
            if h:
                return ComisionHistSerializer(h).data['nombre']
            else:
                return None
    
    class Meta:
        model = Comision
        fields = ('id', 'caracter', 'tipocamara', 'finicio', 'ffin', 'sigla', 'normacreacion', 'nombre')
           
class ComisionExpedienteIdSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Comision
        fields = ('id',)

# class ComisionSerializer(serializers.ModelSerializer):
#     
#     class Meta:
#         model = Comision
#         fields = ('id','caracter','tipocamara','finicio','ffin','sigla','normacreacion')
        
# class ComisionIntegrantesSerializer(serializers.ModelSerializer):
#     
#     date = None
#     integrantes = serializers.SerializerMethodField('get_comision_estructura')
#     
#     def get_comision_estructura(self, comision):
#         
#         if self.date is not None:
#             filtered_qs = ComisionesDetalle.objects.filter(id=comision.id).filter(Q(fdesde__lte=self.date), Q(fhasta__isnull=True) | Q(fhasta__gt=self.date))
#         else:    
#             filtered_qs = ComisionesDetalle.objects.filter(id=comision.id)        
#              
#         serializer = ComisionesDetalleSerializer(filtered_qs, many=True)
# 
#         return serializer.data    
# 
#     def __init__(self, *args, **kwargs):
#         
#         super(ComisionIntegrantesSerializer, self).__init__(*args, **kwargs)
#           
#         try:
#             self.date = datetime.strptime(kwargs['context']['request'].QUERY_PARAMS['fecha'], '%Y-%m-%d')
#         except:
#             pass      
#     
#     class Meta:
#         model = ComisionesDetalle
#         fields = ('id','nombre_comision','nombre_corto','caracter','tipocamara','finicio','ffin','sigla','normacreacion', 'integrantes')

