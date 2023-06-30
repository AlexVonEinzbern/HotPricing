from django.db import models

# Create your models here.
class Hoteles (models.Model):
    id = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=50)
    hotelname = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    precio_antes = models.DecimalField(max_digits=20, decimal_places=5)
    precio_ahora = models.DecimalField(max_digits=20, decimal_places=5)
    imagen_uno = models.BinaryField()
    imagen_dos = models.BinaryField()
    visitas = models.IntegerField()
    reservas = models.IntegerField()
    urls = models.CharField(max_length=200)