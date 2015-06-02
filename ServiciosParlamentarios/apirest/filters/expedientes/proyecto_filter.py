from rest_framework.compat import django_filters
from apirest.models.expedientes.proyecto import Proyecto
from apirest.filters.custom_filter_list import CustomFilterList
from apirest.filters.expedientes.expediente_filter import ExpedienteFilter

class ProyectoFilter(ExpedienteFilter):
    
    codigo_digesto = django_filters.CharFilter(lookup_type='icontains',name="codigo_digesto")
    proyecto_reproduce = django_filters.NumberFilter(name="fk_proyecto_reproduce")
    estado = django_filters.CharFilter(lookup_type='icontains',name="estado")
    tipo_proy = django_filters.CharFilter(lookup_type='icontains',name="tipo_proy")
    subtipo_proy = django_filters.CharFilter(lookup_type='icontains',name="subtipo_proy")

    # Orden del dia filter
    od_numero = django_filters.NumberFilter(name="despachos__ordenes_del_dia__numero")
    od_anio = django_filters.NumberFilter(name="despachos__ordenes_del_dia__anio")  
    
    # Resultado filters
    nro_ley = django_filters.CharFilter(name="resultados__sanciones__nro_ley")
    resultado = CustomFilterList(name="resultados__resultado", lookup_type="in")  
    
    # Despacho filters
    dictamen_camara = django_filters.CharFilter(lookup_type='icontains',name="despachos__tipo_camara")
    
    # Giro filters
    giro_comision_id = django_filters.CharFilter(name="giros__comision_id")
    giro_comision_nombre = django_filters.CharFilter(name="giros__comision_nombre")
    giro_comision_nombre_corto = django_filters.CharFilter(name="giros__comision_nombre_corto")

    # Firmantes filters
    firm_persona_fisica_id = django_filters.CharFilter(name="firmantes__persona_fisica_id")
    firm_orden = django_filters.CharFilter(name="firmantes__orden")
    firm_cargo = django_filters.CharFilter(name="firmantes__cargo")
    firm_cargo_tipo = django_filters.CharFilter(name="firmantes__cargo_tipo")
    firm_nombre_leg_func = django_filters.CharFilter(name="firmantes__nombre_leg_func")
    
    class Meta:
        model = Proyecto
        fields = ['codigo_digesto','proyecto_reproduce','estado','tipo_proy','subtipo_proy','od_numero','od_anio'
                ,'nro_ley','resultado','dictamen_camara','giro_comision_id','giro_comision_nombre','giro_comision_nombre_corto'
                ,'firm_persona_fisica_id','firm_orden','firm_cargo','firm_cargo_tipo','firm_nombre_leg_func'] 
        order_by = True
