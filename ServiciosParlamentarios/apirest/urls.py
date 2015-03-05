from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from apirest.views.cargos import cargo
from apirest.views.individuos import persona_fisica, legislador
from apirest.views.expedientes import expediente
from apirest.views.organismos.comisiones import comision
from apirest.views.organismos.bloques import bloque
from rest_framework_nested import routers
from apirest.views.firmantes import FirmantesViewSet
from apirest.views.persona_fisica_detalle import PersonaFisicaDetalleViewSet

router = DefaultRouter()

router.register(r'cargos', cargo.CargoViewSet)
router.register(r'personas_fisicas', persona_fisica.PersonaFisicaViewSet)
router.register(r'personas_fisicas_detalle', PersonaFisicaDetalleViewSet)
# router.register(r'personas_fisicas', persona_fisica.PersonaFisicaFullViewSet)
# router.register(r'personas_fisicas_datos_actuales', persona_fisica.PersonaFisicaActualViewSet)
router.register(r'legisladores', legislador.LegisladorViewSet)
# router.register(r'legisladores', legislador.LegisladorComisionViewSet)
router.register(r'expedientes', expediente.ExpedienteViewSet)
router.register(r'comisiones', comision.ComisionViewSet)
# router.register(r'comisiones_historico', comision.ComisionHistoricoViewSet)
# router.register(r'comisiones_detalle', comision.ComisionDetalleViewSet)
router.register(r'bloques', bloque.BloqueViewSet)
# router.register(r'bloques_detalle', bloque.BloqueDetalleViewSet)

expediente_router = routers.NestedSimpleRouter(router, r'expedientes', lookup='expediente')
expediente_router.register(r'firmantes',FirmantesViewSet)

urlpatterns = patterns('apirest.views',
    url(r'^', include(router.urls)),
    url(r'^', include(expediente_router.urls)),
)


