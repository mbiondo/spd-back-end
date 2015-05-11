from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from apirest.views.cargos import cargo
from apirest.views.individuos import persona_fisica, legislador
from apirest.views.expedientes import expediente
from apirest.views.organismos.comisiones import comision
from apirest.views.organismos.bloques import bloque
from rest_framework_nested import routers
from apirest.views.firmantes import FirmantesViewSet
from apirest.views.giros import GirosViewSet
from apirest.views.persona_fisica_detalle import PersonaFisicaDetalleViewSet
from apirest.views.proyectos import ProyectosViewSet
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
from apirest.views.publicaciones.publicacion import PublicacionViewSet
from apirest.views.publicaciones.tramite_parlamentario import TramiteParlamentarioViewSet
from apirest.views.publicaciones.boletin_asuntos_entrados import BoletinAsuntosEntradosViewSet
from apirest.views.publicaciones.boletin_asuntos_tratados import BoletinAsuntosTratadosViewSet
from apirest.views.publicaciones.boletin_novedades import BoletinNovedadesViewSet
from apirest.views.publicaciones.diario_asuntos_entrados import DiarioAsuntosEntradosViewSet

router = DefaultRouter()

router.register(r'bloques', bloque.BloqueViewSet)
router.register(r'cargos', cargo.CargoViewSet)
router.register(r'citaciones', CitacionViewSet)
router.register(r'comisiones', comision.ComisionViewSet)
router.register(r'despachos',DespachoViewSet)
router.register(r'dictamenes', DictamenViewSet)
router.register(r'expedientes', expediente.ExpedienteViewSet)
router.register(r'legisladores', legislador.LegisladorViewSet)
router.register(r'personas_fisicas', persona_fisica.PersonaFisicaViewSet)
router.register(r'personas_fisicas_detalle', PersonaFisicaDetalleViewSet)
router.register(r'proyectos', ProyectosViewSet)
router.register(r'lugares', LugarViewSet)
router.register(r'estados', AuxEstadoViewSet)
router.register(r'invitados', CitacionInvitaEntidadViewSet)
router.register(r'resultados',ResultadoViewSet)
router.register(r'citaciones_gpa', CitacionGpaViewSet)
router.register(r'gpas', GpaViewSet)
router.register(r'invitados_gpa', CitacionGpaInvitaEntidadViewSet)
router.register(r'publicacion', PublicacionViewSet)
router.register(r'tramites_parlamentarios', TramiteParlamentarioViewSet)
router.register(r'boletin_asuntos_entrados', BoletinAsuntosEntradosViewSet)
router.register(r'boletin_asuntos_tratados', BoletinAsuntosTratadosViewSet)
router.register(r'boletin_novedades', BoletinNovedadesViewSet)
router.register(r'diario_asuntos_entrados', DiarioAsuntosEntradosViewSet)
# router.register(r'personas_fisicas', persona_fisica.PersonaFisicaFullViewSet)
# router.register(r'personas_fisicas_datos_actuales', persona_fisica.PersonaFisicaActualViewSet)
# router.register(r'legisladores', legislador.LegisladorComisionViewSet)
# router.register(r'comisiones_historico', comision.ComisionHistoricoViewSet)
# router.register(r'comisiones_detalle', comision.ComisionDetalleViewSet)
# router.register(r'bloques_detalle', bloque.BloqueDetalleViewSet)


expediente_router = routers.NestedSimpleRouter(router, r'expedientes', lookup='expediente')
expediente_router.register(r'firmantes',FirmantesViewSet)
expediente_router.register(r'giros',GirosViewSet)



urlpatterns = patterns('apirest.views',
    url(r'^', include(router.urls)),
    url(r'^', include(expediente_router.urls)),
)
