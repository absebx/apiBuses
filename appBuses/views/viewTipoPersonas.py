from django.shortcuts import render
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from appBuses.serializers import TipoPersonaSerializer
from appBuses.models import TipoPersona

@csrf_exempt
def tipoPersonas(request):
  if request.method == 'GET':
    tipos = TipoPersona.objects.all()
    serializer = TipoPersonaSerializer(tipos, many=True)
    # print(serializer.data)
    return JsonResponse(serializer.data, safe=False)

  if request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = TipoPersonaSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tipoPersonasSingle(request,pk):
  try:
    tipoPersona = TipoPersona.objects.get(pk=pk)
  except TipoPersona.DoesNotExist:
    return HttpResponse(status=404)
  
  if request.method == 'GET':
    serializer = TipoPersonaSerializer(tipoPersona)
    return JsonResponse(serializer.data)
    
  if request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = TipoPersonaSerializer(tipoPersona, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors,status=400)
  
  if request.method == 'DELETE':
    tipoPersona.delete()
    return HttpResponse(status=204)