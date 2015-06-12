from rest_framework import serializers
from apirest.models.expedientes.proyecto import Proyecto
from apirest.serializers.db_views.firmantes import FirmanteSerializer

class ProyectoSerializer(serializers.ModelSerializer):
    
    firmantes = FirmanteSerializer(many=True)
    
    class Meta:
        model = Proyecto
        fields = ('id','fk_proyecto_reproduce','estado','tipo_proy','subtipo_proy','codigo_digesto','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                 'fecha_caducidad','fecha','periodo','titulo','voces','resultados','despachos','firmantes','giros')
        
        
class ProyectoChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Proyecto 
#         fields = ('id','estado','tipoproy','subtipoproy','codigodigesto')  