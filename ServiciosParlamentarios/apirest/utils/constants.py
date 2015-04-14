from apirest.utils.utils import singleton
from ServiciosParlamentarios import settings

@singleton
class Constants():
    
    #### TABLE NAME ####    
    ACUERDO = 'acuerdo'
    APROBACION_SIMPLE = 'aprobacion_simple'
    BAE = 'bae'
    BAT_BN = 'bat_bn'
    BLOQUE = 'bloque'
    BLOQUE_ESTRUCTURA = 'bloque_estructura'
    BLOQUE_DETALLE = 'bloque_detalle'
    BLQ_INTERBLOQUE = 'blq_interblq'
    CADUCIDAD_HIST = 'caducidad_hist'
    CAMARA = 'camara'
    CAMARA_AUTORIDAD = 'camara_autoridad'
    CAMARA_PRODUCE_DESPACHO = 'camara_produce_despacho'
    CAMARA_REUNION = 'camara_reunion'
    CARGO = 'cargo'
    CARGO_PERSONA_FISICA = 'cargo_persona_fisica'
    CARGO_PERSONA_FISICA_FIRMA_EXPEDIENTE = 'cargo_persona_fisica_firma_expediente'
    CITACION = 'citacion'
    CITACION_COMISION = 'citacion_comision'
    CITACION_CONTIENE_EXPEDIENTE = 'citacion_contiene_expediente'
    CITACION_INVITA_ENTIDAD = 'citacion_invita_entidad'
    CITACION_TEMARIO = 'citacion_temario'
    COMISION_ESTRUCTURA = 'com_estructura'
    COMISION = 'comision'
    COMISION_COMISION_REUNION = 'comision_comision_reunion'
    COMISION_COMUNICACION = 'comision_comunicacion'
    COMISION_REUNION = 'comision_reunion'
    COMISION_SUCEDE_COMISION = 'comision_sucede_comision'
    COMISIONES_DETALLE = 'comisiones_detalle'
    COMISION_HIST = 'comision_hist'
    COMUNICACION = 'comunicacion'
    COMUNICACION_ENTIDAD = 'comunicacion_entidad'
    COMUNICACION_DESPACHO = 'comunicacion_despacho'
    COMUNICACION_LEG = 'comunicacion_leg'
    COMUNICACION_PEN = 'comunicacion_pen'
    COMUNICACION_RESULTADO = 'comunicacion_resultado'
    DEBATE = 'debate'
    DEBATE_DESPACHO = 'debate_despacho'
    DEBATE_SOBRE_ITEM_PLP = 'debate_sobre_item_plp'
    DEBATE_SOBRE_EXPEDIENTE = 'debate_sobre_expediente'
    DEPENDENCIA = 'dependencia'
    DESPACHO = 'despacho'
    DIARIO_SESION = 'diario_sesion'
    DICTAMEN = 'dictamen'
    DICTAMENES = 'dictamenes'
    ENTIDAD = 'entidad'
    ENTIDAD_CELEBRA_EVENTO = 'entidad_celebra_evento'
    ENTIDAD_CITA_EVENTO = 'entidad_cita_evento'
    ENTIDAD_COMISION_REUNION = 'entidad_comision_reunion'
    ENTIDAD_PARTICIPA_EVENTO_REUNION = 'entidad_participa_evento_reunion'
    ENTIDAD_PRODUCE_EXPEDIENTE = 'entidad_produce_expediente'
    ESTADO = 'estado'
    EVENTO = 'evento'
    EVENTO_REUNION = 'evento_reunion'
    EXPEDIENTE = 'expediente'
    EXPEDIENTE_INCLUIDO_PLP = 'expediente_incluido_plp'
    EXPEDIENTE_GIRADO_CAMARA  = 'expediente_girado_camara'
    EXPEDIENTE_GIRADO_PRESIDENCIA_CAMARA = 'expediente_girado_presidencia_camara'
    EXPEDIENTE_ORIGINA_DESPACHO = 'expediente_origina_despacho'
    EXPEDIENTE_REFERIDO_EXPEDIENTE = 'expediente_referido_expediente'
    EXPEDIENTE_TENIDO_VISTA = 'expediente_tenido_vista'
    EXPEDIENTE_TRAMITACION = 'expediente_tramitacion'
    EXTRAORDINARIA = 'extraordinaria'
    FE_ERRATA = 'fe_errata'
    FIRMANTES = 'firmantes'
    FUNCIONARIO = 'funcionario'
    FUNCIONARIO_CAMARA_REUNION = 'funcionario_camara_reunion'
    GIRO = 'giro'
    GIROS = 'giros'
    INSISTENCIA = 'insistencia'
    INTERBLOQUE = 'interbloque'
    LEGISLADOR = 'legislador'
    LEGISLADOR_CAMARA_REUNION = 'legislador_camara_reunion'
    LEGISLADOR_COMISION_REUNION = 'legislador_comision_reunion'
    LEGISLADORES_DETALLE = 'legisladores_detalle'
    LEGISLADOR_EJERCE_PRESIDENCIA_CAMARA = 'legislador_ejerce_presidencia_camara'
    LEGISLADOR_FIRMA_DICTAMEN = 'legislador_firma_dictamen'
    LEGISLADOR_FIRMA_OBSERVACION = 'legislador_firma_observacion'
    LEGISLADOR_INCLUIDO_JURAS = 'legislador_incluido_juras'
    LEGISLADOR_JURA_CAMARA_REUNION = 'legislador_jura_camara_reunion'
    LEGISLADOR_PRESIDE_INTERBLOQUE = 'legislador_preside_interbloque'
    LEGISLADOR_PRODUCE_COMUNICACION_LEG = 'legislador_produce_comunicacion_leg'
    LEGISLADOR_REALIZA_MOCION = 'legislador_realiza_mocion'
    LEGISLADOR_REEMPLAZA_LEGISLADOR = 'legislador_reemplaza_legislador'
    LEGISLADOR_VOTACION = 'legislador_votacion'
    LICENCIA = 'licencia'
    MEDIA_SANCION = 'media_sancion'
    MENSAJE = 'mensaje'
    MOCION = 'mocion'
    MOCION_CAMARA_REUNION = 'mocion_camara_reunion'
    MOCION_EXPEDIENTE = 'mocion_expediente'
    MOCION_RECONSIDERA_VOTACION = 'mocion_reconsidera_votacion'
    MOCION_REFERIDA_ITEM_PLP = 'mocion_referida_item_plp'
    MOCION_SOBRE_DESPACHO = 'mocion_sobre_despacho'
    NORMA = 'norma'
    OBSERVACION = 'observacion'
    ORDEN_DIA = 'orden_dia'
    ORG_PUB = 'org_pub'
    PERIODO = 'periodo'
    PERSONA_FISICA = 'persona_fisica'
    PERSONA_FISICA_DETALLE = 'persona_fisica_detalle'
    PERSONA_FISICA_HIST = 'persona_fisica_hist'
    PLAN_LABOR = 'plan_labor'
    PLANTEAMIENTO = 'planteamiento'
    PLANTEAMIENTO_COMO_EXPEDIENTE = 'planteamiento_como_expediente'
    PLANTEAMIENTO_LEGISLADOR = 'planteamiento_legislador'
    PLANTEAMIENTO_REFERIDO_EXPEDIENTE = 'planteamiento_referido_expediente'
    PLANTEAMIENTO_SOBRE_DEBATE = 'planteamiento_sobre_debate'
    PLP_DETALLE_ESTRUCTURA = 'plp_detalle_estructura'
    PLP_DETALLE_ESTRUCTURA_INCLUYE_BAE = 'plp_detalle_estructura_incluye_bae'
    PLP_ESTRUCTURA = 'plp_estructura'
    PLP_INCLUIDO_DESPACHO = 'plp_incluido_despacho'
    PRESIDENCIA_CAMARA = 'presidencia_camara'
    PRESIDENCIA_CAMARA_PRODUCE_EXPEDIENTE = 'presidencia_camara_produce_expediente'
    PROPUESTA = 'propuesta'
    PROYECTO = 'proyecto'
    PROYECTOS = 'proyectos'
    PUBLICACION = 'publicacion'
    PUBLICACION_DETALLE_ESTRUCTURA = 'publicacion_detalle_estructura'
    PUBLICACION_ESTRUCTURA = 'publicacion_estructura'
    RECHAZO = 'rechazo'
    RESULTADO = 'resultado'
    RESULTADO_GIRO = 'resultado_girado'
    RESULTADO_PUB_DETALLE_ESTRUCTURA = 'resultado_pub_detalle_estructura'
    RESULTADO_SOBRE_DESPACHO = 'resultado_sobre_despacho'
    RESULTADO_SOBRE_EXPEDIENTE = 'resultado_sobre_expediente'
    RP_DP = 'rp_dp'
    RP_DP_GIRO = 'rp_dp_giro'
    SANCION = 'sancion'
    SESION = 'sesion'
    SOLICITUD = 'solicitud'
    SOLICITUD_REFERIDA_EXPEDIENTE = 'solicitud_referida_expediente'
    SOLICITUD_REPRODUCE_PROYECTO = 'solicitud_reproduce_proyecto'
    SUPLEMENTO = 'suplemento'
    TEMA = 'tema'
    TEMA_EXPEDIENTE = 'tema_expediente'
    TEMARIO = 'temario'
    TIPO_SESION_PERIODO = 'tipo_sesion_periodo'
    TP_DAE = 'tp_dae'
    TRATAMIENTO = 'tratamiento'
    TRATAMIENTO_COMISION_REUNION = 'tratamiento_comision_reunion'
    TRATAMIENTO_EXPEDIENTE = 'tratamiento_expediente'
    TRATAMIENTO_PRODUCE_DESPACHO = 'tratamiento_produce_despacho'
    VETO = 'veto'
    VERSION_TAQUIGRAFICA = 'version_taquigrafica'
    VOTACION = 'votacion'
    VOTACION_SOBRE_DICTAMEN = 'votacion_sobre_dictamen'
    VOTACION_SOBRE_MOCION = 'votacion_sobre_mocion'
    VOTACION_SOBRE_PLANTEAMIENTO = 'votacion_sobre_planteamiento'
    VOTACION_SOBRE_PROPUESTA = 'votacion_sobre_propuesta'

    #APP NAME
    APIREST = 'apirest'
    
    #### DB NAME ####
    PAP = "pap_nueva_pruebas"
    
    #### AUTHENTICATION SERVER DATA ####
#     HAS_PERMISSION_SERVICE ='http://10.105.5.55:9000/o/has_permission/{0}/{1}/{2}/'
#     HAS_PERMISSION_SERVICE ='http://10.105.5.55:9000/o/has_permission/{0}/{1}/{2}/{3}/'
    HAS_PERMISSION_SERVICE ='http://'+settings.AUTH_SERVER['HOST']+ ':' +settings.AUTH_SERVER['PORT']+'/o/has_permission/{0}/{1}/{2}/{3}/'
    AUTH_HEADER_KEY='Authorization'
    AUTH_HEADER_CREDENTIALS='Credential {0} {1}'
    IS_AUTHORIZED_KEY="is_authorized"
    
    #### authorization Exceptions constants     
    NO_AUTH_EXCP = "EXCEPTION: There is NO Authorization in http header."
    NOT_AUTHORIZED_EXCP = "EXCEPTION: Invalid Token. User unauthorized."
    AUTH_FORMAT_EXCP = "EXCEPTION: Invalid Authorization Format. E.g. 'Authorization: Bearer EfbWyP71D6JHcE8vbQ3tBwqVI5iRAz'"
    AUTH_CONNECTION_EXCP = "EXCEPTION: Could not connect to authentication server."
    
    #### ERROR MSGS ####
   
    NO_HEADER_EXC="Header invalido, vacio o inexistente"
    AUTH_FORMAT_EXCP_STR="Authorization header con formato incorrecto. E.g. 'Authorization: Bearer EfbWyP71D6JHcE8vbQ3tBwqVI5iRAz'"
    NO_PERMISSION_STR="Permisos no concedidos."
    NO_ROL_PERMISSION_STR="El usuario no tiene permisos para acceder al servicio"
    NO_SERVICE_PATH="Ruta de servicio inexistente"
    BAD_FORMAT_ERROR="La URL del servicio solicitada no coincide con el formato estipulado. [No Match Error]"
    
    AUTH_HEADER_KEY_CONST='HTTP_AUTHORIZATION'
    BEARER_KEY="Bearer "
    SERVICE_PATH = 'PATH_INFO'
    
    #### ERROR CODES ####
    NO_PERMISSION_EXC_CODE=434
    MISSING_TOKEN_CODE=432
    NO_ROL_PERMISSION_CODE=440
    
    #Logging
    LOG_PROPERTIES='properties.json'
    LOGGING_FOLDER_EXC="No permission to log"
    
    SERVICES_UNIQUE_NAME='servicios-parlamentarios'
    
    #Error message