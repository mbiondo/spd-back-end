from rest_framework import serializers
from apirest.models.organismos.despacho import Despacho
from apirest.serializers.publicaciones.orden_dia import OrdenDiaSerializer

class DespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Despacho
        fields = ('id','numero','anio','tipo_camara','sumario','art108par2','tipo','fecha_caducidad','visibilidad',
                  'visibilidad','unanimidad','tramite_especial','modificaciones','texto_legado','dictamenes','ordenes_del_dia','proyectos')
