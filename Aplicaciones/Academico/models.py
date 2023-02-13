from django.db import models

class Curso(models.Model):
   nombre = models.CharField(max_length=30)
   creditos = models.PositiveSmallIntegerField()
   def __str__(self):
      return self.nombre #para que en el panel de administrador nos muestre mejor los datos
# Create your models here.
