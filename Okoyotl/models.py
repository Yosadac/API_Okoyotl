from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

#--TABLA PRINCIPAL -> INCENDIO--
class Incendio(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    clave = models.CharField(max_length=20, blank=False, null=False)
    fechaIncio = models.DateTimeField(null=False)
    fechaCierre = models.DateTimeField(null=False)
      
    def __str__(self):
        return f"El nombre del incendio es: {self.nombre} y tiene de clave: {self.clave}"

#---------------------------------------------------------------------------------------
#--------------------------CATÁLOGOS----------------------------------------------------
#---------------------------------------------------------------------------------------

#--PUESTO QUE TIENE EL PERSONAL--   
class TipoPuesto(models.Model):
    TIPO_PUESTOS = [
        ('COMANDANTE', 'comandante de incidentes'),
        ('CUADRILLA', 'jefe de cuadrilla'),
        ('COMBATIENTE', 'combatiente de incendios'),
        ('OBSERVADOR', 'observador-vigilante de zona'),
        ('TECNICO', 'técnico de maquinaría y planeación'),
        ('MEDICO', 'médico o paramedico'),
    ]

    tipoUsuario = models.CharField(max_length=20, choices=TIPO_PUESTOS)
      
    def __str__(self):
        return f"La posición del personal es de tipo: {self.tipoUsuario}"

#--TIPOS DE JORNADA--
class TipoJornada(models.Model):
    TIPOS_JORNADA = [
        ('MATUTINA', 'matutina'),
        ('VESPERTINA', 'vespertina'),
        ('NOCTURNA', 'nocturna'),
        ('ACUMULADA', 'acumulada'),
    ]

    nombreJornada = models.CharField(max_length=20, choices=TIPOS_JORNADA)
      
    def __str__(self):
        return f"La jornada del trabajador es: {self.prioridad}"


#--CUADRILLA--
class Cuadrilla(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
      
    def __str__(self):
        return f"El nombre o clave de la cuadrilla es: {self.nombre}"

#--ESTADO DEL RECURSO--
class EstadoRecurso(models.Model):
    TIPOS_ESTADOS = [
        ('LLENO', 'Lleno en su totalidad'),
        ('MEDIO', 'A la mitad de su capacidad'),
        ('VACIO', 'Vaciado por completo'),
        ('DESCOMPUESTO', 'Descompuesto o no disponible'),
        ('OCUPADO', 'Ocupado por otra entidad'),
        ('DISPONIBLE', 'Disponible para asignarse'),
    ]

    estado = models.CharField(max_length=20, choices=TIPOS_ESTADOS)
      
    def __str__(self):
        return f"El estado del recurso es: '{self.estado}'"

#---------------------------------------------------------------------------------------------
#-----------------------TABLAS PRINCIPALES----------------------------------------------------
#---------------------------------------------------------------------------------------------

#--PERSONAL TOTAL CON EL QUE SE CUENTA--
class Personal(models.Model):
    tipoPuesto = models.ForeignKey(TipoPuesto, on_delete=models.CASCADE)
    tipoJornada = models.ForeignKey(TipoJornada, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apPaterno = models.CharField(max_length=100, blank=False, null=False)
    apMaterno = models.CharField(max_length=100, blank=False, null=False)
    edad = models.SmallIntegerField(blank=False, null=False)
    curp = models.CharField(max_length=255, blank=False, null=False)
    numTel = models.BigIntegerField(blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    disponible = models.BooleanField(blank=False,null=False, default=False)
      
    class Meta:
        unique_together = ('tipoPuesto','tipoJornada')

    def __str__(self):
        return f"{self.nombre} {self.apPaterno} {self.apMaterno} {self.email}"

#--IDENTIFICACIÓN DE LOS RECURSOS--
class Recursos(models.Model):
    estadoRecurso = models.ForeignKey(EstadoRecurso, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=20, blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"El recurso es: {self.nombre} y tiene de identificador: {self.identificador}"

#-----------------------------------------------------------------------------------------------------
#-------------------------TABLAS DE RELACIONES--------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#--RELACIÓN: INCENDIO <-> MAPA--
class Mapa(models.Model):
    incendio = models.ForeignKey(Incendio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    latitud = models.FloatField(max_length=20, blank=False, null=False)
    longitud = models.FloatField(max_length=20, blank=False, null=False)
    radio = models.FloatField( blank=False, null=False, default=1)
    fecha = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"La ubicación tiene de nomnre: {self.nombre}"

#--RELACIÓN: PERSONAL <-> INCENDIO--
class RelPersonal(models.Model):
    incendio = models.ForeignKey(Incendio, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    cuadrilla = models.ForeignKey(Cuadrilla, on_delete=models.CASCADE)
    fechaAsignado = models.DateTimeField(blank=False, null=False)
      
    class Meta:
        unique_together = ('incendio','personal','cuadrilla')

    def __str__(self):
        return f"Se asignó el: {self.fechaAsignado}"
    
#--RELACIÓN: RECURSO <-> INCENDIO--
class RelRecurso(models.Model):
    incendio = models.ForeignKey(Incendio, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recursos, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False, blank=False)
      
    class Meta:
        unique_together = ('incendio','recurso')

    def __str__(self):
        return f"El recurso se asignó el: {self.fecha}"
