from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.db.models import Count

from appBuses.serializers import BusSerializer, HorarioServicioSerializer, PersonaSerializer, PasajeSerializer
from appBuses.models import Bus, HorarioServicio, Persona, Pasaje

def busesTrayectoCapacidadMayorCero(request, idTrayecto):
  if request.method == 'GET':

    #1-traer buses que tienenen un trayecto con el id pedido
    #2-quitar repetidos
    #3-contar cantidad de pasajes para cada bus
    #4-filtrar los buses que tienen pasajes 
    data = Bus.objects.filter(horarioservicio__trayecto__idTrayecto=idTrayecto) \
    .distinct() \
    .annotate(cant=Count('horarioservicio__pasaje')) \
    .filter(cant__gt=0)


    # data = data.get(idHorarioServicio__esact=)
    serializer = BusSerializer(data,many=True)
    return JsonResponse(serializer.data, safe=False)
    # buses = Bus.objects.get(idBus__exact=idTrayecto)
    # serializer = BusSerializer(buses)
    # return JsonResponse(serializer.data)

def horarioServicioTrayecto(request, idTrayecto):
  if request.method == 'GET':
    data = HorarioServicio.objects.filter(trayecto__idTrayecto=idTrayecto).order_by('-fechaServicio')

    serializer = HorarioServicioSerializer(data,many=True)
    return JsonResponse(serializer.data, safe=False)

def personasChoferes(request):
  if request.method == 'GET':
    # Se busca por descripción ya que el id puede cambiar
    data = Persona.objects.filter(tipoUsuario__descripcion='chofer')
    serializer = PersonaSerializer(data,many=True)
    return JsonResponse(serializer.data, safe=False)

def personasPasajeros(request):
  if request.method == 'GET':
    # Se busca por descripción ya que el id puede cambiar
    data = Persona.objects.filter(tipoUsuario__descripcion='pasajero')
    serializer = PersonaSerializer(data,many=True)
    return JsonResponse(serializer.data, safe=False)

def pasajesHorarios(request, idHorarioServicio):
  if request.method == 'GET':
    data = Pasaje.objects.filter(horario__idHorarioServicio=idHorarioServicio)
    serializer = PasajeSerializer(data,many=True)
    return JsonResponse(serializer.data, safe=False)