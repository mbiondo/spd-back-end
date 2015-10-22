from rest_framework import serializers
from apirest.models.expedientes.comunicacion import Comunicacion
from apirest.serializers.expedientes.resultado import ResultadoComunicacionSerializer

class ComunicacionSerializer(serializers.ModelSerializer):
    
    resultados_com = ResultadoComunicacionSerializer(many=True)
    
#     resultados_com = serializers.SerializerMethodField()
#     
#     def get_resultados_com(self, obj):
#         result = None
#         if obj.resultados_com is not None:
#             obj.resultados_com = ResultadoComunicacionSerializer( many=True)
#             result = obj.resultados_com 
#         
#         return result
        
    class Meta:
        model = Comunicacion 
        fields= ('id','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','fecha','periodo','titulo','voces','subtipo','fecha_recepcion','orden','resultados_com')
        
