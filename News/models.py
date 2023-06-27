from django.db import models

# Create your models here.
class news (models.Model):
    id = models.IntegerField(primary_key=True)
    newname = models.CharField(max_length=50)
    image = models.URLField (max_length=400)
    title = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)