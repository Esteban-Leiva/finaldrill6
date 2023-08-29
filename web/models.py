from django.db import models

# Create your models here.
class Autos (models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    carroceria = models.CharField(max_length=50)
    motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    precio = models.IntegerField()
