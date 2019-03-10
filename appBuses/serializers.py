from rest_framework import serializers, fields
from .models import TipoPersona, Persona, Bus, Trayecto, HorarioServicio, Pasaje

class TipoPersonaSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoPersona
    fields = '__all__'

  # idTipoPersona = serializers.IntegerField(read_only=True, required=False)
  # descripcion = serializers.CharField(max_length=30)
  # fecIngresoReg = serializers.DateTimeField(required=False)
  # fecUltActReg = serializers.DateTimeField(required=False)
  # estadoReg = serializers.BooleanField(required=False)

  # def create(self, validated_data):
  #   return TipoPersona.objects.create(**validated_data)

  # def update(self, instance, validated_data):
  #   instance.descripcion = validated_data.get('descripcion',instance.descripcion)
  #   instance.save()
  #   return instance

class PersonaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Persona
    fields = ('__all__')

  def to_representation(self, instance):
    representation = super(PersonaSerializer, self).to_representation(instance)
    representation['tipoUsuarioDescripcion'] = instance.tipoUsuario.descripcion
    return representation

class BusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bus
    fields = '__all__'

class TrayectoSerializer(serializers.ModelSerializer):
  class Meta:
    model =Trayecto
    fields = '__all__'

class HorarioServicioSerializer(serializers.ModelSerializer):
  fechaServicio = fields.DateField(input_formats=['%Y-%m-%d'])
  horaInicio = fields.TimeField(input_formats=['%H:%M:%S'])
  horaFin = fields.TimeField(input_formats=['%H:%M:%S'])

  class Meta:
    model = HorarioServicio
    fields = '__all__'
  
  def to_representation(self, instance):
    representation = super(HorarioServicioSerializer, self).to_representation(instance)
    representation['bus'] = {
      "idBus": instance.bus.idBus,
      "modelo": instance.bus.modelo,
      "patente": instance.bus.patente,
      "capacidadPasajeros": instance.bus.capacidadPasajeros
    }
    representation['chofer'] = {
      "idPersona": instance.chofer.idPersona,
      "identificacionPais": instance.chofer.identificacionPais,
      "nombrePrimario": instance.chofer.nombrePrimario,
      "nombreSecundario": instance.chofer.nombreSecundario,
      "apPaterno": instance.chofer.apPaterno,
      "apMaterno": instance.chofer.apMaterno
    }
    representation['trayecto'] = {
      "idTrayecto": instance.trayecto.idTrayecto,
      "ciudadSalida": instance.trayecto.ciudadSalida,
      "ciudadLlegada": instance.trayecto.ciudadLlegada
    }
    return representation

class PasajeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pasaje
    fields = '__all__'
  def to_representation(self, instance):
    representation = super(PasajeSerializer, self).to_representation(instance)
    representation['id']: instance.id
    representation['pasajero'] = {
      "idPersona": instance.pasajero.idPersona,
      "identificacionPais": instance.pasajero.identificacionPais,
      "nombrePrimario": instance.pasajero.nombrePrimario,
      "nombreSecundario": instance.pasajero.nombreSecundario,
      "apPaterno": instance.pasajero.apPaterno,
      "apMaterno": instance.pasajero.apMaterno
    }
    return representation



# class PersonaSerializer(serializers.Serializer):

#   idPersona = serializers.IntegerField(read_only=True, required=False)
#   identificacionPais = serializers.CharField(max_length=15)
#   nombrePrimario = serializers.CharField(max_length=45)
#   nombreSecundario = serializers.CharField(max_length=45)
#   apPaterno = serializers.CharField(max_length=45)
#   apMaterno = serializers.CharField(max_length=45)
#   fecIncorporacion = serializers.DateField()
#   fecIngresoReg = serializers.DateTimeField()
#   fecUltActReg = serializers.DateTimeField()
#   estadoReg = serializers.BooleanField()
#   tipoUsuario = serializers.SlugRelatedField(querySet=TipoPersona.objects.all())

#   def create(self, validated_data):
#     return Persona.objects.create(**validated_data)
  
#   def update(self, instance, validated_data):
#     nombrePrimario = serializers.CharField(max_length=45)
#     nombreSecundario = serializers.CharField(max_length=45)
#     instance.save()
#     return instance