from django.db import models


# Create your models here.
class Station(models.Model):
    name = models.TextField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    tubeLine = models.TextField(max_length=50, default='LINE')
    adjacencyList = models.JSONField()
