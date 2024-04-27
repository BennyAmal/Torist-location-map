from django.db import models

# Create your models here.
class Destination(models.Model):
    place_name = models.CharField(max_length=200)
    weather = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    google_map_link = models.URLField()
    image = models.ImageField(upload_to='destinations/')
    description = models.CharField(max_length=1000)