from rest_framework import serializers
from apirest.models.expedientes.expediente import Expediente
from apirest.serializers.db_views.firmantes import FirmanteSerializer
# from apirest.serializers.db_views.giros import GirosSerializer
from apirest.serializers.giro import GiroSerializer

class ExpedienteSerializer(serializers.ModelSerializer):
    
    firmantes = FirmanteSerializer(many=True)
    #giros = GirosSerializer(many=True)    
    giros = GiroSerializer(many=True)
    
    class Meta:
        model = Expediente
        fields = ('id','codigoexp','codigonum','codigoorigen','codigoanio','sumario','tipocamara','tipo','codigoestado',
                  'fechacaducidad','fecha','periodo','titulo','voces','firmantes','giros')
        
        
        
        
        
# from apirest.serializers.giro import GiroExpedienteSerializer
# from apirest.serializers.expedientes.proyecto import ProyectoChildSerializer
# from apirest.serializers.expedientes.comunicacion_pen import ComunicacionChildPenSerializer
# from apirest.serializers.expedientes.comunicacion import ComunicacionChildSerializer
# from apirest.serializers.expedientes.observacion import ObservacionChildSerializer
# from apirest.serializers.db_views.firmantes import FirmanteSerializer  
#     firmantes = FirmanteSerializer(many=True)
#     giros = GiroExpedienteSerializer(many=True) 
#     
#     tipo_detalles = serializers.SerializerMethodField('get_child')   
#    
#     def get_child(self, Expediente):
#         if hasattr(Expediente, 'proyecto'): return ProyectoChildSerializer(Expediente.proyecto).data
#         elif hasattr(Expediente, 'comunicacionpen'): return ComunicacionChildPenSerializer(Expediente.comunicacionpen).data
#         elif hasattr(Expediente, 'comunicacion'): return ComunicacionChildSerializer(Expediente.comunicacion).data
#         elif hasattr(Expediente, 'observacion'): return ObservacionChildSerializer(Expediente.observacion).data
#         else: None    
#                   'giros',
#                   'tipo_detalles',