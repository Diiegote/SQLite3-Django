from django.db import models

class Curso(models.Model):
   nombre = models.CharField(max_length=30)
   creditos = models.PositiveSmallIntegerField()
# Create your models here.
