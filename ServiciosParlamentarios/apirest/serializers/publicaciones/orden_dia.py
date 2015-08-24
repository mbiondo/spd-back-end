from rest_framework import serializers
from apirest.models.publicaciones.orden_dia import OrdenDia

class OrdenDiaSerializer(serializers.ModelSerializer):
    
    periodo = serializers.SerializerMethodField()
    
    def get_periodo(self, obj):
        return obj.periodo.nro_periodo
        
    class Meta:
        model = OrdenDia
        fields = ('id','periodo','fecha_impresion','tipo','visibilidad','despacho','numero','anio','fecha_art113')
        
# class OrdenDiaSerializerId(serializers.ModelSerializer):
#     
#     class Meta: 
#         model = OrdenDia
#         fields = ('orden_dia_id')