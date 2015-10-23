from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from apirest.views.cargos import cargo
from apirest.views.individuos import persona_fisica, legislador
from apirest.views.organismos.comisiones import comision
from apirest.views.organismos.bloques import bloque
from rest_framework_nested import routers
from apirest.views.firmantes import FirmantesViewSet
from apirest.views.giros import GirosViewSet
from apirest.views.citacion import CitacionViewSet
from apirest.views.expedientes.dictamen import DictamenViewSet
from apirest.views.organismos.despacho import DespachoViewSet
from apirest.views.lugar import LugarViewSet
from apirest.views.aux_estado import AuxEstadoViewSet
from apirest.views.individuos.invitados import CitacionInvitaEntidadViewSet
from apirest.views.expedientes.resultado import ResultadoViewSet
from apirest.views.citacion_gpa import CitacionGpaViewSet
from apirest.views.organismos.gpa import GpaViewSet
from apirest.views.individuos.invitados_gpa import CitacionGpaInvitaEntidadViewSet
from apirest.views.publicaciones.tramite_parlamentario import TramiteParlamentarioViewSet
from apirest.views.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntradosViewSet
from apirest.views.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratadosViewSet
from apirest.views.publicaciones.boletin_novedades import BoletinNovedadesViewSet
from apirest.views.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntradosViewSet
from apirest.views.publicaciones.orden_dia import OrdenDiaViewSet
from apirest.views.sancion import SancionViewSet
from apirest.views.expedientes.proyecto import ProyectoViewSet
from apirest.views.expedientes.comunicacion import ComunicacionViewSet
from apirest.views.expedientes.observacion import ObservacionViewSet
from apirest.views.expedientes.comunicacion_pen import ComunicacionPenViewSet
from apirest.views.expedientes.solicitud import SolicitudViewSet
from apirest.views.giro import GiroViewSet
from apirest.views.expedientes.insistencia import InsistenciaViewSet
from apirest.views.expedientes.aprobacion_simple import AprobacionSimpleViewSet
from apirest.views.plan_labor import PlanLaborViewSet
from apirest.views.plp_detalle_estructura import PlpDetalleEstructuraViewSet
from apirest.views.sesion import SesionViewSet
from apirest.views.mocion import MocionViewSet
from apirest.views.organismos.comisiones.comision_reunion import ComisionReunionViewSet
from apirest.views.organismos.comisiones.com_estructura import ComEstructuraViewSet
from apirest.views.organismos.bloques.bloque_estructura import BloqueEstructuraViewSet
from apirest.views.periodo import PeriodoViewSet
from apirest.views.debate import DebateViewSet
from apirest.views.expedientes.mansaje import MensajeViewSet


router = DefaultRouter()

router.register(r'bloques', bloque.BloqueViewSet)
router.register(r'cargos', cargo.CargoViewSet)
router.register(r'citaciones', CitacionViewSet)
router.register(r'comisiones', comision.ComisionViewSet)
router.register(r'legisladores_comisiones', ComEstructuraViewSet)
router.register(r'despachos',DespachoViewSet)
router.register(r'dictamenes', DictamenViewSet)
router.register(r'legisladores', legislador.LegisladorViewSet)
router.register(r'personas_fisicas', persona_fisica.PersonaFisicaViewSet)
router.register(r'lugares', LugarViewSet)
router.register(r'estados', AuxEstadoViewSet)
router.register(r'invitados', CitacionInvitaEntidadViewSet)
router.register(r'citaciones_gpa', CitacionGpaViewSet)
router.register(r'gpas', GpaViewSet)
router.register(r'invitados_gpa', CitacionGpaInvitaEntidadViewSet)
router.register(r'tramites_parlamentarios', TramiteParlamentarioViewSet)
router.register(r'boletines_asuntos_entrados', BoletinAsuntosEntradosViewSet)
router.register(r'boletines_asuntos_tratados', BoletinAsuntosTratadosViewSet)
router.register(r'boletines_novedades', BoletinNovedadesViewSet)
router.register(r'diarios_asuntos_entrados', DiarioAsuntosEntradosViewSet)
router.register(r'ordenes_del_dia', OrdenDiaViewSet, 'OrdenDia')
router.register(r'proyectos',ProyectoViewSet)
router.register(r'comunicaciones',ComunicacionViewSet)
router.register(r'observaciones',ObservacionViewSet)
router.register(r'comunicaciones_pen',ComunicacionPenViewSet)
router.register(r'solicitudes',SolicitudViewSet)
router.register(r'giros',GiroViewSet)

router.register(r'resultados',ResultadoViewSet)
router.register(r'sanciones', SancionViewSet)
router.register(r'insistencias',InsistenciaViewSet)
router.register(r'aprobaciones_simples',AprobacionSimpleViewSet)
router.register(r'planes_de_labor',PlanLaborViewSet)
router.register(r'plp_detalles_estructura',PlpDetalleEstructuraViewSet)
router.register(r'sesiones',SesionViewSet)
router.register(r'mociones',MocionViewSet)

router.register(r'partes',ComisionReunionViewSet)
router.register(r'periodos',PeriodoViewSet)
router.register(r'debates',DebateViewSet)

router.register(r'legisladores_bloques',BloqueEstructuraViewSet)
router.register(r'mensajes',MensajeViewSet)
# router.register(r'firmantes',FirmantesViewSet)


# router.register(r'personas_fisicas', persona_fisica.PersonaFisicaFullViewSet)
# router.register(r'personas_fisicas_datos_actuales', persona_fisica.PersonaFisicaActualViewSet)
# router.register(r'legisladores', legislador.LegisladorComisionViewSet)
# router.register(r'comisiones_historico', comision.ComisionHistoricoViewSet)
# router.register(r'comisiones_detalle', comision.ComisionDetalleViewSet)
# router.register(r'bloques_detalle', bloque.BloqueDetalleViewSet)

# 
proyecto_router = routers.NestedSimpleRouter(router, r'proyectos', lookup='proyectos')
proyecto_router.register(r'firmantes',FirmantesViewSet)
proyecto_router.register(r'giros',GirosViewSet)

urlpatterns = patterns('apirest.views',
    url(r'^', include(router.urls)),
    url(r'^', include(proyecto_router.urls)),
)
