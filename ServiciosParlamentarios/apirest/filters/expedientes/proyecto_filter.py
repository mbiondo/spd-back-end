from rest_framework.compat import django_filters
from apirest.models.expedientes.proyecto import Proyecto
from apirest.filters.custom_filter_list import CustomFilterList

class ProyectoFilter(django_filters.FilterSet):
    
    id = CustomFilterList(name="id", lookup_type="in")
    tipo = django_filters.CharFilter(lookup_type='icontains',name="tipo")
    codigo_origen = django_filters.CharFilter(lookup_type='icontains',name="codigo_origen")
    tipo_camara = django_filters.CharFilter(lookup_type='icontains',name="tipo_camara")
    codigo_exp = django_filters.CharFilter(lookup_type='icontains',name="codigo_exp")
    codigo_num = django_filters.CharFilter(lookup_type='icontains',name="codigo_num")
    codigo_anio = django_filters.CharFilter(lookup_type='icontains',name="codigo_anio")
    fecha_desde = django_filters.DateFilter(name="fecha", lookup_type='gte')
    fecha_hasta = django_filters.DateFilter(name="fecha", lookup_type='lte')
    
    codigo_digesto = django_filters.CharFilter(lookup_type='icontains',name="codigo_digesto")
    proyecto_reproduce = django_filters.NumberFilter(name="fk_proyecto_reproduce")
    estado = django_filters.CharFilter(lookup_type='icontains',name="estado")
    tipo_proy = django_filters.CharFilter(lookup_type='icontains',name="tipo_proy")
    subtipo_proy = django_filters.CharFilter(lookup_type='icontains',name="subtipo_proy")
    codigo_anio = django_filters.CharFilter(lookup_type='icontains',name="codigo_anio")

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
        fields = ['id','fk_proyecto_reproduce','estado','tipo_proy','subtipo_proy','codigo_digesto','codigo_exp','codigo_num','codigo_anio'
                ,'codigo_origen','tipo_camara','tipo','fecha_caducidad','fecha_desde','fecha_hasta','periodo','od_numero','od_anio','nro_ley','resultado'
                ,'dictamen_camara','giro_comision_id','giro_comision_nombre','giro_comision_nombre_corto','firm_persona_fisica_id'
                ,'firm_orden','firm_cargo','firm_cargo_tipo','firm_nombre_leg_func'] 
        order_by = True