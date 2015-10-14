from rest_framework import serializers
from apirest.models.publicaciones.orden_dia import OrdenDia

class OrdenDiaSerializer(serializers.ModelSerializer):
    
    proyectos = serializers.SerializerMethodField()
    periodo = serializers.SerializerMethodField()    

    def get_periodo(self, obj):
        if(obj.periodo is not None):
            return obj.periodo.nro_periodo
        else:
            return None
    
    def get_proyectos(self, obj):
        return obj.despacho.proyectos.values_list('id', flat=True)
        
    class Meta:
        model = OrdenDia
        fields = ('id','periodo','fecha_impresion','tipo','visibilidad','despacho','numero','anio','fecha_art113','proyectos')
        
# class OrdenDiaSerializerId(serializers.ModelSerializer):
#     
#     class Meta: 
#         model = OrdenDia
#         fields = ('orden_dia_id')