from rest_framework import serializers
from apirest.models.individuos.legislador import Legislador
# from apirest.serializers.cargos.cargo_persona_fisica import CargoPersonaFisicaSerializer
# from apirest.models.cargos.cargo_persona_fisica import CargoPersonaFisica
# from apirest.models.organismos.comisiones.com_estructura import ComEstructura
#     
# from apirest.serializers.organismos.comisiones.com_estructura import ComEstructuraSerializer


class LegisladorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Legislador
        fields = ['id','cargo','distrito','fecha_incorporacion','fecha_cese','fecha_inicio','fecha_fin','nota',
                  'matricula','partido','fk_persona_fisica']         
          
                  
# class LegisladorCargoSerializer(serializers.ModelSerializer):
#     
#     cargo_persona_fisica = serializers.SerializerMethodField('get_comision_estructura_serializer') 
#     
#     class Meta:
#         model = Legislador
#         fields = ('cargo_persona_fisica', 'cargo','distrito','fincorporacion','fcese','finicio','ffin','nota','matricula','partido')
# 
#     def get_comision_estructura_serializer(self, legislador):
#         
#         cargo_persona_fisica = CargoPersonaFisica.objects.get(cargo_persona_fisica_id=legislador.legislador_id)
#         serializer = CargoPersonaFisicaSerializer(cargo_persona_fisica)
# 
#         return serializer.data
#     
# class LegisladorComisionSerializer(serializers.ModelSerializer):
#     
#     cargo_persona_fisica = serializers.SerializerMethodField('get_cargo_persona_fisica') 
#     comisiones = serializers.SerializerMethodField('get_comision_estructura_serializer')
#     
#     def get_cargo_persona_fisica(self, legislador):
#         
#         cargo_persona_fisica = CargoPersonaFisica.objects.get(cargo_persona_fisica_id=legislador.legislador_id)
#         serializer = CargoPersonaFisicaSerializer(cargo_persona_fisica)
# 
#         return serializer.data
# 
#     def get_comision_estructura_serializer(self, legislador):
#         
#         estructuras_comision = ComEstructura.objects.filter(fk_legislador=legislador.legislador_id)
#         serializer = ComEstructuraSerializer(estructuras_comision)
#         
#         return serializer.data
# 
#     class Meta:
#         model = Legislador
#         fields = ('cargo_persona_fisica', 'comisiones', 'cargo','distrito','fincorporacion','fcese','finicio','ffin','nota','matricula','partido')
#         
#         
#         
#         
#         