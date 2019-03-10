from django.urls import path, include

from rest_framework import routers
from .api import TipoPersonaViewSet, PersonaViewSet, BusViewSet, TrayectoViewSet, HorarioServicioViewSet, PasajeViewSet

from . import views

# urlpatterns = [
#   path('', views.index, name='index'),
#   path('personas', views.personas, name='personas'),
#   path('tipoPersonas', TipoPersonaViewSet, 'tipoPersonas')
#   # path('tipoPersonas', views.tipoPersonas, name='tipoPersonas'),
#   # path('tipoPersonas/<int:pk>', views.tipoPersonasSingle)
# ]

router = routers.DefaultRouter()
router.register('tipoPersonas', TipoPersonaViewSet, 'tipoPersona')
router.register('personas', PersonaViewSet, 'personas')
router.register('buses', BusViewSet, 'buses')
router.register('trayectos', TrayectoViewSet, 'trayectos')
router.register('horarios', HorarioServicioViewSet, 'horarios')
router.register('pasajes', PasajeViewSet, 'pasajes')

urlpatterns = [
  path('', include(router.urls)),
  path('busesMayorCero/<int:idTrayecto>',views.busesTrayectoCapacidadMayorCero),
  path('horariosTrayecto/<int:idTrayecto>', views.horarioServicioTrayecto),
  path('personasChoferes', views.personasChoferes),
  path('pasajesHorario/<int:idHorarioServicio>',views.pasajesHorarios),
  path('personasPasajeros', views.personasPasajeros)
]