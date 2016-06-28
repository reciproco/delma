from django.db import models
import os
from uuid import uuid4
from django.utils.translation import ugettext_lazy as _

def path_and_rename(instance, filename):
    instance.nombre = filename
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return filename

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido1 = models.CharField(max_length=32)
    apellido2 = models.CharField(max_length=32)
    direccion = models.CharField(max_length=512)
    telefono = models.CharField(max_length=32)
    correo = models.EmailField()
    dni = models.CharField(max_length=16)
    nacimiento = models.DateTimeField()
    alta = models.DateTimeField()

    def _get_nombre_completo(self):
        "Devuelve el nombre completo de la persona."
        return '%s %s %s' % (self.nombre, self.apellido1, self.apellido2)
    nombre_completo = property(_get_nombre_completo)

    def __str__(self):
        return self.nombre_completo

class Ficha(models.Model):

    TERAPEUTA_CHOICES = (
        ('ALB', _('ALBERTO')),
        ('DEL', _('DELFIN')),
        ('CAR', _('CAROLINA')),
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    lesion = models.CharField(max_length=1024)
    cuando  = models.DateTimeField()
    como = models.CharField(max_length=1024)
    tratamiento_ee = models.BooleanField(default=False)
    tratamiento_ir = models.BooleanField(default=False)
    tratamiento_tm = models.BooleanField(default=False)
    tratamiento_us = models.BooleanField(default=False)
    tratamiento_l = models.BooleanField(default=False)
    tratamiento_mg = models.BooleanField(default=False)
    tratamiento_cines = models.BooleanField(default=False)
    tratamiento_synm = models.BooleanField(default=False)
    tratamiento_tc = models.BooleanField(default=False)
    tratamiento_ps = models.BooleanField(default=False)
    tratamiento_epte = models.BooleanField(default=False)
    observaciones = models.TextField()
    terapeuta = models.CharField(max_length=3,choices=TERAPEUTA_CHOICES, default='ALB')
    dolor = models.CharField(max_length=128)
    sesiones = models.TextField(max_length=1024)

    def __str__(self):
        return self.paciente.nombre_completo

class Adjunto(models.Model):
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    nombre  =  models.CharField(max_length=128)
    fichero = models.FileField(upload_to=path_and_rename)

class Abono(models.Model):
    cliente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    periodo_inicio  = models.DateField()
    periodo_fin  = models.DateField()
    importe = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True,default=0)
    pagado = models.BooleanField(default=False)
