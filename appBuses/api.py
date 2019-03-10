from .models import TipoPersona, Persona, Bus, Trayecto, HorarioServicio, Pasaje
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TipoPersonaSerializer, PersonaSerializer, BusSerializer, TrayectoSerializer, HorarioServicioSerializer, PasajeSerializer

class TipoPersonaViewSet(viewsets.ModelViewSet):
  queryset = TipoPersona.objects.all()
  serializer_class = TipoPersonaSerializer
  permission_classes = [
    permissions.AllowAny
  ]

class PersonaViewSet(viewsets.ModelViewSet):
  queryset = Persona.objects.all()
  serializer_class = PersonaSerializer
  permission_classes = [
    permissions.AllowAny
  ]

class BusViewSet(viewsets.ModelViewSet):
  queryset = Bus.objects.all()
  serializer_class = BusSerializer
  permission_classes = [
    permissions.AllowAny
  ]
  
  @action(detail=False, methods=['GET'], url_path='busesCapacidad/{pk}')
  def busesCapacidad(self, request, pkTrayecto, pk=None):
    buses = Bus.objects.all()
    serializer = self.get_serializer(buses, many=True)
    return Response({'status': 'ok'})

  

class TrayectoViewSet(viewsets.ModelViewSet):
  queryset = Trayecto.objects.all()
  serializer_class = TrayectoSerializer
  permission_classes = [
    permissions.AllowAny
  ]

class HorarioServicioViewSet(viewsets.ModelViewSet):
  queryset = HorarioServicio.objects.all()
  serializer_class = HorarioServicioSerializer
  permission_classes = [
    permissions.AllowAny
  ]

class PasajeViewSet(viewsets.ModelViewSet):
  queryset = Pasaje.objects.all()
  serializer_class = PasajeSerializer
  permission_classes = [
    permissions.AllowAny
  ]