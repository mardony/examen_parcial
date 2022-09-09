from django.db import models
import datetime

# Create your models here.
class usuario(models.Model):
     nombre = models.CharField(max_length=128,default='')
     apellido=models.CharField(max_length=128,default='')
     codigo_usuario = models.CharField(max_length=128,default='')
     psw_usuario = models.CharField(max_length=128, default='')

class tarea(models.Model):
      Descripcion=models.CharField(max_length=500,default='')
      fecha_creacion = models.DateField(default=datetime.date.today)
      fecha_entrega = models.DateField(null=True)
      usuario_responsable = models.CharField(max_length=128,default='0')
      estado_tarea = models.CharField(max_length=128,default='Programado')

