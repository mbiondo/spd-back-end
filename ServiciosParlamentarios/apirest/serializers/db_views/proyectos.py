from rest_framework import serializers
from apirest.models.db_views.proyectos import Proyectos

class ProyectoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Proyectos
        fields = ('expediente_id','codigo_exp','codigo_num','codigo_origen','codigo_anio','sumario','tipo_camara','tipo','fecha_caducidad','fecha','periodo','titulo','voces','resultado','tipo_proy','nro_ley')  