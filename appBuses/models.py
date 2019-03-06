from django.db import models
import datetime

# Create your models here.

class TipoPersona(models.Model):
  idTipoPersona = models.AutoField(primary_key=True)
  descripcion = models.CharField(max_length=30)
  fecIngresoReg = models.DateTimeField(auto_now_add=True)
  fecUltActReg = models.DateTimeField(auto_now_add=True)
  estadoReg = models.BooleanField(default=True)

  def __str__(self):
    return self.descripcion

class Persona(models.Model):
  idPersona = models.AutoField(primary_key=True )
  identificacionPais = models.CharField(max_length=15)
  nombrePrimario = models.CharField(max_length=45)
  nombreSecundario = models.CharField(max_length=45, null=True)
  apPaterno = models.CharField(max_length=45)
  apMaterno = models.CharField(max_length=45)
  fecIncorporacion = models.DateField(auto_now_add=True)
  fecIngresoReg = models.DateTimeField(auto_now_add=True)
  fecUltActReg = models.DateTimeField(auto_now_add=True)
  estadoReg = models.BooleanField(default=True)
  tipoUsuario = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombrePrimario

class Bus(models.Model):
  idBus = models.AutoField(primary_key=True)
  patente = models.CharField(max_length=10)
  modelo = models.CharField(max_length=50)
  capacidadPasajeros = models.IntegerField(default=10)
  fecIngresoReg = models.DateTimeField(auto_now_add=True)
  fecUltActReg = models.DateTimeField(auto_now_add=True)
  estadoReg = models.BooleanField(default=True)

  def __str__(self):
    return self.modelo

class Trayecto(models.Model):
  idTrayecto = models.AutoField(primary_key=True)
  ciudadSalida = models.CharField(max_length=100)
  ciudadLlegada = models.CharField(max_length=100)
  fecIngresoReg = models.DateTimeField(auto_now_add=True)
  fecUltActReg = models.DateTimeField(auto_now_add=True)
  estadoReg = models.BooleanField(default=True)

  def __str__(self):
    return self.ciudadSalida+'-'+self.ciudadLlegada

class HorarioServicio(models.Model):
  idHorarioServicio = models.AutoField(primary_key=True)
  fechaServicio = models.DateField()
  horaInicio = models.TimeField()
  horaFin = models.TimeField()
  fecIngresoReg = models.DateTimeField(auto_now_add=True)
  fecUltActReg = models.DateTimeField(auto_now_add=True)
  estadoReg = models.BooleanField(default=True)
  bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
  chofer = models.ForeignKey(Persona, on_delete=models.CASCADE)
  trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)

  def __str__(self):
    return unicode(self.horaInicio)+'//'+ unicode(self.horaFin)

class Pasaje(models.Model):
  horario = models.ForeignKey(HorarioServicio, on_delete=models.CASCADE)
  pasajero = models.ForeignKey(Persona, on_delete=models.CASCADE)
  numeroAsiento = models.CharField(max_length=2) #por si es asiento con alfanumericos
  fecIngresoReg = models.DateTimeField(auto_now_add=True)
  fecUltActReg = models.DateTimeField(auto_now_add=True)
  estadoReg = models.BooleanField(default=True)

  def __str__(self):
    return self.horario+'/'+self.pasajero