from rest_framework import serializers
from .models import TipoPersona, Persona, Bus

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
        representation['tipoUsuario'] = instance.tipoUsuario.descripcion
        return representation

class BusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bus
    fields = '__all__'

  

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