from rest_framework import serializers
from apirest.models.expedientes.comunicacion import Comunicacion

class ComunicacionSerializer(serializers.ModelSerializer):
        
    proyecto_original_id = serializers.SerializerMethodField()
     
    def get_proyecto_original_id(self, obj):
        result = None
        if obj.resultados_com is not None:
            for resultado in obj.resultados_com.all():
                for proyecto in resultado.resultados.all():
                    result = proyecto.proyecto_id
   
        return result
     
    class Meta:
        model = Comunicacion 
        fields= ('id','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','fecha','periodo','titulo','voces','subtipo','fecha_recepcion','orden','proyecto_original_id')
        
