from .models import TipoPersona, Persona, Bus
from rest_framework import viewsets, permissions
from .serializers import TipoPersonaSerializer, PersonaSerializer, BusSerializer

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
