from rest_framework import serializers
from apirest.models.organismos.despacho import Despacho
from apirest.serializers.publicaciones.orden_dia import OrdenDiaSerializer

class DespachoSerializer(serializers.ModelSerializer):
    proyectos = serializers.SerializerMethodField()
    mensajes = serializers.SerializerMethodField()

    def get_proyectos(self, obj):
        return obj.proyectos.values_list('id', flat=True)

    def get_mensajes(self, obj):
        return obj.mensajes.values_list('id', flat=True)       

    class Meta:
        model = Despacho
        fields = ('id','numero','anio','tipo_camara','sumario','art108par2','tipo','fecha_caducidad','visibilidad',
                  'visibilidad','unanimidad','tramite_especial','modificaciones','texto_legado','dictamenes','ordenes_del_dia', 'proyectos', 'mensajes')
