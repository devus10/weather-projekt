from django.db import models

class Miasto(models.Model):
    nazwa_miasta = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()
    temperatura = models.FloatField()

