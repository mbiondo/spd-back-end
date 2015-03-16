from rest_framework import serializers
from apirest.models.db_views.proyectos import Proyectos

class ProyectoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Proyectos
        fields = ('expediente_id','codigoexp','codigonum','codigoorigen','codigoanio','sumario','tipocamara','tipo','fechacaducidad','fecha','periodo','titulo','voces','resultado','tipoproy','nroley')