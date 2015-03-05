from rest_framework import serializers
from apirest.models.individuos.persona_fisica import PersonaFisica
from apirest.serializers.individuos.persona_fisica_hist import PersonaFisicaHistSerializer
from apirest.serializers.individuos.legislador import LegisladorSerializer
from apirest.serializers.individuos.funcionario import FuncionarioSerializer
import datetime

# class PersonaFisicaActualSerializer(serializers.ModelSerializer):
#     
#     datos_actuales = serializers.SerializerMethodField('get_historico_actual')
#     cargo_actual = serializers.SerializerMethodField('get_cargo_actual')  
#     
#     def get_historico_actual(self, personafisica):
# 
#         historico_flt = personafisica.historial.filter(fhasta__isnull=True)
#         for h in historico_flt:
#             if h:
#                 return PersonaFisicaHistSerializer(h).data
#             else:
#                 return None
# 
#     def get_cargo_actual(self, personafisica):
#         actual_date = datetime.date.today()
# 
#         cargo_actual = None
#         cargos_flt = personafisica.cargo.all()
# 
#         for c in cargos_flt:
#             if c.selector == 'LEGISLADOR' and c.legislador.ffin >= actual_date and c.legislador.fcese >= actual_date:
#                 cargo_actual = LegisladorSerializer(c.legislador).data
#             elif c.selector == 'FUNCIONARIO' and c.funcionario.ffin >= actual_date:
#                 cargo_actual = FuncionarioSerializer(c.funcionario).data
#                              
#         return cargo_actual    
#     
#     class Meta:
#         model = PersonaFisica 
#         fields = ('persona_fisica_id','tipodoc','numerodoc','fechanacimiento','datos_actuales','cargo_actual')
# 
# 
# class PersonaFisicaFullSerializer(serializers.ModelSerializer):
#     
#     historial = PersonaFisicaHistSerializer()
#     cargos = serializers.SerializerMethodField('get_hijo')
# 
#     def get_hijo(self, personafisica):
#         cargos = []
# 
#         for c in personafisica.cargo.all():
#             if c.selector == 'LEGISLADOR':
#                 cargos.append(LegisladorSerializer(c.legislador).data)
#             elif c.selector == 'FUNCIONARIO':
#                 cargos.append(FuncionarioSerializer(c.funcionario).data)
#                              
#         return cargos    
#     
#     class Meta:
#         model = PersonaFisica 
#         fields = ('persona_fisica_id','tipodoc','numerodoc','fechanacimiento','cargos','historial')
#         depth=1
#         
#         

class PersonaFisicaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonaFisica 
#         fields = ('id','tipodoc','numerodoc','fechanacimiento')

        