from django.shortcuts import render
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from appBuses.serializers import TipoPersonaSerializer
from appBuses.models import TipoPersona

def index(request):
    return HttpResponse("You are in appBuses app")

@csrf_exempt
def personas(request): 
  if request.method == 'GET':
    return JsonResponse({'Message':'Hola'}) 