# from django.urls import path

from rest_framework import routers
from .api import TipoPersonaViewSet, PersonaViewSet, BusViewSet

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
router.register('buses', BusViewSet, 'buses'  )

urlpatterns = router.urls