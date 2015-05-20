from rest_framework import serializers
from apirest.models.publicaciones.orden_dia import OrdenDia

class OrdenDiaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrdenDia
        fields = ('publicacion_id','periodo','fecha_impresion','tipo','visibilidad','despacho','numero','anio','f113')
        
# class OrdenDiaSerializerId(serializers.ModelSerializer):
#     
#     class Meta: 
#         model = OrdenDia
#         fields = ('orden_dia_id')