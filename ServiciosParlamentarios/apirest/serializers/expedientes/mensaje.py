from rest_framework import serializers
from apirest.models.expedientes.mensaje import Mensaje
from apirest.serializers.expedientes.expediente import ExpedienteSerializer
from apirest.serializers.db_views.firmantes import FirmanteSerializer
from apirest.serializers.db_views.giros import GirosSerializer

class MensajeSerializer(serializers.ModelSerializer):
    
    #fk_expediente = ExpedienteSerializer()
    codigo_exp = serializers.SerializerMethodField()
    codigo_num = serializers.SerializerMethodField()
    codigo_origen = serializers.SerializerMethodField()
    codigo_anio = serializers.SerializerMethodField()
    sumario = serializers.SerializerMethodField()
    tipo_camara = serializers.SerializerMethodField()
    tipo = serializers.SerializerMethodField()
    codigo_estado = serializers.SerializerMethodField()
    fecha_caducidad = serializers.SerializerMethodField()
    periodo = serializers.SerializerMethodField()
    titulo = serializers.SerializerMethodField()
    voces = serializers.SerializerMethodField()
    giros = serializers.SerializerMethodField()
    firmantes = serializers.SerializerMethodField()


    def get_codigo_exp(self, obj):
    	return obj.fk_expediente.codigo_exp

    def get_codigo_num(self, obj):
    	return obj.fk_expediente.codigo_num

    def get_codigo_origen(self, obj):
    	return obj.fk_expediente.codigo_origen

    def get_codigo_anio(self, obj):
    	return obj.fk_expediente.codigo_anio

    def get_sumario(self, obj):
    	return obj.fk_expediente.sumario

    def get_tipo_camara(self, obj):
    	return obj.fk_expediente.tipo_camara

    def get_tipo(self, obj):
    	return obj.fk_expediente.tipo

    def get_codigo_estado(self, obj):
    	return obj.fk_expediente.codigo_estado

    def get_fecha_caducidad(self, obj):
    	return obj.fk_expediente.fecha_caducidad

    def get_periodo(self, obj):
    	return obj.fk_expediente.periodo  

    def get_titulo(self, obj):
    	return obj.fk_expediente.titulo  

    def get_voces(self, obj):
    	return obj.fk_expediente.voces      

    def get_giros(self, obj):
    	giros = GirosSerializer(obj.fk_expediente.giros, many=True)
    	return giros.data

    def get_firmantes(self, obj):
    	firmantes = FirmanteSerializer(obj.fk_expediente.firmantes, many=True)    	
    	return firmantes.data

    class Meta:
        model = Mensaje
        fields = ('id', 'num','anio','fecha', 'codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','codigo_estado',
                  'fecha_caducidad','periodo','titulo','voces', 'giros', 'firmantes')
